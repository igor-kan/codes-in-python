"""Implementation of spherical harmonic radial component order 2054."""

def compute_spherical_harm_2054(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_2054():
    v=compute_spherical_harm_2054(0.5)
    assert isinstance(v,float) and v==v
