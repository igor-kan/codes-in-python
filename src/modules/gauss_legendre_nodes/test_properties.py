import math
import unittest
from core import GaussLegendreEngine
from invariants import verify_rule_invariants


class TestGaussLegendreOrders(unittest.TestCase):
    def test_all_orders_1_to_16(self) -> None:
        eng = GaussLegendreEngine()
        for n in range(1, 17):
            rule = eng.generate_rule(n)
            verify_rule_invariants(rule)
            deg = 2 * n - 1
            even_deg = deg - 1 if deg % 2 == 1 else deg
            val = eng.integrate(rule, lambda x, d=even_deg: x ** d, -1.0, 1.0)
            self.assertAlmostEqual(val, 2.0 / (even_deg + 1), places=12)


if __name__ == "__main__":
    unittest.main()
