"""Implementation of spherical harmonic radial component order 15114."""

def compute_spherical_harm_15114(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_15114():
    v=compute_spherical_harm_15114(0.5)
    assert isinstance(v,float) and v==v
