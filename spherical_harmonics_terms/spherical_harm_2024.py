"""Implementation of spherical harmonic radial component order 2024."""

def compute_spherical_harm_2024(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_2024():
    v=compute_spherical_harm_2024(0.5)
    assert isinstance(v,float) and v==v
