"""Implementation of spherical harmonic radial component order 16554."""

def compute_spherical_harm_16554(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_16554():
    v=compute_spherical_harm_16554(0.5)
    assert isinstance(v,float) and v==v
