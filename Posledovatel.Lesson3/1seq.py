fish = int(input("Введите количество пойманной рыбы: -"))
fishWeight = []
i = 0
while i < fish:
    proff = 'Введите вес (кг) ' + str(i+1) + '-й пойманной рыбы:'
    fishWeight.append(int(input(proff)))
    i += 1
fishWeight.sort()
print(fishWeight)
print(type(fishWeight))