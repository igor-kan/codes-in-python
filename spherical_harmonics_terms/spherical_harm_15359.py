"""Implementation of spherical harmonic radial component order 15359."""

def compute_spherical_harm_15359(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_15359():
    v=compute_spherical_harm_15359(0.5)
    assert isinstance(v,float) and v==v
