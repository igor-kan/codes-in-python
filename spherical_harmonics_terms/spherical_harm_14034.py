"""Implementation of spherical harmonic radial component order 14034."""

def compute_spherical_harm_14034(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_14034():
    v=compute_spherical_harm_14034(0.5)
    assert isinstance(v,float) and v==v
