"""
МОДУЛЬ 1
В модуле прописаны заготовки для 8 функций
Под каждой функцией есть описание как она должна работать
ниже есть примеры использования функции
Задание: реализовать код функции, чтобы он работал по описанию и примеры использования давали верный результат
"""


print('Функция №1. Введите пять любых чисел, от 0 до 9.')
def simple_separator():
    """
    Функция создает красивый резделитель из 10-и звездочек (**********)
    return
    """
    tur = input()
    return (print('**********'.join(tur)))
simple_separator()

print('Функция №2.')
def long_separator(x):
    """
    Функция создает разделитель из звездочек число которых можно регулировать параметром count
    :param count: количество звездочек
    :return: строка разделитель, примеры использования ниже
    """
    return (print(('*' * x)))
long_separator(5)   # True
long_separator(8)   # True

print('Функция №3.')
def separator(a, b):
    """
    Функция создает разделитель из любых символов любого количества
    :param simbol: символ разделителя
    :param count: количество повторений
    :return: строка разделитель примеры использования ниже
    """
    glist = input('Введите - ')
    print((a * b).join(glist))
    return
separator('*', 10) # True
separator('%', 5) # True

print('Функция №4. ')
def hello_world():
    """
    Функция печатает Hello World в формате:
    **********

    Hello World!

    ##########
    :return: None
    """
    print('*' * 10)
    print('Hello World!')
    print('#' * 10)

'''
**********

Hello World!

##########
'''
hello_world()

print('Функция №5.')
def hello_who(who='World'):
    """
    Функция печатает приветствие в красивом формате
    **********

    Hello {who}!

    ##########
    :param who: кого мы приветствуем, по умолчанию World
    :return: None
    """
    print('*' * 10)
    print(f'Hello, {who}!')
    print('#' * 10)
    return
'''
**********

Hello World!

##########
'''
hello_who()
'''
**********

Hello Max!

##########
'''
hello_who('Max')
'''
**********

Hello Kate!

##########
'''
hello_who('Askhat')
hello_who('Gulnar')
hello_who('Salmira')
hello_who('Alina')

print('Функция №6.')
def pow_many(power, *args):
    """
    Функция складывает любое количество цифр и возводит результат в степень power (примеры использования ниже)
    :param power: степень
    :param args: любое количество цифр
    :return: результат вычисления # True -> (1 + 2)**1
    """
    adf = (sum(args)**power)
    return print(adf)
pow_many(1, 1, 2) == 3  # True -> (1 + 2)**1 == 3
pow_many(1, 2, 3) == 5  # True -> (2 + 3)**1 == 5
pow_many(2, 1, 1) == 4  # True -> (1 + 1)**2 == 4
pow_many(3, 2) == 8  # True -> 2**3 == 8
pow_many(2, 1, 2, 3, 4) == 100  # True -> (1 + 2 + 3 + 4)**2 == 10**2 == 100
pow_many(3, 4, 3, 2, 5)

print('Функция №7.')
def print_key_val(**kwargs):
    """
    Функция выводит переданные параметры в фиде key --> value
    key - имя параметра
    value - значение параметра
    :param kwargs: любое количество именованных параметров
    :return: None
    """
    for key, value in kwargs.items():
        print('{} is {}'.format(key, value))


"""
name --> Max
age --> 21
"""
print_key_val(name='Max', age=21)
"""
animal --> Cat
is_animal --> True
"""
print_key_val(animal='Cat', is_animal=True)
print_key_val(name='Askhat', age=51)
print_key_val(auto='TOYOTA', model='FG CRUISER')

print('Функция №8.')
def my_filter(iterable, function):
    """
    (Усложненое задание со *)
    Функция фильтрует последовательность iterable и возвращает новую
    Если function от элемента последовательности возвращает True, то
    элемент входит в новую последовательность иначе нет
    (примеры ниже)
    :param iterable: входаня последовательности
    :param function: функция фильтрации
    :return: новая отфильтрованная последовательность
    """
    list_a = []
    for x in iterable:
        if function(x):
            list_a.append(x)
    return list_a

print(my_filter([1, 2, 3, 4, 5], lambda x: x > 3) == [4, 5])  # True
print(my_filter([1, 2, 3, 4, 5], lambda x: x == 2) == [2])  # True
print(my_filter([1, 2, 3, 4, 5], lambda x: x != 3) == [1, 2, 4, 5])  # True
print(my_filter(['a', 'b', 'c', 'd'], lambda x: x in 'abba') == ['a', 'b'])  # True