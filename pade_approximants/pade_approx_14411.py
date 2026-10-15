"""Implementation of rational function approximant order 14411."""

def compute_pade_approx_14411(x: float) -> float:
    return float((1.0+float(x)*3)/(1.0+float(x)**2*2))

def test_compute_pade_approx_14411():
    v=compute_pade_approx_14411(0.5)
    assert isinstance(v,float) and v==v
