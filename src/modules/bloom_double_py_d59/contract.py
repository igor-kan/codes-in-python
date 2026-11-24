from typing import Protocol

class AlgorithmContract(Protocol):
    def module_slug(self) -> str: ...

def contract_slug() -> str:
    return "bloom_double_py_d59"
