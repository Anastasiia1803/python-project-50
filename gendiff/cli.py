import argparse

from gendiff.constants import FORMATS


def get_arg_parser():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
    )
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument(
        '-f', '--format',
        help='set format of output: ' + ', '.join(FORMATS.keys()),
        default='stylish', type=str
    )
    return parser


def parse_args():
    args = get_arg_parser().parse_args()
    return args
