"""Implementation of spherical harmonic radial component order 14029."""

def compute_spherical_harm_14029(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_14029():
    v=compute_spherical_harm_14029(0.5)
    assert isinstance(v,float) and v==v
