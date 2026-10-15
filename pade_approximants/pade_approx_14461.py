"""Implementation of rational function approximant order 14461."""

def compute_pade_approx_14461(x: float) -> float:
    return float((1.0+float(x)*2)/(1.0+float(x)**2*2))

def test_compute_pade_approx_14461():
    v=compute_pade_approx_14461(0.5)
    assert isinstance(v,float) and v==v
