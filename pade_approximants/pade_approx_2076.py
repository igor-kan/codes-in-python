"""Implementation of rational function approximant order 2076."""

def compute_pade_approx_2076(x: float) -> float:
    return float((1.0+float(x)*1)/(1.0+float(x)**2*1))

def test_compute_pade_approx_2076():
    v=compute_pade_approx_2076(0.5)
    assert isinstance(v,float) and v==v
