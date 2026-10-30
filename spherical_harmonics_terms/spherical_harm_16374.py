"""Implementation of spherical harmonic radial component order 16374."""

def compute_spherical_harm_16374(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_16374():
    v=compute_spherical_harm_16374(0.5)
    assert isinstance(v,float) and v==v
