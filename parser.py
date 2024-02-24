import json
from pathlib import Path

import yaml


def load_file(path) -> dict:
    file_name = Path(path).resolve()
    with open(file_name) as f:
        if file_name.suffix == '.json':
            data = json.load(f)
        elif file_name.suffix in ['.yml', '.yaml']:
            data = yaml.safe_load(f)
    return data
