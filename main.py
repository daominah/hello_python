f1 = open('main.py')
f2 = open('main.py')
print(dir(f1))
print('test:', f1.__sizeof__(), f2.fileno().__sizeof__())