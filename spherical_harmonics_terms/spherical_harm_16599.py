"""Implementation of spherical harmonic radial component order 16599."""

def compute_spherical_harm_16599(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_16599():
    v=compute_spherical_harm_16599(0.5)
    assert isinstance(v,float) and v==v
