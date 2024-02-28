"""
    Property 'common.follow' was added with value: false
    Property 'common.setting2' was removed
    Property 'common.setting3' was updated. From true to null
    Property 'common.setting4' was added with value: 'blah blah'
    Property 'common.setting5' was added with value: [complex value]
    Property 'common.setting6.doge.wow' was updated. From '' to 'so much'
    Property 'common.setting6.ops' was added with value: 'vops'
    Property 'group1.baz' was updated. From 'bas' to 'bars'
    Property 'group1.nest' was updated. From [complex value] to 'str'
    Property 'group2' was removed
    Property 'group3' was added with value: [complex value]
"""

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
    else:
        value = f"'{value}'"
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
