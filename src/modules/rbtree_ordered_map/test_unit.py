import unittest
from core import RedBlackOrderedMap
from fast_path import lower_bound
from invariants import verify_rbtree
from validation import validate_range_bounds


class TestRedBlackMap(unittest.TestCase):
    def test_sorted_and_reversed_insert(self) -> None:
        m = RedBlackOrderedMap()
        validate_range_bounds(0, 20)
        for i in range(20, 0, -1):
            m.insert(i, i * 10)
            verify_rbtree(m)
        self.assertEqual(m.count, 20)
        self.assertEqual(m.get(7), 70)
        self.assertEqual(lower_bound(m, 14), 14)
        self.assertEqual([k for k, _ in m.inorder_items()], list(range(1, 21)))


if __name__ == "__main__":
    unittest.main()
