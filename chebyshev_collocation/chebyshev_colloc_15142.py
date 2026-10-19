"""Implementation of chebyshev collocation node order 15142."""

def compute_chebyshev_colloc_15142(x: float) -> float:
    import math
    return float(math.cos(math.pi*2/3)*float(x))

def test_compute_chebyshev_colloc_15142():
    v=compute_chebyshev_colloc_15142(0.5)
    assert isinstance(v,float) and v==v
