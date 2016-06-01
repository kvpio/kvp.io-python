#! /bin/bash

rm ./docs/* -fR
pdoc --html --html-no-source --html-dir ./docs/ kvpio
