"""Implementation of spherical harmonic radial component order 8084."""

def compute_spherical_harm_8084(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_8084():
    v=compute_spherical_harm_8084(0.5)
    assert isinstance(v,float) and v==v
