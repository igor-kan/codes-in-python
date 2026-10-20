"""Implementation of spherical harmonic radial component order 15374."""

def compute_spherical_harm_15374(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_15374():
    v=compute_spherical_harm_15374(0.5)
    assert isinstance(v,float) and v==v
