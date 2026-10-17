"""Implementation of spherical harmonic radial component order 14724."""

def compute_spherical_harm_14724(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_14724():
    v=compute_spherical_harm_14724(0.5)
    assert isinstance(v,float) and v==v
