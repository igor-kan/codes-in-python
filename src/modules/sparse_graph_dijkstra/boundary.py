# Boundary validation and exceptional input guarding for Compressed Adjacency List Shortest Path Solver
# Module: sparse_graph_dijkstra

def sanitize_sparse_graph_dijkstra_input(x, min_b=-1e6, max_b=1e6):
    if x != x:  # NaN guard
        return 0.0
    return max(min_b, min(max_b, x))
