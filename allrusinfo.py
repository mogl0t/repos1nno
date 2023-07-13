@dp.message_handler(commands=['numrus'])
async def start_command(message: types.Message):
                    # Создание кнопки, открывающей список
                    button_text = 'Открыть список задач по русскоиу языку'
                    menu_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                    menu_markup.add(types.KeyboardButton(button_text))

                    # Отправка сообщения с кнопкой
                    await message.answer("Нажмите на кнопку, чтобы открыть список.", reply_markup=menu_markup)

                # Обработка нажатия на кнопку
@dp.message_handler(lambda message: message.text == 'Открыть список задач по русскому языку')
async def open_list_handler(message: types.Message, state: FSMContext):                    # Создание списка пунктов
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