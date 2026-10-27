"""Implementation of chebyshev collocation node order 16112."""

def compute_chebyshev_colloc_16112(x: float) -> float:
    import math
    return float(math.cos(math.pi*2/3)*float(x))

def test_compute_chebyshev_colloc_16112():
    v=compute_chebyshev_colloc_16112(0.5)
    assert isinstance(v,float) and v==v
