import pathlib

import pytest

from gendiff.main import generate_diff

FIXTURES_PATH = pathlib.Path(__file__).parent / 'fixtures'


@pytest.mark.parametrize('paths', (
        ('file1.json', 'file2.json', 'result.txt'),
        ('file1.json', 'file2.json', 'result.txt'),
        ('nested_file1.yml', 'nested_file2.yml', 'nested_result.txt'),
        ('nested_file1.json', 'nested_file2.json', 'nested_result.txt')
))
def test_gendiff(paths):
    with open(FIXTURES_PATH / paths[2]) as f:
        expected = f.read()
    got = generate_diff(
        FIXTURES_PATH / paths[0], FIXTURES_PATH / paths[1])
    assert got == expected
