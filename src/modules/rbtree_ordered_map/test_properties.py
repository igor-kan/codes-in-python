import random
import unittest
from core import RedBlackOrderedMap
from invariants import verify_rbtree


class TestRedBlackProperties(unittest.TestCase):
    def test_random_insert_permutations(self) -> None:
        rng = random.Random(909)
        m = RedBlackOrderedMap()
        ref = {}
        for _ in range(150):
            k = rng.randint(-50, 50)
            v = rng.randint(0, 1000)
            m.insert(k, v)
            ref[k] = v
            verify_rbtree(m)
        self.assertEqual(m.inorder_items(), sorted(ref.items()))


if __name__ == "__main__":
    unittest.main()
