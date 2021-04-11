check:
	black --check .
	isort --check .
	flake8
	mypy .

coverage:
	coverage run setup.py test
	coverage combine
	coverage html
	coverage report

dev:
	python3 -m pip install -q -U pip~=21.0.0 pip-tools~=6.0.0
	pip-sync requirements.txt

fix:
	black .
	isort .
	flake8
	mypy .

outdated:
	python3 -m pip list --outdated

pip:
	python3 -m pip install -q -U pip~=21.0.0 pip-tools~=6.0.0
	pip-compile -q -U -o requirements.txt requirements.in
