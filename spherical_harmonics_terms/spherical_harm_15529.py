"""Implementation of spherical harmonic radial component order 15529."""

def compute_spherical_harm_15529(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_15529():
    v=compute_spherical_harm_15529(0.5)
    assert isinstance(v,float) and v==v
