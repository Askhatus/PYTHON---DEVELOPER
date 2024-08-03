auto = input('Введите любые числа: -')
moto = []
mot = []
for i in auto:
    moto.append(i)
print(moto)
for i in moto:
    if moto.count(i) == 1:
      mot.append(i)
#mot.sort()
print(str(mot))
print('; '.join(mot))
print('/ '.join(mot))
print(', '.join(mot))


