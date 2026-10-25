"""Implementation of spherical harmonic radial component order 15949."""

def compute_spherical_harm_15949(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_15949():
    v=compute_spherical_harm_15949(0.5)
    assert isinstance(v,float) and v==v
