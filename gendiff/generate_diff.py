from pathlib import Path

from gendiff.constants import STYLIST_FORMAT
from gendiff.diff_builder import get_diff
from gendiff.parser import parse_data
from gendiff.renders import render_diff


def get_file_ext(file_path):
    return Path(file_path).suffix[1:]


def get_file_content(file_path):
    with open(file_path) as file:
        return file.read()


def get_file_data(path):
    _format = get_file_ext(path)
    content = get_file_content(path)
    return parse_data(content, _format)


def generate_diff(file1, file2, _format=STYLIST_FORMAT) -> str:
    data1 = get_file_data(file1)
    data2 = get_file_data(file2)
    diff = get_diff(data1, data2)
    return render_diff(diff, _format)
