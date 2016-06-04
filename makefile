
all: tests clean docs build release

clean:
	rm ./dist -fR
	rm ./build -fR
	rm ./*.egg_info -fR
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +

tests:
	py.test --cov-report term --cov=kvpio

docs:
	rm ../kvp.io-python-docs/*
	pycco ./kvpio/*.py -d ../kvp.io-python-docs/
	cp ./pycco-dark.css ../kvp.io-python-docs/pycco.css
	rm ../kvp.io-python-docs/cli.html
	mv ../kvp.io-python-docs/__init__.html ../kvp.io-python-docs/index.html

build:
	python setup.py sdist
	python setup.py egg_info

release:
	twine register -r pypi ./dist/*
	twine upload -r pypi ./dist/*
