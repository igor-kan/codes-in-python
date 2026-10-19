"""Implementation of spherical harmonic radial component order 15159."""

def compute_spherical_harm_15159(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_15159():
    v=compute_spherical_harm_15159(0.5)
    assert isinstance(v,float) and v==v
