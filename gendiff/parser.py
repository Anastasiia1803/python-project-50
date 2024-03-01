import json

import yaml


def parse_data(content, _format):
    match _format:
        case 'json':
            return json.loads(content)
        case 'yml' | 'yaml':
            return yaml.safe_load(content)
        case _:
            raise ValueError(f"Формат {_format} не поддерживается")
