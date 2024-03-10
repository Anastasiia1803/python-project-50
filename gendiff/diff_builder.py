from gendiff.constants import (UNCHANGED, UPDATED, NESTED,
                               ADDED, DELETED)


def get_diff(data1, data2):
    keys = sorted(data1.keys() | data2.keys())
    diff = {}
    for key in keys:
        value2 = data2.get(key)
        value1 = data1.get(key)

        if key not in data1:
            diff[key] = {ADDED: value2}
            continue

        if key not in data2:
            diff[key] = {DELETED: value1}
            continue

        if isinstance(value1, dict) and isinstance(value2, dict):
            diff[key] = {NESTED: get_diff(value1, value2)}
            continue

        if value2 != value1:
            diff[key] = {UPDATED: (value1, value2)}
            continue

        diff[key] = {UNCHANGED: value1}

    return diff
