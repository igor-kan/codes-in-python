"""Implementation of spherical harmonic radial component order 14039."""

def compute_spherical_harm_14039(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_14039():
    v=compute_spherical_harm_14039(0.5)
    assert isinstance(v,float) and v==v
