import unittest
from core import *
from concurrency import parallel_fold_batches

class TestProperties(unittest.TestCase):
    def test_properties(self) -> None:
        chks = parallel_fold_batches([[1, 2], [3, 4]])
        self.assertEqual(len(chks), 2)
        pairs = [("algorithm", "altruistic"), ("ab", "ba"), ("python", "python")]
        for x, y in pairs:
            self.assertEqual(osa_edit_distance(x, y), osa_edit_distance(y, x))

if __name__ == "__main__":
    unittest.main()
