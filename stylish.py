import json

from gendiff.constants import SEPARATORS, UPDATED, DELETED, ADDED


def replace_keys(diff):
    new_diff = {}
    for k, v in diff.items():
        if k[0] == UPDATED:
            new_diff[f'{SEPARATORS[DELETED]} {k[1]}'] = v[0]
            new_diff[f'{SEPARATORS[ADDED]} {k[1]}'] = v[1]
            continue
        key = f'{SEPARATORS[k[0]]} {k[1]}' if isinstance(k, tuple) else k
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
