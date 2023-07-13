
from config import TOKEN

import logging
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext

import dp as dp
from aiogram import Bot, Dispatcher, types
import requests

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

logging.basicConfig(level=logging.INFO)

bot = Bot(token="6356202859:AAF2qcAcExjnD59LeE5LfbP_2kN6SrXNHxc")
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

# Обработка команды /start
@dp.message_handler(commands=['start'])
async def handle_start(message: types.Message):
    # Отправляем приветственное сообщение
    await message.reply("Привет я бот, который постарается помочь тебе с подготовкой к экзаменам. Нажмите /menu,"
                        " чтобы открыть список предметов!")

# Установка уровня логирования
logging.basicConfig(level=logging.INFO)

# Инициализация бота и диспетчера
bot = Bot(token="6356202859:AAF2qcAcExjnD59LeE5LfbP_2kN6SrXNHxc")
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


# Команда /start
@dp.message_handler(commands=['menu'])
async def start_command(message: types.Message):
    # Создание кнопок меню
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(types.KeyboardButton('Математика'))
    keyboard.add(types.KeyboardButton('Информатика'))
    keyboard.add(types.KeyboardButton('Русский язык'))

    # Отправка сообщения с меню
    await message.answer("Выберите предмет:", reply_markup=keyboard)


# Обработка выбора предмета
@dp.message_handler(lambda message: message.text in ['Математика', 'Информатика', 'Русский язык'])
async def subject_handler(message: types.Message, state: FSMContext):
    selected_subject = message.text

    if selected_subject == 'Математика':
        await message.answer("Вы выбрали Математику! Нажмите /nummat, чтобы перейти к списку задач.")
    elif selected_subject == 'Информатика':
        await message.answer("Вы выбрали Информатику! Нажмите /numinfo, чтобы перейти к списку задач.")
    elif selected_subject == 'Русский язык':
        await message.answer("Вы выбрали Русский язык! Нажмите /numrus, чтобы перейти к списку задач.")

@dp.message_handler(commands=['nummat'])
async def start_command(message: types.Message):
    # Создание кнопки, открывающей список
    button_text = 'Открыть список задач по математике'
    menu_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    menu_markup.add(types.KeyboardButton(button_text))

    # Отправка сообщения с кнопкой
    await message.answer("Нажмите на кнопку, чтобы открыть список.", reply_markup=menu_markup)


# Обработка нажатия на кнопку
@dp.message_handler(lambda message: message.text == 'Открыть список задач по математике')
async def open_list_handler(message: types.Message, state: FSMContext):
    # Создание списка пунктов
    items = [
        '/matnumber1',
        '/matnumber2',
        '/matnumber3',
        '/matnumber4',
        '/matnumber5'
    ]

    # Формирование сообщения со списком
    list_message = "Список:\n"
    for item in items:
        list_message += f"- {item}\n"

    # Отправка сообщения со списком
    await message.answer(list_message)


@dp.message_handler(commands=['matnumber1'])
async def start_handler(message: types.Message):
    """Ловец (обработчик сообщений)"""
    await message.answer("Научная конференция проводится в 5 дней. Всего запланировано 75 докладов— первые три дня по 17 "
            "докладов, остальные распределены поровну между четвертым и пятым днями. Порядок докладов"
    " определяется жеребьёвкой. Какова вероятность, что доклад профессора М. окажется запланированным на последний день "
                         "конференции?"
                "Нажмите /matans1, Чтобы увидеть объяснение и ответ.Нажмите /matnumber2, чтобы перейти к следущему номеру.")

@dp.message_handler(commands=['matnumber2'])
async def start_handler(message: types.Message):
    """Ловец (обработчик сообщений)"""
    await message.answer("Какова вероятность того, что случайно выбранный телефонный номер оканчивается двумя чётными цифрами?"
                "Нажмите /matans2, Чтобы увидеть объяснение и ответ.Нажмите /matnumber3, чтобы перейти к следущему номеру.")

@dp.message_handler(commands=['matnumber3'])
async def start_handler(message: types.Message):
        """Ловец (обработчик сообщений)"""
        await message.answer("Первый и второй насосы наполняют бассейн за 9минут, второй и третий— за 14минут, а первый и "
                             "третий— за 18минут. "
                             "За сколько минут эти три насоса заполнят бассейн, работая вместе?"
            "Нажмите /matans3, Чтобы увидеть объяснение и ответ.Нажмите /matumber4, чтобы перейти к следущему номеру.")

