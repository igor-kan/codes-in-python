import unittest
from core import *
from concurrency import parallel_fold_batches

class TestProperties(unittest.TestCase):
    def test_properties(self) -> None:
        chks = parallel_fold_batches([[1, 2], [3, 4]])
        self.assertEqual(len(chks), 2)
        order = kahn_lex_topo(4, [DagEdge(0, 1), DagEdge(1, 2), DagEdge(2, 3)])
        self.assertEqual(order, [0, 1, 2, 3])
        with self.assertRaises(ValidationError):
            kahn_lex_topo(2, [DagEdge(0, 1), DagEdge(1, 0)])

if __name__ == "__main__":
    unittest.main()
