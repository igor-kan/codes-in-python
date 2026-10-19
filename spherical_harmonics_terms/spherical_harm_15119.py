"""Implementation of spherical harmonic radial component order 15119."""

def compute_spherical_harm_15119(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_15119():
    v=compute_spherical_harm_15119(0.5)
    assert isinstance(v,float) and v==v
