import pathlib

import pytest

from gendiff.generate_diff import generate_diff

FIXTURES_PATH = pathlib.Path(__file__).parent / 'fixtures'
FILES_PATH = FIXTURES_PATH / 'files'
RESULTS_PATH = FIXTURES_PATH / 'results'


@pytest.mark.parametrize(
    'files', (
            ('file1.json', 'file2.json'),
            ('file1.yml', 'file2.yml'),
    )
)
@pytest.mark.parametrize('_format', ('plain', 'stylish', 'json'))
@pytest.mark.parametrize('structure', ('nested', 'flat'))
def test_gendiff(files, _format, structure):
    expected = (RESULTS_PATH / structure / f'{_format}_result.txt').read_text()
    got = generate_diff(
        FILES_PATH / structure / files[0],
        FILES_PATH / structure / files[1],
        _format
    )
    assert got == expected
