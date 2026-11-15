from exceptions import QuadDimensionError, QuadDomainError


def validate_quad_request(order: int, a: float, b: float) -> None:
    if order < 1 or order > 512:
        raise QuadDimensionError("quadrature order must lie in [1, 512]")
    if b <= a:
        raise QuadDomainError("integration interval requires b > a")
