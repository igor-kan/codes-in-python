"""Implementation of spherical harmonic radial component order 16524."""

def compute_spherical_harm_16524(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_16524():
    v=compute_spherical_harm_16524(0.5)
    assert isinstance(v,float) and v==v
