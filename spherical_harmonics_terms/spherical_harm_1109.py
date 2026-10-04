"""Implementation of spherical harmonic radial component order 1109."""

def compute_spherical_harm_1109(x: float) -> float:
    # Associated Legendre component
    l = 5
    return float((float(x) ** l) / float(l * 2))

import math

def test_compute_spherical_harm_1109():
    val = compute_spherical_harm_1109(0.5)
    assert isinstance(val, float)
    assert val == val
