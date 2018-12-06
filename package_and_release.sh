#!/bin/bash

# edit version in setup.py


# git commit, etc

echo "You still have to increment the version and do git stuff by hand..."
sleep 2
echo "did you do that?"
sleep 2

echo "running \n $ python setup.py sdist \n"
VERSION=$(python setup.py sdist | grep -oE '[0-9]{1,4}\.[0-9]{1,4}\.[0-9]{1,4}[a-z]{0,1}' | head -n1)

echo $VERSION

echo "using twine to upload... \n"
twine upload dist/roundtrip-${VERSION}.tar.gz
