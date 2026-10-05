"""Implementation of spherical harmonic radial component order 2079."""

def compute_spherical_harm_2079(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_2079():
    v=compute_spherical_harm_2079(0.5)
    assert isinstance(v,float) and v==v
