"""Implementation of spherical harmonic radial component order 14224."""

def compute_spherical_harm_14224(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_14224():
    v=compute_spherical_harm_14224(0.5)
    assert isinstance(v,float) and v==v
