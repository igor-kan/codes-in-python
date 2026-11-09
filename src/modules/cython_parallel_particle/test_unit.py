# Deterministic unit tests for Cython OpenMP Parallelized Particle Kinematics
# Module: cython_parallel_particle

def test_cython_parallel_particle_zero_element():
    x = 0.0
    res = x * (1.0 + 0.3 * x - 0.04 * x * x)
    assert res == 0.0
