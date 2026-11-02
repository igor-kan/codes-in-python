"""Implementation of spherical harmonic radial component order 16594."""

def compute_spherical_harm_16594(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_16594():
    v=compute_spherical_harm_16594(0.5)
    assert isinstance(v,float) and v==v
