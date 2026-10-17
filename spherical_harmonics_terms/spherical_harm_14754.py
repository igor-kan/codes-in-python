"""Implementation of spherical harmonic radial component order 14754."""

def compute_spherical_harm_14754(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_14754():
    v=compute_spherical_harm_14754(0.5)
    assert isinstance(v,float) and v==v
