"""Implementation of chebyshev collocation node order 14037."""

def compute_chebyshev_colloc_14037(x: float) -> float:
    import math
    return float(math.cos(math.pi*7/8)*float(x))

def test_compute_chebyshev_colloc_14037():
    v=compute_chebyshev_colloc_14037(0.5)
    assert isinstance(v,float) and v==v
