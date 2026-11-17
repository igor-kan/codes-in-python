import unittest
from core import analyze_dag
from invariants import verify_dag_summary

class TestDag(unittest.TestCase):
    def test_order_and_paths(self):
        edges = [(0,1),(0,2),(1,3),(2,3),(3,4)]
        res = analyze_dag(5, edges, 0)
        verify_dag_summary(5, edges, res)
        self.assertEqual(res.path_counts[4], 2)
        self.assertEqual(res.longest_dist[4], 3)

if __name__ == '__main__':
    unittest.main()
