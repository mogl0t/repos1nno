import dp as dp
from aiogram import Bot, Dispatcher, types
import requests
from config import TOKEN

import logging
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext


bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

logging.basicConfig(level=logging.INFO)

bot = Bot(token="6356202859:AAF2qcAcExjnD59LeE5LfbP_2kN6SrXNHxc")
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)





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
async def open_list_handler(message: types.Message, state: FSMContext):
    # Создание списка пунктов
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
    await message.answer("Автоматическая фотокамера с 200 Кбайт видеопамяти производит растровые изображения c фиксированным "
"разрешением и 8-цветной палитрой. Сколько цветов можно будет использовать в палитре, если увеличить видеопамять до 400 Кбайт?"
                "Нажмите /infoans1, Чтобы увидеть объяснение и ответ.Нажмите /infonumber2, чтобы перейти к следущему номеру.")

@dp.message_handler(commands=['infonumber2'])
async def start_handler(message: types.Message):
    """Ловец (обработчик сообщений)"""
    await message.answer("Ольга составляет 5-буквенные коды из букв О, Л, Ь, Г, А. Каждую букву нужно использовать ровно 1 раз,"
            " при этом Ь нельзя ставить первым и нельзя ставить после гласной. Сколько различных кодов может составить Ольга?"
                "Нажмите /infoans2, Чтобы увидеть объяснение и ответ.Нажмите /infonumber3, чтобы перейти к следущему номеру.")

    @dp.message_handler(commands=['infonumber3'])
    async def start_handler(message: types.Message):
        """Ловец (обработчик сообщений)"""
        await message.answer("По каналу связи передаются сообщения, содержащие только семь букв: А, Б, В, Г, Й, К, Л."
" Для передачи используется двоичный код, удовлетворяющий условию Фано. Кодовые слова для некоторых букв известны: "
        "Б— 00, Г— 010, К— 101. Какое наименьшее количество двоичных знаков потребуется для кодирования слова БАЛАЛАЙКА?"
   "Примечание. Условие Фано означает, что ни одно кодовое слово не является началом другого кодового слова."
            "Нажмите /infoans3, Чтобы увидеть объяснение и ответ.Нажмите /infonumber4, чтобы перейти к следущему номеру.")

        @dp.message_handler(commands=['infonumber4'])
        async def start_handler(message: types.Message):
            """Ловец (обработчик сообщений)"""
            await message.answer(
"Для проведения эксперимента записывается звуковой фрагмент в формате квадро (четырёхканальная запись) с частотой дискретизации"
" 32 кГц и 32-битным разрешением. Результаты записываются в файл, сжатие данных не производится; дополнительно в файл "
"записывается служебная информация, необходимая для эксперимента, размер полученного файла 97 Мбайт. Затем производится "
"повторная запись этого же фрагмента в формате моно (одноканальная запись) с частотой дискретизации 16 кГц и 16-битным "
"разрешением. Результаты тоже записываются в файл без сжатия и со служебной информацией, размер полученного файла 7 Мбайт. "
"Объём служебной информации в обоих случаях одинаков. Укажите этот объём в мегабайтах. В ответе укажите только число "
"(количество Мбайт), единицу измерения указывать не надо."
                "Нажмите /infoans4, Чтобы увидеть объяснение и ответ.Нажмите /infonumber5, чтобы перейти к следущему номеру.")

            @dp.message_handler(commands=['infonumber5'])
            async def start_handler(message: types.Message):
                """Ловец (обработчик сообщений)"""
                await message.answer(
                    "Автомат получает на вход четырёхзначное число. По этому числу строится новое число по следующим правилам."
 "1.Складываются отдельно первая и вторая цифры, вторая и третья цифры, а также третья и четвёртая цифры."
"2.Из полученных трёх чисел выбираются два наибольших и записываются друг за другом в порядке неубывания без разделителей."
"Пример. Исходное число: 9575. Суммы: 9 + 5 = 14; 5 + 7 = 12; 7 + 5 = 12. Наибольшие суммы: 14, 12. Результат: 1214."
"Укажите наименьшее число, при обработке которого автомат выдаёт результат 1418."
                    "Нажмите /infoans5, Чтобы увидеть объяснение и ответ.Нажмите /menu для перехода к списку предметов.")