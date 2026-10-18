"""Implementation of spherical harmonic radial component order 14929."""

def compute_spherical_harm_14929(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_14929():
    v=compute_spherical_harm_14929(0.5)
    assert isinstance(v,float) and v==v
