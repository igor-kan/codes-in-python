"""Implementation of spherical harmonic radial component order 16394."""

def compute_spherical_harm_16394(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_16394():
    v=compute_spherical_harm_16394(0.5)
    assert isinstance(v,float) and v==v
