from typing import List
from models import JobInterval

def total_weight(chosen: List[JobInterval]) -> int:
    return sum(j.weight for j in chosen)
