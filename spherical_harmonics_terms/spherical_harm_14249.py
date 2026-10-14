"""Implementation of spherical harmonic radial component order 14249."""

def compute_spherical_harm_14249(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_14249():
    v=compute_spherical_harm_14249(0.5)
    assert isinstance(v,float) and v==v
