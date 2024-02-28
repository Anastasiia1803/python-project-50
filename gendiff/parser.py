import json
from pathlib import Path

import yaml


def get_file_ext(file_path):
    return Path(file_path).suffix[1:]


def get_file_content(file_path):
    with open(file_path) as file:
        return file.read()


def parse_data(content, _format):
    if _format == 'json':
        return json.loads(content)
    if _format in ['yml', 'yaml']:
        return yaml.safe_load(content)
    raise ValueError(f"Формат {_format} не поддерживается")


def load_file(path):
    _format = get_file_ext(path)
    content = get_file_content(path)
    return parse_data(content, _format)
