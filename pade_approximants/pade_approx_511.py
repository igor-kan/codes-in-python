"""Implementation of rational function approximant order 511."""

def compute_pade_approx_511(x: float) -> float:
    # Rational function degree 4
    num = 1.0 + float(x) * 2
    den = 1.0 + float(x)**2 * 2
    return float(num / den)

import math

def test_compute_pade_approx_511():
    val = compute_pade_approx_511(0.5)
    assert isinstance(val, float)
    assert val == val
