### List packages to requirements.txt
```python -m pip freeze > requirements.txt```  
```python -m pip freeze --local > requirements.txt```

### Remove all packages in requirements.txt
```python -m pip uninstall -r requirements.txt -y```