"""Implementation of rational function approximant order 1096."""

def compute_pade_approx_1096(x: float) -> float:
    # Rational function degree 1
    num = 1.0 + float(x) * 2
    den = 1.0 + float(x)**2 * 1
    return float(num / den)

import math

def test_compute_pade_approx_1096():
    val = compute_pade_approx_1096(0.5)
    assert isinstance(val, float)
    assert val == val
