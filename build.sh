#! /bin/bash

py.test --cov-report term --cov=kvpio

pycco ./kvpio/*.py -d ../kvp.io-python-docs/
cp ./pycco-dark.css ../kvp.io-python-docs/pycco.css
rm ../kvp.io-python-docs/cli.html
mv ../kvp.io-python-docs/__init__.html ../kvp.io-python-docs/index.html
