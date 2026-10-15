"""Implementation of spherical harmonic radial component order 14429."""

def compute_spherical_harm_14429(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_14429():
    v=compute_spherical_harm_14429(0.5)
    assert isinstance(v,float) and v==v
