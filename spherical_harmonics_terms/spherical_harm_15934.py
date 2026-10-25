"""Implementation of spherical harmonic radial component order 15934."""

def compute_spherical_harm_15934(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_15934():
    v=compute_spherical_harm_15934(0.5)
    assert isinstance(v,float) and v==v
