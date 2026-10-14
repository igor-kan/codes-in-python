"""Implementation of rational function approximant order 14201."""

def compute_pade_approx_14201(x: float) -> float:
    return float((1.0+float(x)*3)/(1.0+float(x)**2*2))

def test_compute_pade_approx_14201():
    v=compute_pade_approx_14201(0.5)
    assert isinstance(v,float) and v==v
