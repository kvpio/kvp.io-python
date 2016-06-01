#! /bin/bash

pdoc --html \
    --overwrite \
    --html-no-source \
    --html-dir ../kvp.io-python-docs/ \
    kvpio
mv ../kvp.io-python-docs/kvpio/* ../kvp.io-python-docs/
rm ../kvp.io-python-docs/kvpio/ -fR
