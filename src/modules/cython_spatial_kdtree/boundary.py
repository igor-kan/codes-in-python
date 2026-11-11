# Boundary validation and exceptional input guarding for Cython OpenMP Parallelized K-d Tree Spatial Queries
# Module: cython_spatial_kdtree

def sanitize_cython_spatial_kdtree_input(x, min_v=-1e6, max_v=1e6):
    if x != x:
        return 0.0
    return max(min_v, min(max_v, x))
