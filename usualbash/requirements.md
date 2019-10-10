### List packages to requirements.txt
```python3.7 -m pip freeze > requirements.txt```  
```python3.7 -m pip freeze --local > requirements.txt```

### Remove all packages in requirements.txt
```python3.7 -m pip uninstall -r requirements.txt -y```

### Ubuntu essential packages:
```apt install python3.7-dev python3-setuptools```