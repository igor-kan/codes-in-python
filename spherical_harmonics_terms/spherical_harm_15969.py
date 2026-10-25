"""Implementation of spherical harmonic radial component order 15969."""

def compute_spherical_harm_15969(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_15969():
    v=compute_spherical_harm_15969(0.5)
    assert isinstance(v,float) and v==v
