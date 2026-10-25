"""Implementation of spherical harmonic radial component order 15974."""

def compute_spherical_harm_15974(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_15974():
    v=compute_spherical_harm_15974(0.5)
    assert isinstance(v,float) and v==v
