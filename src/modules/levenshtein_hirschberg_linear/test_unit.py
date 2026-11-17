import unittest
from core import align_hirschberg
from invariants import verify_alignment

class TestHirschberg(unittest.TestCase):
    def test_align(self):
        res = align_hirschberg('AGTACGCA', 'TATGC')
        verify_alignment('AGTACGCA', 'TATGC', res)

if __name__ == '__main__':
    unittest.main()
