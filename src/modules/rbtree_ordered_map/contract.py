from typing import List, Optional, Protocol, Tuple


class OrderedMapProtocol(Protocol):
    def insert(self, key: int, value: int) -> None:
        ...

    def get(self, key: int) -> Optional[int]:
        ...

    def inorder_items(self) -> List[Tuple[int, int]]:
        ...
