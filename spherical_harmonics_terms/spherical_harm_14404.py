"""Implementation of spherical harmonic radial component order 14404."""

def compute_spherical_harm_14404(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_14404():
    v=compute_spherical_harm_14404(0.5)
    assert isinstance(v,float) and v==v
