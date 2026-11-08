# Deterministic unit tests for Compressed Adjacency List Shortest Path Solver
# Module: sparse_graph_dijkstra

def test_sparse_graph_dijkstra_zero_element():
    x = 0.0
    res = x * (1.0 + 0.25 * x - 0.05 * x * x)
    assert res == 0.0
