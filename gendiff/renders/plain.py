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


def change_value(value):
    if isinstance(value, dict):
        value = '[complex value]'
    elif isinstance(value, tuple):
        value = list(value)
        value[0] = change_value(value[0])
        value[1] = change_value(value[1])
        value = tuple(value)
    elif isinstance(value, bool):
        value = str(value).lower()
    else:
        value = f"'{value}'"
    return value


def replace_keys(diff, path='') -> list:
    new_diff = []
    for k, v in diff.items():
        if k[0] == NESTED:
            new_diff += replace_keys(v, f'{path}.{k[1]}'.strip('.'))
            continue
        elif k[0] == UNCHANGED:
            continue

        v = change_value(v)
        v = v if isinstance(v, str) else v[0], v[1],
        new_diff.append(TEMPLATE.format(
            f'{path}.{k[1]}'.strip('.'),
            STATUSES[k[0]].format(*v)
        ))

    return new_diff


def render_plain(diff) -> str:
    return '\n'.join(replace_keys(diff))
