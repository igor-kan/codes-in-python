import runpy
from pathlib import Path

_MODULE = Path(__file__).with_name("miller_rabin.py")


def test_main_asserts():
    runpy.run_path(str(_MODULE), run_name="__main__")
