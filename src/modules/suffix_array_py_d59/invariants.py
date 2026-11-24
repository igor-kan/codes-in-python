from exceptions import InvariantError

def ensure_postcondition(ok: bool, msg: str = "invariant failed") -> None:
    if not ok:
        raise InvariantError(msg)
