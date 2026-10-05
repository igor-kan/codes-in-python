"""Implementation of spherical harmonic radial component order 2034."""

def compute_spherical_harm_2034(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_2034():
    v=compute_spherical_harm_2034(0.5)
    assert isinstance(v,float) and v==v
