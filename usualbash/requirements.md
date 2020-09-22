## Init venv

````bash
python3.8 -m venv venv
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

## Remove all packages in requirements.txt

````bash
python -m pip uninstall -r requirements.txt -y
````

## Ubuntu essential packages:

````bash
apt install python3.8-dev python3-setuptools
````

# Example full init python dependencies

````bash
#!/usr/bin/env bash

set -e
set -x

isFirstTime=false
if [[ ! -d "$PWD/venv" ]]; then
    isFirstTime=true
fi

if [[ "$isFirstTime" = true ]]; then
    python3.8 -m venv venv
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
