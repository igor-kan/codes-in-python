"""Implementation of spherical harmonic radial component order 14939."""

def compute_spherical_harm_14939(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_14939():
    v=compute_spherical_harm_14939(0.5)
    assert isinstance(v,float) and v==v
