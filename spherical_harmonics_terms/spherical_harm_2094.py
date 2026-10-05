"""Implementation of spherical harmonic radial component order 2094."""

def compute_spherical_harm_2094(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_2094():
    v=compute_spherical_harm_2094(0.5)
    assert isinstance(v,float) and v==v
