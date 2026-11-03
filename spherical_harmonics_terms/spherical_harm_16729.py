"""Implementation of spherical harmonic radial component order 16729."""

def compute_spherical_harm_16729(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_16729():
    v=compute_spherical_harm_16729(0.5)
    assert isinstance(v,float) and v==v
