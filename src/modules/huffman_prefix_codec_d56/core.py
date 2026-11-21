from typing import Dict, List, Optional, Tuple
import heapq
import math
from models import *
from exceptions import ValidationError

def build_huffman_codes(freqs: Dict[str, int]) -> Dict[str, str]:
    if not freqs:
        raise ValidationError("empty frequency map")
    if len(freqs) == 1:
        k = next(iter(freqs))
        return {k: "0"}
    heap: List[Tuple[int, int, object]] = []
    uid = 0
    for ch, f in sorted(freqs.items()):
        heapq.heappush(heap, (f, uid, ch))
        uid += 1
    while len(heap) > 1:
        f1, _, n1 = heapq.heappop(heap)
        f2, _, n2 = heapq.heappop(heap)
        heapq.heappush(heap, (f1 + f2, uid, (n1, n2)))
        uid += 1
    out: Dict[str, str] = {}

    def walk(node: object, prefix: str) -> None:
        if isinstance(node, str):
            out[node] = prefix
        else:
            left, right = node  # type: ignore[misc]
            walk(left, prefix + "0")
            walk(right, prefix + "1")

    walk(heap[0][2], "")
    return out

def huffman_roundtrip(text: str) -> str:
    freq: Dict[str, int] = {}
    for ch in text:
        freq[ch] = freq.get(ch, 0) + 1
    codes = build_huffman_codes(freq)
    rev = {v: k for k, v in codes.items()}
    bits = "".join(codes[ch] for ch in text)
    cur = ""
    dec: List[str] = []
    for b in bits:
        cur += b
        if cur in rev:
            dec.append(rev[cur])
            cur = ""
    return "".join(dec)
