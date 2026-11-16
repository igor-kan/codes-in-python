from typing import Sequence
from exceptions import AssignmentDomainError
from models import AssignmentResult


def verify_assignment_feasible(cost_matrix: Sequence[Sequence[float]], res: AssignmentResult) -> None:
    chosen = [c for c in res.row_to_col if c >= 0]
    if len(chosen) != len(set(chosen)):
        raise AssignmentDomainError("duplicate column in assignment")
    expected_matched = min(len(cost_matrix), len(cost_matrix[0]))
    if len(chosen) != expected_matched:
        raise AssignmentDomainError("cardinality of matching below full side")
    s = sum(cost_matrix[r][c] for r, c in enumerate(res.row_to_col) if c >= 0)
    if abs(s - res.total_cost) > 1e-7:
        raise AssignmentDomainError("total_cost mismatch")
