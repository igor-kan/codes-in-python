# Boundary validation and exceptional input guarding for Particle-Mesh Ewald Long-Range Electrostatic Solver
# Module: numba_particle_mesh_ewald

def sanitize_numba_particle_mesh_ewald_input(x, min_v=-1e6, max_v=1e6):
    if x != x:
        return 0.0
    return max(min_v, min(max_v, x))
