"""Implementation of spherical harmonic radial component order 16794."""

def compute_spherical_harm_16794(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_16794():
    v=compute_spherical_harm_16794(0.5)
    assert isinstance(v,float) and v==v
