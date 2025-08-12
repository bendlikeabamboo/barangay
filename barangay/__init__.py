"""
List of Barangay in the Philippines
"""

from pathlib import Path
import json

_BARANGAY_FILENAME = "barangay.json"
_BARANGAY_EXTENDED_FILENAME = "barangay_extended.json"
_BARANGAY_FLAT_FILENAME = "barangay_flat.json"


_current_file_path = Path(__file__).resolve()
_current_dir = _current_file_path.parent

with open(f"{_current_dir}/{_BARANGAY_FILENAME}", encoding="utf8", mode="r") as file:
    BARANGAY = json.load(file)

with open(
    f"{_current_dir}/{_BARANGAY_EXTENDED_FILENAME}", encoding="utf8", mode="r"
) as file:
    BARANGAY_EXTENDED = json.load(file)

with open(
    f"{_current_dir}/{_BARANGAY_FLAT_FILENAME}", encoding="utf8", mode="r"
) as file:
    BARANGAY_FLAT = json.load(file)
