from concurrent.futures import ThreadPoolExecutor
from typing import Dict, List, Tuple
from core import EarleyParser

def parallel_recognize(grammar: Dict[str, List[Tuple[str, ...]]], start: str, inputs: List[List[str]]) -> List[bool]:
    parser = EarleyParser(grammar, start)
    with ThreadPoolExecutor(max_workers=2) as pool:
        return list(pool.map(parser.recognizes, inputs))
