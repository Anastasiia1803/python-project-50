install:
	poetry install

build:
	poetry build

publish:
	poetry publish --dry-run

lint:
	poetry run flake8 gendiff

test:
	poetry run pytest -vv  --strict-markers

package-install:
	python -m pip install --user dist/*.whl --force-reinstall

package-reinstall:
	python -m pip install dist/*.whl --force-reinstall

test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml