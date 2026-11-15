from typing import List, Protocol
from models import Suggestion


class AutocompleteProtocol(Protocol):
    def insert(self, term: str, weight: int) -> None:
        ...

    def top_k(self, prefix: str, k: int) -> List[Suggestion]:
        ...
