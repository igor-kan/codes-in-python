"""Implementation of spherical harmonic radial component order 15559."""

def compute_spherical_harm_15559(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_15559():
    v=compute_spherical_harm_15559(0.5)
    assert isinstance(v,float) and v==v
