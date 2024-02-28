import json


def render_json(diff) -> str:
    return json.dumps(diff, indent=4)
