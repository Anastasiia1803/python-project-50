from gendiff.constants import STYLIST_FORMAT, PLAIN_FORMAT, JSON_FORMAT
from gendiff.renders.json import render_json
from gendiff.renders.plain import render_plain
from gendiff.renders.stylish import render_stylish

FORMATS = {
    STYLIST_FORMAT: render_stylish,
    PLAIN_FORMAT: render_plain,
    JSON_FORMAT: render_json,
}


def render_view(diff, format_):
    render_func = FORMATS.get(format_)
    return render_func(diff)
