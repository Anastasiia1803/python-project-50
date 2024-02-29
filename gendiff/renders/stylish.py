from gendiff.constants import UPDATED, DELETED, ADDED, NESTED, UNCHANGED

SEPARATOR = " "
ADD = '+ '
DELETE = '- '
NONE = '  '


def to_str(value, spaces_count=2):
    if value is None:
        return "null"

    if isinstance(value, bool):
        return str(value).lower()
    elif isinstance(value, tuple):
        value = list(value)
        value[0] = to_str(value[0])
        value[1] = to_str(value[1])
        value = tuple(value)
    elif isinstance(value, dict):
        indent = SEPARATOR * (spaces_count + 4)
        lines = []
        for key, inner_value in value.items():
            formatted_value = to_str(inner_value, spaces_count + 4)
            lines.append(f"{indent}  {key}: {formatted_value}")
        formatted_string = '\n'.join(lines)
        end_indent = SEPARATOR * (spaces_count + 4)
        return f"{{\n{formatted_string}\n{end_indent}}}"
    return value


def replace_keys(diff, spaces_count=2):
    indent = SEPARATOR * spaces_count
    lines = []
    for k, v in diff.items():
        separator, value = list(v.items())[0]
        if separator == NESTED:
            nested = replace_keys(
                value, spaces_count + 4
            )
            lines.append(f"{indent}{NONE}{k}: {nested}")

        value = to_str(value)

        if separator == UNCHANGED:
            current_value = to_str(value, spaces_count)
            lines.append(f"{indent}{NONE}{k}: {current_value}")
        elif separator == UPDATED:
            lines.append(f"{indent}{DELETE}{k}: {value[0]}")
            lines.append(f"{indent}{ADD}{k}: {value[1]}")
        elif separator == DELETED:
            lines.append(f"{indent}{DELETE}{k}: {value}")
        elif separator == ADDED:
            lines.append(f"{indent}{ADD}{k}: {value}")

    formatted_string = '\n'.join(lines)
    end_indent = SEPARATOR * (spaces_count - 2)

    return f"{{\n{formatted_string}\n{end_indent}}}"

def render_stylish(diff) -> str:
    print('{\n    common: {\n      + follow: false\n        setting1: Value 1\n      - setting2: 200\n      - setting3: true\n      + setting4: blah blah\n      + setting5: {\n        key5: value5\n      }\n        setting6: {\n            doge: {\n              - wow: \n              + wow: so much\n            }\n            key: value\n          + ops: vops\n        }\n    }\n    group1: {\n      - baz: bas\n      + baz: bars\n        foo: bar\n      - nest: {\n        key: value\n      }\n      + nest: str\n    }\n  - group2: {\n        abc: 12345\n        deep: {\n            id: 45\n          }\n      }\n  + group3: {\n        deep: {\n            id: {\n                number: 45\n              }\n          }\n        fee: 100500\n      }\n}')
    return replace_keys(diff)
