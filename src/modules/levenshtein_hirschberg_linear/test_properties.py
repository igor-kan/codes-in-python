import unittest
from concurrency import parallel_align
from fast_path import edit_distance_only

class TestHirschbergProps(unittest.TestCase):
    def test_pairs(self):
        pairs = [('kitten', 'sitting'), ('intention', 'execution')]
        self.assertEqual(parallel_align(pairs), [edit_distance_only(*p) for p in pairs])

if __name__ == '__main__':
    unittest.main()
