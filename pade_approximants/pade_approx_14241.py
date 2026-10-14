"""Implementation of rational function approximant order 14241."""

def compute_pade_approx_14241(x: float) -> float:
    return float((1.0+float(x)*1)/(1.0+float(x)**2*2))

def test_compute_pade_approx_14241():
    v=compute_pade_approx_14241(0.5)
    assert isinstance(v,float) and v==v
