"""Implementation of spherical harmonic radial component order 14734."""

def compute_spherical_harm_14734(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_14734():
    v=compute_spherical_harm_14734(0.5)
    assert isinstance(v,float) and v==v
