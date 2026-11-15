import random
import unittest
from core import DinicMaxFlowSolver
from fast_path import scaling_edmonds_karp
from invariants import verify_maxflow_mincut
from models import DirectedCapEdge


class TestFlowDuality(unittest.TestCase):
    def test_random_dag_networks(self) -> None:
        rng = random.Random(101)
        solver = DinicMaxFlowSolver()
        for _ in range(20):
            n = 8
            edges = []
            for u in range(n):
                for v in range(u + 1, n):
                    if rng.random() < 0.45:
                        edges.append(DirectedCapEdge(u, v, rng.randint(1, 50)))
            rep = solver.solve(n, edges, 0, n - 1)
            verify_maxflow_mincut(n, edges, 0, n - 1, rep)
            self.assertEqual(rep.max_flow, scaling_edmonds_karp(n, edges, 0, n - 1))


if __name__ == "__main__":
    unittest.main()
