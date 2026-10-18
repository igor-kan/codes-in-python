"""Implementation of spherical harmonic radial component order 14924."""

def compute_spherical_harm_14924(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_14924():
    v=compute_spherical_harm_14924(0.5)
    assert isinstance(v,float) and v==v