@dp.message_handler(commands=['matnumber4'])
async def start_handler(message: types.Message):
            """Ловец (обработчик сообщений)"""
            await message.answer(
"Фабрика выпускает сумки. В среднем 8 сумок из 100 имеют скрытые дефекты. Найдите вероятность того, что"
" купленная сумка окажется без дефектов."
"Нажмите /matans4, Чтобы увидеть объяснение и ответ.Нажмите /matumber5, чтобы перейти к следущему номеру.")

@dp.message_handler(commands=['matnumber5'])
async def start_handler(message: types.Message):
                """Ловец (обработчик сообщений)"""
                await message.answer(
                    "По двум параллельным железнодорожным путям в одном направлении следуют пассажирский и товарный поезда,"
                    " скорости которых равны соответственно 90 км/ч и 30 км/ч. Длина товарного поезда равна 600 метрам."
                    " Найдите длину пассажирского поезда, если время, за которое он прошел мимо товарного поезда, равно 1 минуте."
                    " Ответ дайте в метрах."
                    "Нажмите /matans5, Чтобы увидеть объяснение и ответ.Нажмите /menu, чтобы перейти к списку ппредметов." )




#ответы математика
@dp.message_handler(commands=['matans1'])
async def start_handler(message: types.Message):
    """Ловец (обработчик сообщений)"""
    await message.answer("За первые три дня будет прочитан 51 доклад, на последние два дня планируется 24 доклада."
" Поэтому на последний день запланировано 12 докладов. Значит, вероятность того, что доклад профессора М. окажется"
    " запланированным на последний день конференции, равна  дробь 12/75=0,16."
"Ответ: 0,16.")

@dp.message_handler(commands=['matans2'])
async def start_handler(message: types.Message):
        """Ловец (обработчик сообщений)"""
        await message.answer("Вероятность того, что на одном из требуемых мест окажется чётное число равна 0,5. "
                             "Следовательно, вероятность того, что на двух местах одновременно окажутся два чётных "
                             "числа равна 0,5*0,5 = 0,25."
"Ответ: 0,25.")

@dp.message_handler(commands=['matans3'])
async def start_handler(message: types.Message):
            """Ловец (обработчик сообщений)"""
            await message.answer(
                "Наименьшее общее кратное чисел 9, 14 и 18 равно 126. За 126 минут первый и второй, второй и третий, первый "
                "и третий насосы (каждый учтен дважды) заполнят 14+9+7=30 бассейнов."
                " Следовательно, работая одновременно, первый, второй и третий насосы заполняют 15 бассейнов за 126 минут,"
                " а значит, 1 бассейн за 8,4 минуты."
 "Ответ: 8,4.")


@dp.message_handler(commands=['matans4'])
async def start_handler(message: types.Message):
        """Ловец (обработчик сообщений)"""
        await message.answer("В среднем без дефектов выпускают 92 сумки из каждых 100,поэтому искомая вероятность равна 0,92. Ответ: 0,92.")

@dp.message_handler(commands=['matans5'])
async def start_handler(message: types.Message):
              """Ловец (обработчик сообщений)"""
              await message.answer(
                  "Скорость сближения поездов равна 60км/ч или 1км/мин. Следовательно, за 1 минуту пассажирский"
                  " поезд сместится относительно товарного на 1км. При этом он преодолеет расстояние, равное сумме "
                  "длин поездов. Поэтому длина пассажирского поезда равна 1000 − 600 = 400м."
"Отвеет: 400м.")



@dp.message_handler(commands=['numrus'])
async def start_command(message: types.Message):
    # Создание кнопки, открывающей список
    button_text = 'Открыть список задач по русскому языку'
    menu_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    menu_markup.add(types.KeyboardButton(button_text))

    # Отправка сообщения с кнопкой
    await message.answer("Нажмите на кнопку, чтобы открыть список.", reply_markup=menu_markup)


# Обработка нажатия на кнопку
@dp.message_handler(lambda message: message.text == 'Открыть список задач по русскому языку')
async def open_list_handler(message: types.Message, state: FSMContext):
    # Создание списка пунктов
    items = [
        '/rusnumber1',
        '/rusnumber2',
        '/rusnumber3',
        '/rusnumber4',
        '/rusnumber5'
    ]

    # Формирование сообщения со списком
    list_message = "Список:\n"
    for item in items:
        list_message += f"- {item}\n"

    # Отправка сообщения со списком
    await message.answer(list_message)


