import json


def replace_keys(diff):
    new_diff = {}
    for k, v in diff.items():
        key = f'{k[0]} {k[1]}' if isinstance(k, tuple) else k
        if isinstance(v, dict):
            new_diff[key] = replace_keys(v)
            continue

        new_diff[key] = v

    return new_diff


def render_stylish(diff) -> str:
    diff = replace_keys(diff)
    return json.dumps(
        diff, indent=2
    ).replace(
        '"', ''
    ).replace(
        ',', ''
    ).replace(' \n', '\n')
