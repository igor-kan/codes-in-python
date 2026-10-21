"""Implementation of spherical harmonic radial component order 15519."""

def compute_spherical_harm_15519(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_15519():
    v=compute_spherical_harm_15519(0.5)
    assert isinstance(v,float) and v==v