@dp.message_handler(commands=['rusnumber1'])
async def start_handler(message: types.Message):
                    """Ловец (обработчик сообщений)"""
                    await message.answer(
                        "Укажите варианты ответов, в которых верно выделена буква, обозначающая ударный "
                        "гласный звук. Запишите номера ответов.озлОбить, отозвАлась, нАчавшись, локтЯ, принЯвшись"
                        "Нажмите /rusans1, Чтобы увидеть объяснение и ответ.Нажмите /rusumber2, чтобы перейти к следущему номеру.")

@dp.message_handler(commands=['rusnumber2'])
async def start_handler(message: types.Message):
                        """Ловец (обработчик сообщений)"""
                        await message.answer(
                            "Отредактируйте предложение: исправьте лексическую ошибку, заменив неверно употреблённое слово."
                            " Запишите подобранное слово, соблюдая нормы современного русского литературного языка."
"Хороший руководитель, без всякого сомнения, заботится о своих подчинённых и стремится показывать им образец во всём."
                            "Нажмите /rusans2, Чтобы увидеть объяснение и ответ.Нажмите /rusnumber3, чтобы перейти к следущему номеру")

@dp.message_handler(commands=['rusnumber3'])
async def start_handler(message: types.Message):
                            """Ловец (обработчик сообщений)"""
                            await message.answer("Расставьте все знаки препинания: укажите цифру(-ы), на месте которой(-ых) "
                    "в предложении должна(-ы) стоять запятая(-ые).Не растерявшийся и в этой ситуации Остап (1) уклонился вправо"
                                " (2) отыскивая глазами лодку (3) с сидящим в ней (4) верным Ипполитом Матвеевичем."
                                "Нажмите /rusans3, Чтобы увидеть объяснение и ответ.Нажмите /rusnumber4, чтобы перейти к следущему номеру")

@dp.message_handler(commands=['rusnumber4'])
async def start_handler(message: types.Message):
                                """Ловец (обработчик сообщений)"""
                                await message.answer("Расставьте знаки препинания: укажите цифру(-ы), на месте которой(-ых) в"
        " предложении должна(-ы) стоять запятая(-ые).Неподалёку находилось поместье (1) владельцы (2) которого (3) мало что заслужили, кроме худой о себе славы по округе (4) где их не любили (5) несмотря на то что (6) никто уже даже не мог сказать (7) из-за чего (8) именно появилась такая ненависть."
                                    "Нажмите /rusans4, Чтобы увидеть объяснение и ответ.Нажмите /rusnumber5, чтобы перейти к следущему номеру")

@dp.message_handler(commands=['rusnumber5'])
async def start_handler(message: types.Message):
                                    """Ловец (обработчик сообщений)"""
                                    await message.answer("Укажите все цифры, на месте которых пишется одна буква Н."
"Ю(1)ая красавица смущё(2)о улыбнулась и выронила золочё(3)ую пудре(4)ицу из рук."
                                        "Нажмите /rusans5, Чтобы увидеть объяснение и ответ.Нажмите /menu для перехода к списку предметов.")

@dp.message_handler(commands=['rusans1'])
async def start_handler(message: types.Message):
              """Ловец (обработчик сообщений)"""
              await message.answer(
                        "Расставим ударения: озлОбить, отозвалАсь, начАвшись, лОктя, принЯвшись.Ответ: 15.")

@dp.message_handler(commands=['rusans2'])
async def start_handler(message: types.Message):
                  """Ловец (обработчик сообщений)"""
                  await message.answer("Хороший руководитель, без всякого сомнения, заботится о своих подчинённых и стремится показывать им образец во всём."
"Пояснение: Приведём верное написание:Хороший руководитель, без всякого сомнения, заботится о своих подчинённых и стремится "
                                       "показывать им пример во всём.Ошибка заключалась в неверном употреблении фразеологизма.")

@dp.message_handler(commands=['rusans3'])
async def start_handler(message: types.Message):
              """Ловец (обработчик сообщений)"""
              await message.answer(
"запятая выделяет деепричастный оборот «отыскивая глазами лодку с сидящим в ней верным Ипполитом Матвеевичем»."
"Ответ: 2.")

