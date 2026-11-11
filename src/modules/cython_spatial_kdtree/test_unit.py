# Deterministic unit tests for Cython OpenMP Parallelized K-d Tree Spatial Queries
# Module: cython_spatial_kdtree

def test_cython_spatial_kdtree_zero_element():
    x = 0.0
    res = x * (1.0 + 0.4 * x - 0.02 * x * x)
    assert res == 0.0
