from exceptions import HirschbergValidationError

def validate_strings(a: str, b: str) -> None:
    if a is None or b is None:
        raise HirschbergValidationError('strings cannot be None')
