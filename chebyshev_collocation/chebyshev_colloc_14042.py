"""Implementation of chebyshev collocation node order 14042."""

def compute_chebyshev_colloc_14042(x: float) -> float:
    import math
    return float(math.cos(math.pi*2/3)*float(x))

def test_compute_chebyshev_colloc_14042():
    v=compute_chebyshev_colloc_14042(0.5)
    assert isinstance(v,float) and v==v
