import importlib.util
import sys
from pathlib import Path

day = ('0' + sys.argv[1])[-2:]

base_path = Path(".") / day

spec = importlib.util.spec_from_file_location("solve", str(base_path / "solve.py"))
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

module.solve(base_path / "input")
