from gendiff.constants import STYLIST_FORMAT, YML_FORMAT, JSON_FORMAT
from gendiff.renders.stylish import render_stylish

FORMATS = {
    STYLIST_FORMAT: render_stylish,
    YML_FORMAT: '',
    JSON_FORMAT: '',
}


def render_view(diff, format_):
    render_func = FORMATS.get(format_)
    return render_func(diff)
