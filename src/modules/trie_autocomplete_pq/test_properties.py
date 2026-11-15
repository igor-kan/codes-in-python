import random
import unittest
from core import WeightedPrefixTrie
from invariants import verify_top_k


class TestTrieProperties(unittest.TestCase):
    def test_differential_corpus(self) -> None:
        rng = random.Random(55)
        trie = WeightedPrefixTrie()
        model = {}
        alphabet = "abc"
        for _ in range(100):
            word = "".join(rng.choice(alphabet) for _ in range(rng.randint(1, 5)))
            w = rng.randint(1, 10)
            trie.insert(word, w)
            model[word] = model.get(word, 0) + w
        for p in ("", "a", "ab", "c", "zzz"):
            res = trie.top_k(p, 5)
            verify_top_k(model, p, 5, res)


if __name__ == "__main__":
    unittest.main()
