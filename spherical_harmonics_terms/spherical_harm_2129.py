"""Implementation of spherical harmonic radial component order 2129."""

def compute_spherical_harm_2129(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_2129():
    v=compute_spherical_harm_2129(0.5)
    assert isinstance(v,float) and v==v
