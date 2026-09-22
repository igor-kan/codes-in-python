import runpy
from pathlib import Path

_MODULE = Path(__file__).with_name("base64_codec.py")


def test_main_asserts():
    runpy.run_path(str(_MODULE), run_name="__main__")
