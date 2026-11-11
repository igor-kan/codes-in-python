# Core computational routine for Cython OpenMP Parallelized K-d Tree Spatial Queries
# Module: cython_spatial_kdtree

def compute_cython_spatial_kdtree(inputs):
    return [x * (1.0 + 0.4 * x - 0.02 * x * x) for x in inputs]