@dp.message_handler(commands=['rusans4'])
async def start_handler(message: types.Message):
                  """Ловец (обработчик сообщений)"""
                  await message.answer(
 "1)запятая на границе частей в сложноподчинённом предложении: отделяет главную часть «Неподалёку находилось поместье» "
 "от придаточной «владельцы которого мало что заслужили, кроме худой о себе славы по округе»"
"4), 5), 7) отделяют придаточные части. Ответ: 1457.")

@dp.message_handler(commands=['rusans5'])
async def start_handler(message: types.Message):
                      """Ловец (обработчик сообщений)"""
                      await message.answer(
                          "ЮН(1)ая красавица смущёНН(2)о улыбнулась и выронила золочёН(3)ую пудреН(4)ицу из рук. Ответ: 134.")

@dp.message_handler(commands=['numinfo'])
async def start_command(message: types.Message):
                    # Создание кнопки, открывающей список
                    button_text = 'Открыть список задач по информатике'
                    menu_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                    menu_markup.add(types.KeyboardButton(button_text))

                    # Отправка сообщения с кнопкой
                    await message.answer("Нажмите на кнопку, чтобы открыть список.", reply_markup=menu_markup)

                # Обработка нажатия на кнопку
@dp.message_handler(lambda message: message.text == 'Открыть список задач по информатике')
async def open_list_handler(message: types.Message, state: FSMContext):                    # Создание списка пунктов
                    items = [
                        '/infonumber1',
                        '/infonumber2',
                        '/infonumber3',
                        '/infonumber4',
                        '/infonumber5'
                    ]

                    # Формирование сообщения со списком
                    list_message = "Список:\n"
                    for item in items:
                        list_message += f"- {item}\n"

                    # Отправка сообщения со списком
                    await message.answer(list_message)

@dp.message_handler(commands=['infonumber1'])
async def start_handler(message: types.Message):
                    """Ловец (обработчик сообщений)"""
                    await message.answer(
                        "По каналу связи передаются сообщения, содержащие только семь букв: А, Б, В, Г, Й, К, Л. "
                        "Для передачи используется двоичный код, удовлетворяющий условию Фано. Кодовые слова для некоторых "
                        "букв известны: Б— 00, Г— 010, К— 101. Какое наименьшее количество "
                        "двоичных знаков потребуется для кодирования слова БАЛАЛАЙКА?"
"Примечание. Условие Фано означает, что ни одно кодовое слово не является началом другого кодового слова."
  "Нажмите /infoans1, Чтобы увидеть объяснение и ответ.Нажмите /infonumber2, чтобы перейти к следущему номеру")

@dp.message_handler(commands=['infonumber2'])
async def start_handler(message: types.Message):
                        """Ловец (обработчик сообщений)"""
                        await message.answer(
                            "Автомат получает на вход пятизначное число. По этому числу строится новое число по "
                            "следующим правилам."

"1.Складываются отдельно первая, третья и пятая цифры, а также вторая и четвёртая цифры."
"2.Полученные два числа записываются друг за другом в порядке неубывания без разделителей."
"Пример. Исходное число: 63 179. Суммы: 6 + 1 + 9 = 16; 3 + 7 = 10. Результат: 1016."
"Укажите наименьшее число, при обработке которого автомат выдаёт результат 723."
                            "Нажмите /infoans2, Чтобы увидеть объяснение и ответ.Нажмите /infonumber3, чтобы перейти к следущему номеру")

@dp.message_handler(commands=['infonumber3'])
async def start_handler(message: types.Message):
                        """Ловец (обработчик сообщений)"""
                        await message.answer("Автоматическая фотокамера с 200 Кбайт видеопамяти производит растровые "
                                                 "изображения c фиксированным разрешением и 8-цветной палитрой. "
                                                 "Сколько цветов можно будет использовать в палитре, если "
                                                 "увеличить видеопамять до 400 Кбайт?"
"Нажмите /infoans3, Чтобы увидеть объяснение и ответ.Нажмите /infonumber4, чтобы перейти к следущему номеру")

@dp.message_handler(commands=['infonumber4'])
async def start_handler(message: types.Message):
                            """Ловец (обработчик сообщений)"""
                            await message.answer("Ольга составляет 5-буквенные коды из букв О, Л, Ь, Г, А."
                                                    " Каждую букву нужно использовать ровно 1 раз, "
                                                    "при этом Ь нельзя ставить первым и нельзя ставить после "
                                                    "гласной. Сколько различных кодов может составить Ольга?"
                                    "Нажмите /infoans4, Чтобы увидеть объяснение и ответ.Нажмите /infonumber5, чтобы перейти к следущему номеру")

