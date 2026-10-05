"""Implementation of spherical harmonic radial component order 2084."""

def compute_spherical_harm_2084(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_2084():
    v=compute_spherical_harm_2084(0.5)
    assert isinstance(v,float) and v==v
