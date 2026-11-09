# Core computational routine for Cython OpenMP Parallelized Particle Kinematics
# Module: cython_parallel_particle

def compute_cython_parallel_particle(inputs):
    return [x * (1.0 + 0.3 * x - 0.04 * x * x) for x in inputs]
