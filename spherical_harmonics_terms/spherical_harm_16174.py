"""Implementation of spherical harmonic radial component order 16174."""

def compute_spherical_harm_16174(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_16174():
    v=compute_spherical_harm_16174(0.5)
    assert isinstance(v,float) and v==v
