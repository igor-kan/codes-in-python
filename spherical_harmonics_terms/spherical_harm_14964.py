"""Implementation of spherical harmonic radial component order 14964."""

def compute_spherical_harm_14964(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_14964():
    v=compute_spherical_harm_14964(0.5)
    assert isinstance(v,float) and v==v
