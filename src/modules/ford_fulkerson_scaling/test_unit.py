import unittest
from core import DinicMaxFlowSolver
from fast_path import scaling_edmonds_karp
from invariants import verify_maxflow_mincut
from models import DirectedCapEdge
from validation import validate_flow_network


class TestDinicFlow(unittest.TestCase):
    def test_clrs_flow_network(self) -> None:
        edges = [
            DirectedCapEdge(0, 1, 16), DirectedCapEdge(0, 2, 13),
            DirectedCapEdge(1, 2, 10), DirectedCapEdge(2, 1, 4),
            DirectedCapEdge(1, 3, 12), DirectedCapEdge(2, 4, 14),
            DirectedCapEdge(3, 2, 9), DirectedCapEdge(4, 3, 7),
            DirectedCapEdge(3, 5, 20), DirectedCapEdge(4, 5, 4),
        ]
        validate_flow_network(6, edges, 0, 5)
        rep = DinicMaxFlowSolver().solve(6, edges, 0, 5)
        self.assertEqual(rep.max_flow, 23)
        self.assertEqual(scaling_edmonds_karp(6, edges, 0, 5), 23)
        verify_maxflow_mincut(6, edges, 0, 5, rep)


if __name__ == "__main__":
    unittest.main()
