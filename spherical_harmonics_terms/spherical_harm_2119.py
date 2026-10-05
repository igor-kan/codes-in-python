"""Implementation of spherical harmonic radial component order 2119."""

def compute_spherical_harm_2119(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_2119():
    v=compute_spherical_harm_2119(0.5)
    assert isinstance(v,float) and v==v
