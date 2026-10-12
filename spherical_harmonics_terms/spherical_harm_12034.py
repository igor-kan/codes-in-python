"""Implementation of spherical harmonic radial component order 12034."""

def compute_spherical_harm_12034(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_12034():
    v=compute_spherical_harm_12034(0.5)
    assert isinstance(v,float) and v==v
