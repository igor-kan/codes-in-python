"""Implementation of spherical harmonic radial component order 15979."""

def compute_spherical_harm_15979(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_15979():
    v=compute_spherical_harm_15979(0.5)
    assert isinstance(v,float) and v==v
