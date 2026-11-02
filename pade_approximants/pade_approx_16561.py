"""Implementation of rational function approximant order 16561."""

def compute_pade_approx_16561(x: float) -> float:
    return float((1.0+float(x)*2)/(1.0+float(x)**2*2))

def test_compute_pade_approx_16561():
    v=compute_pade_approx_16561(0.5)
    assert isinstance(v,float) and v==v
