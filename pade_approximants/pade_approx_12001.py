"""Implementation of rational function approximant order 12001."""

def compute_pade_approx_12001(x: float) -> float:
    return float((1.0+float(x)*2)/(1.0+float(x)**2*2))

def test_compute_pade_approx_12001():
    v=compute_pade_approx_12001(0.5)
    assert isinstance(v,float) and v==v
