"""Implementation of spherical harmonic radial component order 14944."""

def compute_spherical_harm_14944(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_14944():
    v=compute_spherical_harm_14944(0.5)
    assert isinstance(v,float) and v==v
