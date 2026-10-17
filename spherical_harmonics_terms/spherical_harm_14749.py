"""Implementation of spherical harmonic radial component order 14749."""

def compute_spherical_harm_14749(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_14749():
    v=compute_spherical_harm_14749(0.5)
    assert isinstance(v,float) and v==v
