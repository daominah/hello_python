## Init venv

````bash
python3.8 -m venv venv
source venv/bin/activate
pip install --index-url https://pypi.python.org/simple/ --upgrade pip
````

## List packages to requirements.txt

```python -m pip freeze --local > requirements.txt```

## Remove all packages in requirements.txt

```python -m pip uninstall -r requirements.txt -y```

## Ubuntu essential packages:

```apt install python3.8-dev python3-setuptools```
