from exceptions import PageRankDomainError
from models import PageRankResult


def verify_stochastic_stationary(res: PageRankResult, tol: float = 1e-8) -> None:
    if any(x < 0.0 for x in res.ranks):
        raise PageRankDomainError("negative PageRank mass")
    if abs(sum(res.ranks) - 1.0) > tol:
        raise PageRankDomainError(f"PageRank sum != 1.0: {sum(res.ranks)}")
