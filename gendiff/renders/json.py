import json


def replace_keys(diff):
    new_diff = {}
    for k, v in diff.items():
        if isinstance(k, tuple):
            new_diff[k[1]] = {k[0]: v}
        else:
            new_diff[k] = v
            continue

        if isinstance(v, dict):
            new_diff[k[1]] = {k[0]: replace_keys(v)}
            continue
    return new_diff


def render_json(diff) -> str:
    return json.dumps(replace_keys(diff), indent=4)
