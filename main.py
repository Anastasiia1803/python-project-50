from pathlib import Path

from gendiff.constants import STYLIST_FORMAT
from gendiff.diff_builder import get_diff
from gendiff.parser import load_file
from gendiff.renders import render_view

BASE_DIR = Path(__file__).parent.parent


def generate_diff(file1, file2, _format=STYLIST_FORMAT) -> str:
    data1 = load_file(file1)
    data2 = load_file(file2)
    diff = get_diff(data1, data2)
    return render_view(diff, _format)
