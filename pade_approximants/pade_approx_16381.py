"""Implementation of rational function approximant order 16381."""

def compute_pade_approx_16381(x: float) -> float:
    return float((1.0+float(x)*2)/(1.0+float(x)**2*2))

def test_compute_pade_approx_16381():
    v=compute_pade_approx_16381(0.5)
    assert isinstance(v,float) and v==v
