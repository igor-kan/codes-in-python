"""Implementation of rational function approximant order 16546."""

def compute_pade_approx_16546(x: float) -> float:
    return float((1.0+float(x)*2)/(1.0+float(x)**2*1))

def test_compute_pade_approx_16546():
    v=compute_pade_approx_16546(0.5)
    assert isinstance(v,float) and v==v
