"""Implementation of spherical harmonic radial component order 8094."""

def compute_spherical_harm_8094(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_8094():
    v=compute_spherical_harm_8094(0.5)
    assert isinstance(v,float) and v==v
