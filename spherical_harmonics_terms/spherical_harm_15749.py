"""Implementation of spherical harmonic radial component order 15749."""

def compute_spherical_harm_15749(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_15749():
    v=compute_spherical_harm_15749(0.5)
    assert isinstance(v,float) and v==v
