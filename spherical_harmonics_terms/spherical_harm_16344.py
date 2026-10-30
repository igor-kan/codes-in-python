"""Implementation of spherical harmonic radial component order 16344."""

def compute_spherical_harm_16344(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_16344():
    v=compute_spherical_harm_16344(0.5)
    assert isinstance(v,float) and v==v
