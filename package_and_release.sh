#!/bin/bash

echo "running \n $ python setup.py sdist \n"
VERSION=$(python setup.py sdist | grep -oE '[0-9]{1,4}\.[0-9]{1,4}\.[0-9]{1,4}[a-z]{0,1}' | head -n1)

echo $VERSION

echo "using twine to upload... \n"
twine upload dist/roundtrip-${VERSION}.tar.gz
