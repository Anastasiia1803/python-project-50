from gendiff.constants import ADDED, UPDATED, DELETED, NESTED, UNCHANGED

TEMPLATE = "Property '{}' was {}"

STATUSES = {
    UPDATED: "updated. From {} to {}",
    ADDED: "added with value: {}",
    DELETED: "removed",
}


def to_str(value):
    if isinstance(value, dict):
        value = '[complex value]'
    elif isinstance(value, tuple):
        value = list(value)
        value[0] = to_str(value[0])
        value[1] = to_str(value[1])
        value = tuple(value)
    elif isinstance(value, bool):
        value = str(value).lower()
    elif value is None:
        value = 'null'
    elif isinstance(value, str):
        value = f"'{value}'"
    else:
        value = str(value)
    return value


def make_stylish_format(diff, path='') -> list:
    new_diff = []
    for k, v in diff.items():
        separator, value = list(v.items())[0]
        if separator == NESTED:
            new_diff += make_stylish_format(value, f'{path}.{k}'.strip('.'))
            continue
        elif separator == UNCHANGED:
            continue

        value = to_str(value)
        value = value if isinstance(value, str) else value[0], value[1]

        new_diff.append(TEMPLATE.format(
            f'{path}.{k}'.strip('.'),
            STATUSES[separator].format(*value)
        ))

    return new_diff


def render_plain(diff) -> str:
    return '\n'.join(make_stylish_format(diff))
