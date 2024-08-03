newton = 1    # "Великий учёный физик - Исаак Ньютон"
lennon = 2    # "Джон Леннон"
putin = 3     # "В.В.Путин"
gagarin = 4   # "Ю.А.Гагарин"
mask = 5      # "Илон Маск"
jagger = 6    # "Мик Джаггер"
tyson = 7     # "Майк Тайсон"
jackson = 8   # "Майкл Джексон"
maradona = 9  # "Диего Марадона"
chaplin = 10  # "Чарли Чаплин"

GreatPeople = [newton, lennon, putin, gagarin, mask, jagger, tyson, jackson, maradona, chaplin]
import random
while True:
    result = random.sample(GreatPeople, 5)
    print(result)
    greatMan = []
    for i in result:
        if i == 1:
            newton = str(input('Введите дату рождения Исаака Ньютона: -'))
            if newton == '25.12.1642':
                newton = True
                print('Верно!')
            elif newton != '25.12.1642':
                newton = False
                print('Неверно. Дата рождения Исаака Ньютона - двадцать пятое декабря 1642 года.')
            greatMan.append(newton)
        if i == 2:
            lennon = str(input('Введите дату рождения Джона Леннона: -'))
            if lennon == '09.10.1940':
                lennon = True
                print('Верно!')
            elif lennon != '09.10.1940':
                lennon = False
                print('Неверно. Дата рождения Джона Леннона - девятое октября 1940 года.')
            greatMan.append(lennon)
        if i == 3:
            putin = str(input('Введите дату рождения В.В.Путина: -'))
            if putin == '07.10.1952':
                putin = True
                print('Верно!')
            elif putin != '07.10.1952':
                putin = False
                print('Неверно. Дата рождения В.В.Путина - седьмое октября 1952 года.')
            greatMan.append(putin)
        if i == 4:
            gagarin = str(input('Введите дату рождения Ю.А.Гагарина: -'))
            if gagarin == '09.03.1934':
                gagarin = True
                print('Верно!')
            elif gagarin != '09.03.1934':
                gagarin = False
                print('Неверно. Дата рождения Ю.А.Гагарина - девятое марта 1934 года.')
            greatMan.append(gagarin)
        if i == 5:
            mask = str(input('Введите дату рождения Илона Маска: -'))
            if mask == '28.06.1971':
                mask = True
                print('Верно!')
            elif mask != '28.06.1971':
                mask = False
                print('Неверно. Дата рождения Илона Маска - двадцать восьмое июня 1971 года.')
            greatMan.append(mask)
        if i == 6:
            jagger = str(input('Введите дату рождения Мика Джаггера: -'))
            if jagger == '26.07.1943':
                jagger = True
                print('Верно!')
            elif jagger != '26.07.1943':
                jagger = False
                print('Неверно. Дата рождения Мика Джаггера - двадцать шестое июля 1943 года.')
            greatMan.append(jagger)
        if i == 7:
            tyson = str(input('Введите дату рождения Майка Тайсона: -'))
            if tyson == '30.06.1966':
                tyson = True
                print('Верно!')
            elif tyson != '30.06.1966':
                tyson = False
                print('Неверно. Дата рождения Майка Тайсона - тридцатое июня 1966 года.')
            greatMan.append(tyson)
        if i == 8:
            jackson = str(input('Введите дату рождения Майкла Джексона: -'))
            if jackson == '29.08.1958':
                jackson = True
                print('Верно!')
            elif jackson != '29.08.1958':
                jackson = False
                print('Неверно. Дата рождения Майкла Джексона - двадцать девятое августа 1958 года.')
            greatMan.append(jackson)
        if i == 9:
            maradona = str(input('Введите дату рождения Диего Марадона: -'))
            if maradona == '30.10.1960':
                maradona = True
                print('Верно!')
            elif maradona != '30.10.1960':
                maradona = False
                print('Неверно. Дата рождения Диего Марадона - тридцатое октября 1960 года.')
            greatMan.append(maradona)
        if i == 10:
            chaplin = str(input('Введите дату рождения Чарли Чаплина: -'))
            if chaplin == '16.04.1889':
                chaplin = True
                print('Верно!')
            else:
                chaplin = False
                print('Неверно. Дата рождения Чарли Чаплина - шестнадцатое апреля 1889 года.')
            greatMan.append(chaplin)
    answer_yes = []
    answer_no = []
    for k in greatMan:
        if k == True:
            answer_yes.append(k)
        if k == False:
            answer_no.append(k)

    print('Количество правильных ответов: -', len(answer_yes))
    print('Количество не правильных ответов: -', len(answer_no))
    print('Процент правильных ответов: -', (len(answer_yes)*100)/5, '%')
    print('Процент неправильных ответов: -', (len(answer_no)*100)/5, '%')
    print('Для продолжения игры нажмите - 1, если нет нажмите - 0')

    games = int(input('Хотите продолжить игру? -'))
    if games == 1:
        True
    elif games == 0:
        break