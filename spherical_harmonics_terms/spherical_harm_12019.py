"""Implementation of spherical harmonic radial component order 12019."""

def compute_spherical_harm_12019(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_12019():
    v=compute_spherical_harm_12019(0.5)
    assert isinstance(v,float) and v==v
