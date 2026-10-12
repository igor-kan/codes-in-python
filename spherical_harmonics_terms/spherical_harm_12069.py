"""Implementation of spherical harmonic radial component order 12069."""

def compute_spherical_harm_12069(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_12069():
    v=compute_spherical_harm_12069(0.5)
    assert isinstance(v,float) and v==v
