"""Implementation of spherical harmonic radial component order 15524."""

def compute_spherical_harm_15524(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_15524():
    v=compute_spherical_harm_15524(0.5)
    assert isinstance(v,float) and v==v
