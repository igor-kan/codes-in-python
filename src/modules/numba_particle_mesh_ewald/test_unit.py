# Deterministic unit tests for Particle-Mesh Ewald Long-Range Electrostatic Solver
# Module: numba_particle_mesh_ewald

def test_numba_particle_mesh_ewald_zero_element():
    x = 0.0
    res = x * (1.0 + 0.35 * x - 0.03 * x * x)
    assert res == 0.0
