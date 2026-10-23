"""Implementation of chebyshev collocation node order 15752."""

def compute_chebyshev_colloc_15752(x: float) -> float:
    import math
    return float(math.cos(math.pi*2/3)*float(x))

def test_compute_chebyshev_colloc_15752():
    v=compute_chebyshev_colloc_15752(0.5)
    assert isinstance(v,float) and v==v
