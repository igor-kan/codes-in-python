import unittest
from core import WeightedPrefixTrie
from fast_path import count_prefix_matches
from invariants import verify_top_k
from validation import validate_query


class TestWeightedTrie(unittest.TestCase):
    def test_ranking_tiebreak(self) -> None:
        trie = WeightedPrefixTrie()
        data = {"apple": 5, "app": 5, "apply": 8, "apex": 2, "banana": 9}
        for w, sc in data.items():
            trie.insert(w, sc)
        validate_query("ap", 3)
        res = trie.top_k("ap", 3)
        verify_top_k(data, "ap", 3, res)
        self.assertEqual([r.term for r in res], ["apply", "app", "apple"])
        self.assertEqual(count_prefix_matches(trie.root, "ap"), 4)


if __name__ == "__main__":
    unittest.main()
