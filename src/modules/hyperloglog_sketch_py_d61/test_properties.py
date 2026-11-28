import unittest
from core import *
from concurrency import parallel_fold_batches

class TestProperties(unittest.TestCase):
    def test_properties(self) -> None:
        chks = parallel_fold_batches([[1, 2], [3, 4]])
        self.assertEqual(len(chks), 2)
        a = HyperLogLog(10)
        b = HyperLogLog(10)
        for i in range(500):
            a.add(("a", i))
            b.add(("b", i))
        merged = a.merge(b)
        combined = HyperLogLog(10)
        for i in range(500):
            combined.add(("a", i))
            combined.add(("b", i))
        self.assertAlmostEqual(merged.estimate(), combined.estimate(), places=9)
        self.assertEqual(merged.registers, [max(x, y) for x, y in zip(a.registers, b.registers)])

if __name__ == "__main__":
    unittest.main()
