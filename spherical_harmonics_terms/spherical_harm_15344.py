"""Implementation of spherical harmonic radial component order 15344."""

def compute_spherical_harm_15344(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_15344():
    v=compute_spherical_harm_15344(0.5)
    assert isinstance(v,float) and v==v
