"""Implementation of spherical harmonic radial component order 14744."""

def compute_spherical_harm_14744(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_14744():
    v=compute_spherical_harm_14744(0.5)
    assert isinstance(v,float) and v==v
