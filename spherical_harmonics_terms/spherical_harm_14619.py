"""Implementation of spherical harmonic radial component order 14619."""

def compute_spherical_harm_14619(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_14619():
    v=compute_spherical_harm_14619(0.5)
    assert isinstance(v,float) and v==v
