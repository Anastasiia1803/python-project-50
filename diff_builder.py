from gendiff.constants import (UNCHANGED, UPDATED, NESTED,
                               ADDED, DELETED)


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
