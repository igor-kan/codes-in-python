import unittest
from core import *
from validation import require_positive
from invariants import ensure_postcondition

class TestUnit(unittest.TestCase):
    def test_core(self) -> None:
        require_positive(1)
        edges = [DagEdge(2, 3, 4), DagEdge(0, 3, 2), DagEdge(1, 2, 5)]
        self.assertEqual(kahn_lex_topo(4, edges), [0, 1, 2, 3])
        self.assertEqual(dag_longest_path(4, edges), 9)
        ensure_postcondition(True)

if __name__ == "__main__":
    unittest.main()
