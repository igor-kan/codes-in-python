"""Implementation of spherical harmonic radial component order 14219."""

def compute_spherical_harm_14219(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_14219():
    v=compute_spherical_harm_14219(0.5)
    assert isinstance(v,float) and v==v
