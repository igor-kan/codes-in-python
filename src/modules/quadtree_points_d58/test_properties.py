import unittest
from core import *
from concurrency import parallel_fold_batches

class TestProperties(unittest.TestCase):
    def test_properties(self) -> None:
        chks = parallel_fold_batches([[1, 2], [3, 4]])
        self.assertEqual(len(chks), 2)
        qt = QuadNode(0.0, 0.0, 10.0, 10.0)
        qt.insert((2.0, 2.0))
        self.assertEqual(qt.query_box(5.0, 5.0, 9.0, 9.0), [])

if __name__ == "__main__":
    unittest.main()
