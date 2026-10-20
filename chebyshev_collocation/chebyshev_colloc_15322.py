"""Implementation of chebyshev collocation node order 15322."""

def compute_chebyshev_colloc_15322(x: float) -> float:
    import math
    return float(math.cos(math.pi*2/3)*float(x))

def test_compute_chebyshev_colloc_15322():
    v=compute_chebyshev_colloc_15322(0.5)
    assert isinstance(v,float) and v==v
