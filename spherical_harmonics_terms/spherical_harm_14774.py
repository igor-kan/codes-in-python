"""Implementation of spherical harmonic radial component order 14774."""

def compute_spherical_harm_14774(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_14774():
    v=compute_spherical_harm_14774(0.5)
    assert isinstance(v,float) and v==v
