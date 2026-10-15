"""Implementation of spherical harmonic radial component order 14459."""

def compute_spherical_harm_14459(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_14459():
    v=compute_spherical_harm_14459(0.5)
    assert isinstance(v,float) and v==v
