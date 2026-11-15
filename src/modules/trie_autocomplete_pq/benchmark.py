import time
from core import WeightedPrefixTrie


def main() -> None:
    trie = WeightedPrefixTrie()
    for i in range(5000):
        trie.insert(f"key_{i % 50}_{i}", (i % 100) + 1)
    t0 = time.perf_counter_ns()
    res = trie.top_k("key_12_", 10)
    elapsed = (time.perf_counter_ns() - t0) / 1e6
    assert len(res) == 10
    print(f"trie_autocomplete_pq: {elapsed:.3f} ms hits={len(res)}")


if __name__ == "__main__":
    main()
