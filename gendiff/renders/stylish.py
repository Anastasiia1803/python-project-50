from gendiff.constants import UPDATED, DELETED, ADDED, NESTED, UNCHANGED

SEPARATOR = ' '
ADD = '+'
DELETE = '-'


def to_str(value, spaces_count=2):
    if value is None:
        return "null"

    if isinstance(value, bool):
        return str(value).lower()
    elif isinstance(value, tuple):
        value = list(value)
        value[0] = to_str(value[0], spaces_count)
        value[1] = to_str(value[1], spaces_count)
        value = tuple(value)
    elif isinstance(value, dict):
        indent = SEPARATOR * (spaces_count + 4)
        lines = []
        for key, inner_value in value.items():
            formatted_value = to_str(inner_value, spaces_count + 4)
            lines.append(f"{indent}{'  '}{key}: {formatted_value}")

        formatted_string = '\n'.join(lines)
        end_indent = SEPARATOR * (spaces_count + 2)

        return f"{{\n{formatted_string}\n{end_indent}}}"
    return value


def render_stylish(diff, spaces_count=2):
    indent = SEPARATOR * spaces_count
    lines = []
    for k, v in diff.items():
        separator, value = list(v.items())[0]
        if separator == NESTED:
            nested = render_stylish(
                value, spaces_count + 4
            )
            lines.append(f"{indent}{'  '}{k}: {nested}")
            continue

        value = to_str(value, spaces_count)

        if separator == UNCHANGED:
            current_value = to_str(value, spaces_count)
            lines.append(f"{indent}{'  '}{k}: {current_value}")
        elif separator == UPDATED:
            lines.append(f"{indent}{DELETE} {k}: {value[0]}")
            lines.append(f"{indent}{ADD} {k}: {value[1]}")
        elif separator == DELETED:
            lines.append(f"{indent}{DELETE} {k}: {value}")
        elif separator == ADDED:
            lines.append(f"{indent}{ADD} {k}: {value}")

    formatted_string = '\n'.join(lines)
    end_indent = SEPARATOR * (spaces_count - 2)
    return f"{{\n{formatted_string}\n{end_indent}}}"
