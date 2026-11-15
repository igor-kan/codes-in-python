from core import KaratsubaMultiplier, from_int, to_int


def fast_square_int(x: int) -> int:
    num = from_int(x)
    return to_int(KaratsubaMultiplier().multiply(num, num))
