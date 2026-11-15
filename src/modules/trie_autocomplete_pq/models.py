from dataclasses import dataclass, field
from typing import Dict


@dataclass
class TrieNode:
    children: Dict[str, "TrieNode"] = field(default_factory=dict)
    frequency: int = 0
    is_terminal: bool = False


@dataclass(frozen=True)
class Suggestion:
    term: str
    score: int
