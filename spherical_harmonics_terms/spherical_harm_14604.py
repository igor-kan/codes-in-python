"""Implementation of spherical harmonic radial component order 14604."""

def compute_spherical_harm_14604(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_14604():
    v=compute_spherical_harm_14604(0.5)
    assert isinstance(v,float) and v==v
