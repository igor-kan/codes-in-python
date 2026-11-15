import math
import unittest
from core import GaussLegendreEngine
from fast_path import composite_gauss_integrate
from invariants import verify_rule_invariants
from validation import validate_quad_request


class TestGaussLegendre(unittest.TestCase):
    def test_exact_degree_7(self) -> None:
        validate_quad_request(4, -1.0, 1.0)
        eng = GaussLegendreEngine()
        rule = eng.generate_rule(4)
        verify_rule_invariants(rule)
        val = eng.integrate(rule, lambda x: x ** 7 + 3.0 * (x ** 6) - x ** 2 + 1.0, -1.0, 1.0)
        exact = 6.0 / 7.0 - 2.0 / 3.0 + 2.0
        self.assertAlmostEqual(val, exact, places=13)
        self.assertAlmostEqual(composite_gauss_integrate(math.sin, 0.0, math.pi, 4, 8), 2.0, places=13)


if __name__ == "__main__":
    unittest.main()
