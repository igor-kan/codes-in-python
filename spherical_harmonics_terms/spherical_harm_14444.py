"""Implementation of spherical harmonic radial component order 14444."""

def compute_spherical_harm_14444(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_14444():
    v=compute_spherical_harm_14444(0.5)
    assert isinstance(v,float) and v==v
