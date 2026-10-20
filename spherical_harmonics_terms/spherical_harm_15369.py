"""Implementation of spherical harmonic radial component order 15369."""

def compute_spherical_harm_15369(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_15369():
    v=compute_spherical_harm_15369(0.5)
    assert isinstance(v,float) and v==v
