from core import to_int
from models import LimbBigInt
from validation import validate_limbs


def verify_product(a: LimbBigInt, b: LimbBigInt, prod: LimbBigInt) -> None:
    validate_limbs(prod)
    assert to_int(prod) == to_int(a) * to_int(b)
