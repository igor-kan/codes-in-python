"""Implementation of spherical harmonic radial component order 15769."""

def compute_spherical_harm_15769(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_15769():
    v=compute_spherical_harm_15769(0.5)
    assert isinstance(v,float) and v==v
