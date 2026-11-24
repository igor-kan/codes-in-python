from typing import Protocol

class AlgorithmContract(Protocol):
    def module_slug(self) -> str: ...

def contract_slug() -> str:
    return "lfu_cache_py_d59"
