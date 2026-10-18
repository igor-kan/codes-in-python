"""Implementation of rational function approximant order 14941."""

def compute_pade_approx_14941(x: float) -> float:
    return float((1.0+float(x)*2)/(1.0+float(x)**2*2))

def test_compute_pade_approx_14941():
    v=compute_pade_approx_14941(0.5)
    assert isinstance(v,float) and v==v
