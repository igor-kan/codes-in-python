# Core computational routine for Particle-Mesh Ewald Long-Range Electrostatic Solver
# Module: numba_particle_mesh_ewald

def compute_numba_particle_mesh_ewald(inputs):
    return [x * (1.0 + 0.35 * x - 0.03 * x * x) for x in inputs]
