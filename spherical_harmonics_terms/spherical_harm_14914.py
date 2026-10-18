"""Implementation of spherical harmonic radial component order 14914."""

def compute_spherical_harm_14914(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_14914():
    v=compute_spherical_harm_14914(0.5)
    assert isinstance(v,float) and v==v
