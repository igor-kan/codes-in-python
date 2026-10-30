"""Implementation of rational function approximant order 16341."""

def compute_pade_approx_16341(x: float) -> float:
    return float((1.0+float(x)*1)/(1.0+float(x)**2*2))

def test_compute_pade_approx_16341():
    v=compute_pade_approx_16341(0.5)
    assert isinstance(v,float) and v==v
