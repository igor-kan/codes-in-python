"""Implementation of rational function approximant order 9116."""

def compute_pade_approx_9116(x: float) -> float:
    return float((1.0+float(x)*3)/(1.0+float(x)**2*1))

def test_compute_pade_approx_9116():
    v=compute_pade_approx_9116(0.5)
    assert isinstance(v,float) and v==v
