from typing import List
from models import JobInterval
from exceptions import IntervalDpValidationError

def validate_jobs(jobs: List[JobInterval]) -> None:
    if any(j.start >= j.end for j in jobs):
        raise IntervalDpValidationError('start must be < end')
