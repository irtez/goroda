# goroda
1. В проекте должно быть 2 режима игры: с другом и с компьютером. Программа вначале предоставляет выбор "Выберите режим игры: 1. Игра с компьютером. 2. Игра вдвоём. 3. Выйти из игры." Возможные ответы "1" (программа выводит "Выбран режим игры с компьютером."), "2" (программа выводит "Выбран режим игры вдвоём") или "3" (программа выводит "Вы выбрали выход из игры"). При игре с компьютером, компьютер первым словом называет Москву, дальше выбирает последний по алфавиту город на заданную букву. При игре вдвоём первым город называет игрок 1.
2. Программа выводит сообщение "Неверно. Назовите город на букву {s_end}", если введённый город или слово начинается не с той буквы, "Неверно. Такого города не существует", если такого города нет в списке и "Неверно. Такой город уже называли", если такой город есть в списке использованных городов. В случае выполнения первых двух условий больший приоритет имеет начинается ли город с заданной буквы.
3. Если город заканчивается на "ь","ъ","ы","ц","й", то называется город на предпоследнюю или третью с конца букву.
4. Программа выводит сообщение "Выиграл 1 игрок." или "Выиграл 2 игрок." в режиме игры вдвоём, "Вы проиграли" или "Вы победили" в режиме игры с компьютером, если больше нет городов на данную букву. Программа выводит "Игра окончена. Назвали {len(cityes_old)} городов из {len(cityes_all)}" в любом случае в конце игры. При вводе слова "стоп" на любом этапе игры игра заканчивается.