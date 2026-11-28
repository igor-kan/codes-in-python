import unittest
from core import *
from concurrency import parallel_fold_batches

class TestProperties(unittest.TestCase):
    def test_properties(self) -> None:
        chks = parallel_fold_batches([[1, 2], [3, 4]])
        self.assertEqual(len(chks), 2)
        edges2 = [(0, 1, 1, 0), (1, 3, 1, 0), (0, 2, 1, -1), (2, 3, 1, 0)]
        res2 = min_cost_flow(4, 0, 3, edges2)
        self.assertEqual(res2.flow, 2)
        self.assertEqual(res2.cost, -1)
        with self.assertRaises(ValidationError):
            min_cost_flow(2, 0, 0, [])

if __name__ == "__main__":
    unittest.main()
