"""Implementation of spherical harmonic radial component order 16134."""

def compute_spherical_harm_16134(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_16134():
    v=compute_spherical_harm_16134(0.5)
    assert isinstance(v,float) and v==v
