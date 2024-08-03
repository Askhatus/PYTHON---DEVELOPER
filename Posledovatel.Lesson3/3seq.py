field_A = input('Введите номера игроков на поле А: -')
field_B = input('Введите номера игроков на поле В: -')
fielda = []
fieldb = []
res = []
res_w = []
for i in field_A:
    fielda.append(int(i))
for k in field_B:
    fieldb.append(int(k))
res = (fielda + fieldb)
for g in res:
    if res.count(g) == 1:
      res_w.append(g)
res_w.sort()
print(res_w)


