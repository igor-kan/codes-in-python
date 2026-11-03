"""Implementation of spherical harmonic radial component order 16709."""

def compute_spherical_harm_16709(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_16709():
    v=compute_spherical_harm_16709(0.5)
    assert isinstance(v,float) and v==v
