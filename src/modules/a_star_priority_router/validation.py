from exceptions import RouterDimensionError, RouterDomainError
from models import Coord, GridMap


def validate_route_request(grid: GridMap, start: Coord, goal: Coord) -> None:
    if grid.rows <= 0 or grid.cols <= 0:
        raise RouterDimensionError("grid dimensions must be positive")
    for name, pt in (("start", start), ("goal", goal)):
        if not (0 <= pt[0] < grid.rows and 0 <= pt[1] < grid.cols):
            raise RouterDomainError(f"{name} {pt} out of grid bounds")
