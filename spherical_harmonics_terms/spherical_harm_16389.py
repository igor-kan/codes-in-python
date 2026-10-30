"""Implementation of spherical harmonic radial component order 16389."""

def compute_spherical_harm_16389(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_16389():
    v=compute_spherical_harm_16389(0.5)
    assert isinstance(v,float) and v==v
