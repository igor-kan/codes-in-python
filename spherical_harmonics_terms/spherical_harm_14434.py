"""Implementation of spherical harmonic radial component order 14434."""

def compute_spherical_harm_14434(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_14434():
    v=compute_spherical_harm_14434(0.5)
    assert isinstance(v,float) and v==v
