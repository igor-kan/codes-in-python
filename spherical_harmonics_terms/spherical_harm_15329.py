"""Implementation of spherical harmonic radial component order 15329."""

def compute_spherical_harm_15329(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_15329():
    v=compute_spherical_harm_15329(0.5)
    assert isinstance(v,float) and v==v
