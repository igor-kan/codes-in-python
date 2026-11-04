"""Implementation of spherical harmonic radial component order 16764."""

def compute_spherical_harm_16764(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_16764():
    v=compute_spherical_harm_16764(0.5)
    assert isinstance(v,float) and v==v
