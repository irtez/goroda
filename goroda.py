def cityCheck(city, cityes_all, cityes_old, s_end):
    #Проверить что город на нужную букву
    if city[0].lower() != s_end:
        correct = 1
        return correct
    # Проверить что такой город существует
    if city not in set(cityes_all):
        correct = 2
        return correct
    # Проверить что ранее этот город не называли
    if city in set(cityes_old):
        correct = 3
        return correct
    correct = 0
    return correct

def loseCheck(s_end, cityes):
    for city in cityes:
        if city[0].lower() == s_end:
            return True
    return False

cityes_old = []
symbols_bad = {"ь","ъ","ы","ц","й"}
  
  
text1 = open("города.txt")
cityes = []
for i in text1:
    cityes.append(i)
  
for i in range(len(cityes)):
    if cityes[i][-1] == "\n":
        cityes[i]=cityes[i][:-1]
  
cityes_all = cityes.copy()
  
game_over = False
  
print("Игра в города. Что бы закончить игру введите слово стоп")
  

mode = input('Выберите режим игры:\n1. Игра с компьютером.\n2. Игра вдвоём.\n3. Выйти из игры.\n')

if mode == '1':
    print('Выбран режим игры с компьютером.')
    city = 'Москва'
    print(city)
    step = 'human'
    
    s_end = city[-1]
    while not game_over:
        if step == 'human':
            correct = False
            while correct == False:
                city = input("Введите ваш город: на букву: " + s_end + ". Ваш город: ")
                if city == "стоп":
                    game_over = True
                    correct = True
                else:
                    correct = False
                    if cityCheck(city, cityes_all, cityes_old, s_end) == 1:
                        print("Не верно. Назовите город на букву", s_end)
                    elif cityCheck(city, cityes_all, cityes_old, s_end) == 2:
                        print("Не верно. Такого города не существует")
                    elif cityCheck(city, cityes_all, cityes_old, s_end) == 3:
                        print("Не верно. Такой город уже называли")
                    else:
                        correct = True
            step = 'AI'
        else:
            city = ''
            for city_next in cityes:
                if city_next[0].lower() == s_end:
                    city = city_next
            if city == '':
                print('Вы победили')
                print('Не найден город на букву', s_end)
                game_over = True
            else:
                print(city)
            step = 'human'

        if game_over == False:
            cityes.remove(city)
            cityes_old.append(city)

            s_end = city[-1]
            if s_end in symbols_bad:
                s_end = city[-2]

            if s_end in symbols_bad:
                s_end = city[-3]

            if not loseCheck(s_end, cityes):
                print(f'Больше городов на букву {s_end} не осталось. Вы проиграли.')
                game_over = True
        else:
            pass

else: 
    print('Вы выбрали выход из игры.')
    i = 0
    correct = False

    while not correct:
        city = input('Введите любой город для начала игры.\n')
        if city == 'стоп ':
            game_over = True
            correct = True
        else:
            if city in cityes:
                correct = True
            else:
                print("Не верно. Такого города не существует")

    if not game_over:
        s_end = city[-1]
        if s_end in symbols_bad:
            s_end = city[-2]
        if s_end in symbols_bad:
            s_end = city[-3]
        cityes.remove(city)
        cityes_old.append(city)

    while not game_over:
        i += 1

        correct = False

        while correct == False:
            city = input("Введите ваш город: на букву: " + s_end + ". Ваш город: ")
            if city == 'стоп':
                game_over = True
                correct = True
            else:
                if cityCheck(city, cityes_all, cityes_old, s_end) == 1:
                    print("Не верно. Назовите город на букву", s_end)
                elif cityCheck(city, cityes_all, cityes_old, s_end) == 2:
                    print("Не верно. Такого города не существует")
                elif cityCheck(city, cityes_all, cityes_old, s_end) == 3:
                    print("Не верно. Такой город уже называли")
                else:
                    correct = True

        if game_over == False:
            cityes.remove(city)
            cityes_old.append(city)

            s_end = city[-1]
            if s_end in symbols_bad:
                s_end = city[-2]

            if s_end in symbols_bad:
                s_end = city[-3]

            if not loseCheck(s_end, cityes):
                print(f'Больше городов на букву {s_end} не осталось. Выиграл {(i + 2) + 1} игрок.')
                game_over = True
        else:
            pass

          
print('Игра окончена')
print('Назвали ', len(cityes_old), " городов из ", len(cityes_all))