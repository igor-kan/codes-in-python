from typing import List, Protocol
from models import JobInterval

class SchedulePlanner(Protocol):
    def max_schedule(self, jobs: List[JobInterval]) -> int: ...
