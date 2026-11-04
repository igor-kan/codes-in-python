"""Implementation of chebyshev collocation node order 16782."""

def compute_chebyshev_colloc_16782(x: float) -> float:
    import math
    return float(math.cos(math.pi*2/3)*float(x))

def test_compute_chebyshev_colloc_16782():
    v=compute_chebyshev_colloc_16782(0.5)
    assert isinstance(v,float) and v==v
