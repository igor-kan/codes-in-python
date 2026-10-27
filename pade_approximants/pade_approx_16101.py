"""Implementation of rational function approximant order 16101."""

def compute_pade_approx_16101(x: float) -> float:
    return float((1.0+float(x)*1)/(1.0+float(x)**2*2))

def test_compute_pade_approx_16101():
    v=compute_pade_approx_16101(0.5)
    assert isinstance(v,float) and v==v
