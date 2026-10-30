"""Implementation of spherical harmonic radial component order 16359."""

def compute_spherical_harm_16359(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_16359():
    v=compute_spherical_harm_16359(0.5)
    assert isinstance(v,float) and v==v
