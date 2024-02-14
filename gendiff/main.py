import json
from pathlib import Path

import yaml

from gendiff.constants import (STYLIST_FORMAT, DELETED,
                               UNCHANGED, UPDATED, ADDED, NESTED)
from gendiff.renders import render_view

BASE_DIR = Path(__file__).parent.parent


def load_file(path) -> dict:
    file_name = Path(path).resolve()
    with open(file_name) as f:
        if file_name.suffix == '.json':
            data = json.load(f)
        elif file_name.suffix in ['.yml', '.yaml']:
            data = yaml.safe_load(f)
    return data


def get_diff(json1, json2):
    diff = {}
    for key1, value1 in json1.items():
        value2 = json2.get(key1)
        if isinstance(value1, str):
            value1 = value1.strip()

        if value2 is None:
            diff[(DELETED, key1)] = value1
            continue

        if isinstance(value1, dict) and isinstance(value2, dict):
            diff[(NESTED, key1)] = get_diff(value1, value2)
            continue

        if value2 != value1:
            diff[(UPDATED, key1)] = (value1, value2)
            continue

        diff[(UNCHANGED, key1)] = value1

    for key2, value2 in json2.items():
        if json1.get(key2) is None:
            diff[(ADDED, key2)] = value2
    return dict(sorted(diff.items(), key=lambda item: item[0][1]))


def generate_diff(file1, file2, _format=STYLIST_FORMAT) -> str:
    data1 = load_file(file1)
    data2 = load_file(file2)
    diff = get_diff(data1, data2)
    return render_view(diff, _format)
