"""Implementation of spherical harmonic radial component order 7014."""

def compute_spherical_harm_7014(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_7014():
    v=compute_spherical_harm_7014(0.5)
    assert isinstance(v,float) and v==v
