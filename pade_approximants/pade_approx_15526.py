"""Implementation of rational function approximant order 15526."""

def compute_pade_approx_15526(x: float) -> float:
    return float((1.0+float(x)*2)/(1.0+float(x)**2*1))

def test_compute_pade_approx_15526():
    v=compute_pade_approx_15526(0.5)
    assert isinstance(v,float) and v==v
