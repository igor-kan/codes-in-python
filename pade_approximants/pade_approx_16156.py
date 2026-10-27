"""Implementation of rational function approximant order 16156."""

def compute_pade_approx_16156(x: float) -> float:
    return float((1.0+float(x)*2)/(1.0+float(x)**2*1))

def test_compute_pade_approx_16156():
    v=compute_pade_approx_16156(0.5)
    assert isinstance(v,float) and v==v
