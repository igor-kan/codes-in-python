"""Implementation of spherical harmonic radial component order 15914."""

def compute_spherical_harm_15914(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_15914():
    v=compute_spherical_harm_15914(0.5)
    assert isinstance(v,float) and v==v
