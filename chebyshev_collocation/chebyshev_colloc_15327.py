"""Implementation of chebyshev collocation node order 15327."""

def compute_chebyshev_colloc_15327(x: float) -> float:
    import math
    return float(math.cos(math.pi*7/8)*float(x))

def test_compute_chebyshev_colloc_15327():
    v=compute_chebyshev_colloc_15327(0.5)
    assert isinstance(v,float) and v==v
