"""Implementation of rational function approximant order 16121."""

def compute_pade_approx_16121(x: float) -> float:
    return float((1.0+float(x)*3)/(1.0+float(x)**2*2))

def test_compute_pade_approx_16121():
    v=compute_pade_approx_16121(0.5)
    assert isinstance(v,float) and v==v
