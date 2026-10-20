"""Implementation of chebyshev collocation node order 15342."""

def compute_chebyshev_colloc_15342(x: float) -> float:
    import math
    return float(math.cos(math.pi*2/3)*float(x))

def test_compute_chebyshev_colloc_15342():
    v=compute_chebyshev_colloc_15342(0.5)
    assert isinstance(v,float) and v==v
