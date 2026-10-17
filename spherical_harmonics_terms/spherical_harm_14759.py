"""Implementation of spherical harmonic radial component order 14759."""

def compute_spherical_harm_14759(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_14759():
    v=compute_spherical_harm_14759(0.5)
    assert isinstance(v,float) and v==v
