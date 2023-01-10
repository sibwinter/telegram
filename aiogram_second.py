from aiogram import Bot, Dispatcher, executor, types


# Вместо BOT TOKEN HERE нужно вставить токен вашего бота, полученный у @BotFather
API_TOKEN: str = '5579843922:AAHb9Q1IAAZIUtHHYdlepHh1fuPmqhpmgOA'

# Создаем объекты бота и диспетчера
bot: Bot = Bot(token=API_TOKEN)
dp: Dispatcher = Dispatcher(bot)


# Этот хэндлер будет срабатывать на команду "/start"
async def process_start_command(message: types.Message):
    await message.answer('Привет!\nМеня зовут Эхо-бот!\nНапиши мне что-нибудь или пришли картинку')


# Этот хэндлер будет срабатывать на команду "/help"
async def process_help_command(message: types.Message):
    await message.answer('Напиши мне что-нибудь или пришли картинку и в ответ я пришлю тебе твое сообщение')


# Этот хэндлер будет срабатывать на отправку фото
async def send_photo_echo(message: types.Message):
    await message.answer_photo(message.photo[0].file_id)


# Этот хэндлер будет срабатывать на любые ваши текстовые сообщения, кроме команд "/start" и "/help"
async def send_echo(message: types.Message):
    await message.reply(message.text)


# Этот хендлер будет срабатывать на отправку стикера
async def send_sticker_echo(message: types.Message):
    print(message)
    await message.answer_sticker(message.sticker.file_id)


# Регистрируем хэндлеры
dp.register_message_handler(process_start_command, commands='start')
dp.register_message_handler(process_help_command, commands='help')
dp.register_message_handler(send_photo_echo, content_types=['photo'])
dp.register_message_handler(send_sticker_echo, content_types=['sticker'])
dp.register_message_handler(send_echo)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)