"""
МОДУЛЬ 3
Программа "Личный счет"
Описание работы программы:
Пользователь запускает программу у него на счету 0
Программа предлагает следующие варианты действий
1. пополнить счет
2. покупка
3. история покупок
4. выход

1. пополнение счета
при выборе этого пункта пользователю предлагается ввести сумму на сколько пополнить счет
после того как пользователь вводит сумму она добавляется к счету
снова попадаем в основное меню

2. покупка
при выборе этого пункта пользователю предлагается ввести сумму покупки
если она больше количества денег на счете, то сообщаем что денег не хватает и переходим в основное меню
если денег достаточно предлагаем пользователю ввести название покупки, например (еда)
снимаем деньги со счета
сохраняем покупку в историю
выходим в основное меню

3. история покупок
выводим историю покупок пользователя (название и сумму)
возвращаемся в основное меню

4. выход
выход из программы

При выполнении задания можно пользоваться любыми средствами

Для реализации основного меню можно использовать пример ниже или написать свой
"""
shot = 0
history = []
while True:
    print('1. пополнение счета')
    print('2. покупка')
    print('3. история покупок')
    print('4. выход')
    choice = input('Выберите пункт меню: - ')
    if choice == '1':
      money = float(input('Введите сумму: - '))
      shot += money
    elif choice == '2':
        pok = float(input('Введите сумму покупок: - '))
        if pok > money:
            print('Недостаточно средств. Пополните пожалуйста счёт.')
            money_balance = float(input('Пополнить баланс: - '))
            shot += money_balance
        else:
            product_name = input('Ввести название покупки: - ')
            shot -= pok
            history.append((product_name, pok))
    elif choice == '3':
      if history:
        print("\nИстория покупок:")
        for name, pok in history:
          print(f"{name}: {pok}")
    elif choice == '4':
      print(shot)
      print('PROGRAM EXIT.')
      break
    else:
        print('Неверный пункт меню')
