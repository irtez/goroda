cityes_old = []
symbols_bad = {"ь","ъ"} #1 ошибка
  
  
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
  
city = 'Москва'
print(city)
s_end = 'a'
step = 'human'
cityes_old.append(city)
s_end = city[-1]
s_start = city[0]
  
while game_over == False:    
  
    if step == 'human':
  
        correct = False
        while correct == False:
              
            city = input("Введите ваш город: на букву: " + s_end + ". Ваш город: ")
            if city == "стоп":
                game_over = True
                correct = True
            else:
                correct = True
                #Проверить что город на нужную букву
                if city[0].lower() != s_end and city[-1].lower() != s_end and city[0].lower() != s_start.lower(): #2 и 4 ошибки 
                    correct = False
                    print("Не верно. Назовите город на букву",s_end)

                
  
                #Проверить что такой город существует
                if city in set(cityes_all):
                    pass
                else:
                    correct = False
                    print("Не верно. Такого города не существует")                
  
                #Проверить что ранее этот город не называли
                if city in set(cityes_old):
                    correct = False
                    print("Не верно. Такой город уже называли")    
  
        step = 'AI'
    else:
          
        city = ''
        for city_next in cityes:        #6 ошибка (выбирается всегда последний по алфавиту город на заданную букву)
            if city_next[0].lower() == s_end:
                city = city_next
  
        if city == '': #3 ошибка
            game_over = True
        else:
            print(city)
              
              
        step = 'human'
  
    if game_over == False:
        #cityes.remove(city)     #5 ошибка
        #cityes_old.append(city) 
  
        s_end = city[-1]
        if s_end in symbols_bad:
            s_end = city[-2]
  
        if s_end in symbols_bad:
            s_end = city[-3]

        s_start = city[0]
    else:
        pass
          
print('Вы победили')    #3 ошибка
print('Не найден город на букву', s_end)
print('Игра окончена')
print('Назвали ', len(cityes_old), " городов из ", len(cityes_all))