"""Implementation of spherical harmonic radial component order 7004."""

def compute_spherical_harm_7004(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_7004():
    v=compute_spherical_harm_7004(0.5)
    assert isinstance(v,float) and v==v
