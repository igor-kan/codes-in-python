from typing import List, Sequence, Tuple
from models import XorFilterTable
from validation import validate_xor_keys


def _mix64(x: int) -> int:
    x &= 0xFFFFFFFFFFFFFFFF
    x = ((x ^ (x >> 30)) * 0xBF58476D1CE4E5B9) & 0xFFFFFFFFFFFFFFFF
    x = ((x ^ (x >> 27)) * 0x94D049BB133111EB) & 0xFFFFFFFFFFFFFFFF
    return (x ^ (x >> 31)) & 0xFFFFFFFFFFFFFFFF


def _slots(key: int, seed: int, block_len: int) -> Tuple[int, int, int, int]:
    h = _mix64(key ^ seed)
    r0 = h & 0xFFFFFFFF
    r1 = ((h >> 32) ^ _mix64(h ^ 0x517CC1B727220A95)) & 0xFFFFFFFF
    r2 = _mix64(h ^ 0x9E3779B97F4A7C15)
    h0 = r0 % block_len
    h1 = block_len + (r1 % block_len)
    h2 = 2 * block_len + ((r2 >> 16) % block_len)
    fp = (h ^ (h >> 16)) & 0xFFFF
    return h0, h1, h2, fp


class Xor16Filter:
    def build(self, keys: Sequence[int]) -> XorFilterTable:
        uniq = validate_xor_keys(keys)
        n = len(uniq)
        if n == 0:
            return XorFilterTable(1, 1, (0, 0, 0), 0)
        cap = max(32, int(1.25 * n) + 32)
        cap = ((cap + 2) // 3) * 3
        blk = cap // 3

        for attempt in range(32):
            seed = 0x9E3779B97F4A7C15 + attempt * 0x1000193
            counts = [0] * cap
            xors = [0] * cap
            for k in uniq:
                i0, i1, i2, _ = _slots(k, seed, blk)
                counts[i0] += 1; xors[i0] ^= k
                counts[i1] += 1; xors[i1] ^= k
                counts[i2] += 1; xors[i2] ^= k

            alone = [i for i in range(cap) if counts[i] == 1]
            stack: List[Tuple[int, int]] = []
            seen_keys = set()
            idx_q = 0
            while idx_q < len(alone):
                slot = alone[idx_q]
                idx_q += 1
                if counts[slot] != 1:
                    continue
                k = xors[slot]
                if k in seen_keys:
                    continue
                seen_keys.add(k)
                stack.append((k, slot))
                for pos in _slots(k, seed, blk)[:3]:
                    counts[pos] -= 1
                    xors[pos] ^= k
                    if counts[pos] == 1:
                        alone.append(pos)

            if len(stack) == n:
                b = [0] * cap
                for k, target_slot in reversed(stack):
                    i0, i1, i2, fp = _slots(k, seed, blk)
                    val = fp ^ b[i0] ^ b[i1] ^ b[i2]
                    b[target_slot] = val
                return XorFilterTable(blk, seed, tuple(b), n)

        raise RuntimeError("XOR filter hypergraph peeling exceeded retry budget")

    def contains(self, filt: XorFilterTable, key: int) -> bool:
        if filt.num_keys == 0:
            return False
        i0, i1, i2, fp = _slots(key, filt.seed, filt.block_len)
        return (filt.b[i0] ^ filt.b[i1] ^ filt.b[i2]) == fp
