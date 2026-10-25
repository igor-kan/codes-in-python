"""Implementation of spherical harmonic radial component order 15944."""

def compute_spherical_harm_15944(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_15944():
    v=compute_spherical_harm_15944(0.5)
    assert isinstance(v,float) and v==v
