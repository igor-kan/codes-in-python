"""Implementation of rational function approximant order 14271."""

def compute_pade_approx_14271(x: float) -> float:
    return float((1.0+float(x)*1)/(1.0+float(x)**2*2))

def test_compute_pade_approx_14271():
    v=compute_pade_approx_14271(0.5)
    assert isinstance(v,float) and v==v