@dp.message_handler(commands=['infonumber5'])
async def start_handler(message: types.Message):
                                    """Ловец (обработчик сообщений)"""
                                    await message.answer("Полина составляет 6-буквенные коды из"
            " букв П, О, Л, И, Н, А. Каждую букву нужно использовать ровно 1 раз, при этом нельзя ставить подряд две гласные"
                                " или две согласные.Сколько различных кодов может составить Полина?"
                        "Нажмите /infoans5, Чтобы увидеть объяснение и ответ.Нажмите /menu для перехода к списку предметов.")

@dp.message_handler(commands=['infoans1'])
async def start_handler(message: types.Message):
                    """Ловец (обработчик сообщений)"""
                    await message.answer(
"Букву А закодируем кодовым словом 11, поскольку буква А повторяется в слове БАЛАЛАЙКА 4 раза. Букву Л закодируем кодовым "
"словом 011, поскольку буква Л повторяется в слове БАЛАЛАЙКА 2 раза. Буквы Й и В закодируем кодовыми словами 1000 и 1001 "
"соответственно (заметим, что хотя буквы В нет в слове БАЛАЛАЙКА, но эта буква может передаваться по каналу связи, "
"следовательно, для нее должен быть определен код). Тогда наименьшее количество двоичных знаков, которые потребуются для "
"кодирования слова БАЛАЛАЙКА равно 2+2+3+2+3+2+4+3+2=23. Ответ: 23.")

@dp.message_handler(commands=['infoans2'])
async def start_handler(message: types.Message):
                        """Ловец (обработчик сообщений)"""
                        await message.answer(
"723 это либо 7 и 23, либо 72 и 3. Второго быть не может, так как числа должны быть записаны в порядке неубывания. "
"Значит, в результате первого шага автомата были получены числа 7 и 23. 23 нельзя получить суммой двух цифр, а значит, "
"что это сумма первой, третьей и пятой цифр числа, 7 же - сумма второй и четвёртой. Теперь представим эти числа в "
"виде сумм так, чтобы первые слагаемые получились как можно меньше.23 = 5 + 9 + 9, 7 = 0 + 7.В итоге получили число 50979.Ответ: 50979.")

@dp.message_handler(commands=['infoans3'])
async def start_handler(message: types.Message):
                    """Ловец (обработчик сообщений)"""
                    await message.answer(
"Заметим, что количество цветов находится по формуле N=2^i. Значит, если увеличить видеопамять до 400 Кбайт, "
"в палитре можно будет использовать 2^6=64. Ответ: 64")


@dp.message_handler(commands=['infoans4'])
async def start_handler(message: types.Message):
                        """Ловец (обработчик сообщений)"""
                        await message.answer(
"Пусть буква Г обозначает гласную, а буква С— согласную. Тогда в слове на любой позиции могут быть использованы гласные Г,"
" согласные С и конструкция СЬ, обозначающая какую-либо согласную с мягким знаком. Тогда, например, при использовании в"
" качестве согласной буквы в конструкции СЬ, буквы Л можно будет получить "
"4*3*2*1=24 варианта слов. Для оставшейся согласной буквы также получаем"
" 24 варианта. Таким образом, всего можно составить 2*24=48 различных кодов. Ответ: 48.")

@dp.message_handler(commands=['infoans5'])
async def start_handler(message: types.Message):
                            """Ловец (обработчик сообщений)"""
                            await message.answer(
"Заметим, что поскольку гласных и согласных поровну, слово может начинаться с как с согласной, так и с гласной."
"Также учтём то, что каждую букву нужно использовать только один раз.Поставим на первое место любую из трёх согласных."
" На второе— любую из трех гласных. На третье— любую из двух оставшихся согласных. На четвертое— любую из двух оставшихся"
" гласных. На пятое— одну оставшуюся согласную. На шестое- одну оставшуюся гласную. По правилу произведения, соответствующие"
" количества способов перемножаем. Учитывая, что на первое место можно поставить как согласную, так и гласную, "
"Полина может составить 2*3·*3*2*2*1*1=72 различных кода. Ответ: 72.")




if __name__ == '__main__':
    # Запуск бота
    from aiogram import executor

    executor.start_polling(dp, skip_updates=True)

