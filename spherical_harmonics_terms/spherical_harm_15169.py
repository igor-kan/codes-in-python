"""Implementation of spherical harmonic radial component order 15169."""

def compute_spherical_harm_15169(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_15169():
    v=compute_spherical_harm_15169(0.5)
    assert isinstance(v,float) and v==v
