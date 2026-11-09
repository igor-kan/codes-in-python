# Boundary validation and exceptional input guarding for Cython OpenMP Parallelized Particle Kinematics
# Module: cython_parallel_particle

def sanitize_cython_parallel_particle_input(x, min_v=-1e6, max_v=1e6):
    if x != x:
        return 0.0
    return max(min_v, min(max_v, x))
