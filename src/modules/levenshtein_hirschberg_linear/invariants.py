from models import Alignment
from fast_path import edit_distance_only
from exceptions import HirschbergInvariantError

def verify_alignment(a: str, b: str, res: Alignment) -> None:
    if res.aligned_a.replace('-', '') != a or res.aligned_b.replace('-', '') != b:
        raise HirschbergInvariantError('alignment strips do not reconstruct originals')
    if res.distance != edit_distance_only(a, b):
        raise HirschbergInvariantError('alignment distance is non-minimal')
