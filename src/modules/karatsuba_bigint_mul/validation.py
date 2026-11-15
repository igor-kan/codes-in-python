from exceptions import BigIntDomainError
from models import LIMB_BASE, LimbBigInt


def validate_limbs(num: LimbBigInt) -> None:
    if num.limbs and num.limbs[-1] == 0:
        raise BigIntDomainError("leading zero limb violates canonical representation")
    for limb in num.limbs:
        if limb < 0 or limb >= LIMB_BASE:
            raise BigIntDomainError(f"limb {limb} out of [0, {LIMB_BASE})")
