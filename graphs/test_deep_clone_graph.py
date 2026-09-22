import doctest
import importlib.util
from pathlib import Path

_MODULE_PATH = Path(__file__).with_name("deep_clone_graph.py")


def _load():
    spec = importlib.util.spec_from_file_location("deep_clone_graph", _MODULE_PATH)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_doctests():
    module = _load()
    result = doctest.testmod(module)
    assert result.attempted > 0
    assert result.failed == 0
