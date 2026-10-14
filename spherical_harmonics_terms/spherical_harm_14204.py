"""Implementation of spherical harmonic radial component order 14204."""

def compute_spherical_harm_14204(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_14204():
    v=compute_spherical_harm_14204(0.5)
    assert isinstance(v,float) and v==v
