import unittest
from concurrency import parallel_batch_analyze

class TestDagProps(unittest.TestCase):
    def test_parallel_batch(self):
        jobs = [(4, [(0,1),(0,2),(1,3),(2,3)], 0), (3, [(0,1),(1,2)], 0)]
        self.assertEqual(parallel_batch_analyze(jobs), [2, 1])

if __name__ == '__main__':
    unittest.main()
