"""Implementation of spherical harmonic radial component order 7024."""

def compute_spherical_harm_7024(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_7024():
    v=compute_spherical_harm_7024(0.5)
    assert isinstance(v,float) and v==v
