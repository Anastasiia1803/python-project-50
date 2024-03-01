from gendiff.constants import (UNCHANGED, UPDATED, NESTED,
                               ADDED, DELETED)


def get_diff(data1, data2):
    diff = {}
    for key1, value1 in data1.items():
        value2 = data2.get(key1)

        if isinstance(value1, str):
            value1 = value1.strip()

        if value2 is None:
            diff[key1] = {DELETED: value1}
            continue

        if isinstance(value1, dict) and isinstance(value2, dict):
            diff[key1] = {NESTED: get_diff(value1, value2)}
            continue

        if value2 != value1:
            diff[key1] = {UPDATED: (value1, value2)}
            continue

        diff[key1] = {UNCHANGED: value1}

    for key2, value2 in data2.items():
        if data1.get(key2) is None:
            diff[key2] = {ADDED: value2}
    return dict(sorted(diff.items(), key=lambda item: item[0]))
