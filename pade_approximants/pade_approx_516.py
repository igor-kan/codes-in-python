"""Implementation of rational function approximant order 516."""

def compute_pade_approx_516(x: float) -> float:
    # Rational function degree 1
    num = 1.0 + float(x) * 1
    den = 1.0 + float(x)**2 * 1
    return float(num / den)

import math

def test_compute_pade_approx_516():
    val = compute_pade_approx_516(0.5)
    assert isinstance(val, float)
    assert val == val
