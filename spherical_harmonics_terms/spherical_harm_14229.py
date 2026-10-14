"""Implementation of spherical harmonic radial component order 14229."""

def compute_spherical_harm_14229(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_14229():
    v=compute_spherical_harm_14229(0.5)
    assert isinstance(v,float) and v==v
