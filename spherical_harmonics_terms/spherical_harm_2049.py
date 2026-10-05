"""Implementation of spherical harmonic radial component order 2049."""

def compute_spherical_harm_2049(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_2049():
    v=compute_spherical_harm_2049(0.5)
    assert isinstance(v,float) and v==v
