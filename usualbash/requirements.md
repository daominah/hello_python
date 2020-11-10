## Init venv

````bash
${BIN_PYTHON} -m venv venv
source venv/bin/activate
pip install --index-url https://pypi.python.org/simple/ --upgrade pip
````

## List packages to requirements.txt

````bash
python -m pip freeze --local > requirements.txt
````
or
````bash
python -m pip freeze --local  | grep -v "pkg-resources" > requirements.txt
````

## Install python on Ubuntu 18

````bash
apt update
apt install -qy software-properties-common
add-apt-repository -y ppa:deadsnakes/ppa
apt update

export BIN_PYTHON=python3.7
apt install -qy ${BIN_PYTHON}
apt install -qy python3-distutils python3-pip python3-setuptools
apt install -qy ${BIN_PYTHON}-dev ${BIN_PYTHON}-venv
${BIN_PYTHON} -m pip install --index-url https://pypi.python.org/simple/ --upgrade pip
${BIN_PYTHON} -m pip install virtualenv
````

## Remove all packages in requirements.txt

````bash
python -m pip uninstall -r requirements.txt -y
````

## Example full init python dependencies

````bash
#!/usr/bin/env bash

set -e
set -x

isFirstTime=false
if [[ ! -d "$PWD/venv" ]]; then
    isFirstTime=true
fi

if [[ "$isFirstTime" = true ]]; then
    ${BIN_PYTHON} -m venv venv
fi

source venv/bin/activate

if [[ "$isFirstTime" = true ]]; then
    pip install --index-url https://pypi.python.org/simple/ --upgrade pip
fi

echo $(which python)
echo $(which pip)

pip install -r requirements.txt

if [[ "$isFirstTime" = true ]]; then
    python -c 'import pyppeteer; pyppeteer.chromium_downloader.download_chromium()'
fi

set +x
````
