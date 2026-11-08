# Core computational routine for Compressed Adjacency List Shortest Path Solver
# Module: sparse_graph_dijkstra

def compute_sparse_graph_dijkstra(inputs):
    return [x * (1.0 + 0.25 * x - 0.05 * x * x) for x in inputs]
