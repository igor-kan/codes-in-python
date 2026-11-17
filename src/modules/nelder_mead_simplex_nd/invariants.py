from models import SimplexResult
from exceptions import NelderMeadInvariantError

def verify_converged(res: SimplexResult, ceiling: float) -> None:
    if res.fval > ceiling:
        raise NelderMeadInvariantError(f'did not reach minimum: {res.fval}')
