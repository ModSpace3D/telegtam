from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types.web_app_info import WebAppInfo


bot = Bot(token='6665502140:AAGcXW-ySaZ_CSW46URqgerr25Dcl1gWnEQ')
dp = Dispatcher(bot)

@dp.message_handler(commands='start')
async def start(message: types.Message):
    markupstart = types.ReplyKeyboardMarkup(resize_keyboard = True)
    btn1 = types.KeyboardButton('Личный кабинет 🏠')
    btn2 = types.KeyboardButton('Каталог 📚')
    markupstart.row(btn1, btn2)
    btn3 = types.KeyboardButton('Обратная связь 💬')
    btn4 = types.KeyboardButton('О нас ⚠️')
    markupstart.row(btn3, btn4)
    await  message.answer(f'Приветсвуем вас, {message.from_user.username}! В нашем боте вы сможете найти подходящие модели для себя или своей игры, а также выставить их на продажу.', parse_mode='html', reply_markup=markupstart)

@dp.message_handler(commands=['profile'])
async def profile(message: types.Message):
    markupprofile = types.ReplyKeyboardMarkup(resize_keyboard = True)
    btn1 = types.KeyboardButton('Главное меню 💎')
    btn2 = types.KeyboardButton('Каталог 📚')
    markupprofile.row(btn1, btn2)
    btn3 = types.KeyboardButton('Обратная связь 💬')
    btn4 =types.KeyboardButton('О нас ⚠️')
    markupprofile.row(btn3, btn4)
    await message.answer(f'Ваш ID {message.from_user.id} \nВаше имя: {message.from_user.first_name} \nВаш никнейм: {message.from_user.username}', parse_mode='html', reply_markup=markupprofile)

@dp.message_handler(commands=['help'])
async def help(message: types.Message):
    markuphelp = types.ReplyKeyboardMarkup(resize_keyboard = True)
    btn1 = types.KeyboardButton('Главное меню 💎')
    btn2 = types.KeyboardButton('Каталог 📚')
    markuphelp.row(btn1, btn2)
    btn3 = types.KeyboardButton('Личный кабинет 🏠')
    btn4 = types.KeyboardButton('О нас ⚠️')
    markuphelp.row(btn3, btn4)
    await message.answer(f'Если у тебя появились какие-то вопросы или предложения по технической части, писать <u>@god_gas</u>', parse_mode='html')
    await message.answer(f'По всем остальным вопросам и сотрудничеству, писать <u>@nnvjvsvsh</u>', parse_mode='html', reply_markup=markuphelp)

@dp.message_handler(commands=['info'])
async def info(message: types.Message):
    markupinfo = types.ReplyKeyboardMarkup(resize_keyboard = True)
    btn1 = types.KeyboardButton('Главное меню 💎')
    btn2 = types.KeyboardButton('Личный кабинет 🏠')
    markupinfo.row(btn1, btn2)
    btn3 = types.KeyboardButton('Обратная связь 💬')
    btn4 = types.KeyboardButton('Каталог 📚')
    markupinfo.row(btn3, btn4)
    await message.answer(f'Администраторов/Модераторов/Создателей только двое @god_gas и @nnvjvsvsh \nЕсли кто-то другой будет к вам обращаться, то это мошенники, не видитесь на обман!', parse_mode='html')
    await message.answer(f'Этот бот создан исключительно для того чтобы вы могли найти модели для себя или использовать их в своих целях, играх, приложениях и т.д.', parse_mode='html')
    await message.answer(f'Также у нас есть частный телеграмм-канал «Mod Space - новости» - https://t.me/+_NrXIhGBkhs3MTgy', parse_mode='html')
    await message.answer(f'Оплата производится перед публикацией модели в каталог. \nCтоимость публикации составляет 1/5 (одна пятая) от той суммы за которую вы хотите продавать свою модель. \nНапример: если вы планируете выставить за 1000 рублей свою модель, то стоимость публикации будет равна 200 рублей (1/5).\nМинимальная цена за слот 129 рублей. \nПроценты с продаж мы не берём.', parse_mode='html')
    await message.answer(f'Модели выкладываются только платно. Мы оцениваем труд каждого по заслугам! \nЕсли вы планируете выложить большое количество моделей (от 20 моделей), то цену можно обговорить. \nТакже присутствует сотрудничество и реклама для этого нужно написать Модераторам/Админам.', parse_mode='html', reply_markup=markupinfo)

@dp.message_handler(commands=['shop'])
async def shop(message: types.Message):
    markupshop = types.ReplyKeyboardMarkup(resize_keyboard = True)
    btn1 = types.KeyboardButton('Главное меню 💎')
    btn2 = types.KeyboardButton('Личный кабинет 🏠')
    markupshop.row(btn1, btn2)
    markupshop.add(types.KeyboardButton('Открыть каталог', web_app=WebAppInfo(url='https://modspace3d.github.io/telegtam/')))
    await message.answer('Каталог нашего магазина', reply_markup=markupshop)

@dp.message_handler(content_types=['text'])
async def text(message: types.Message):
    if message.chat.type == 'private':
        if message.text == 'Личный кабинет 🏠':
            markupprofile = types.ReplyKeyboardMarkup(resize_keyboard = True)
            btn1 = types.KeyboardButton('Главное меню 💎')
            btn2 = types.KeyboardButton('Каталог 📚')
            markupprofile.row(btn1, btn2)
            btn3 = types.KeyboardButton('Обратная связь 💬')
            btn4 = types.KeyboardButton('О нас ⚠️')
            markupprofile.row(btn3, btn4)
            await message.answer(f'Ваш ID {message.from_user.id} \nВаше имя: {message.from_user.first_name} \nВаш никнейм: {message.from_user.username}', parse_mode='html', reply_markup=markupprofile)
        elif message.text == 'Главное меню 💎':
            markupstart = types.ReplyKeyboardMarkup(resize_keyboard = True)
            btn1 = types.KeyboardButton('Личный кабинет 🏠')
            btn2 = types.KeyboardButton('Каталог 📚')
            markupstart.row(btn1, btn2)
            btn3 = types.KeyboardButton('Обратная связь 💬')
            btn4 = types.KeyboardButton('О нас ⚠️')
            markupstart.row(btn3, btn4)
            await message.answer(f'Приветствуем вас, {message.from_user.username}! В нашем боте вы сможете найти подходящие модели для себя или своей игры, а также выставить их на продажу.', parse_mode='html', reply_markup=markupstart)
        elif message.text == 'Обратная связь 💬':
            markuphelp = types.ReplyKeyboardMarkup(resize_keyboard = True)
            btn1 = types.KeyboardButton('Главное меню 💎')
            btn2 = types.KeyboardButton('Каталог 📚')
            markuphelp.row(btn1, btn2)
            btn3 = types.KeyboardButton('Личный кабинет 🏠')
            btn4 = types.KeyboardButton('О нас ⚠️')
            markuphelp.row(btn3, btn4)
            await message.answer(f'Если у тебя появились какие-то вопросы или предложения по технической части, писать <u>@god_gas</u>', parse_mode='html')
            await message.answer(f'По всем остальным вопросам и сотрудничеству, писать <u>@nnvjvsvsh</u>',parse_mode='html', reply_markup=markuphelp)
        elif message.text == 'О нас ⚠️':
            markupinfo = types.ReplyKeyboardMarkup(resize_keyboard = True)
            btn1 = types.KeyboardButton('Главное меню 💎')
            btn2 = types.KeyboardButton('Личный кабинет 🏠')
            markupinfo.row(btn1, btn2)
            btn3 = types.KeyboardButton('Обратная связь 💬')
            btn4 = types.KeyboardButton('Каталог 📚')
            markupinfo.row(btn3, btn4)
            await message.answer(f'Администраторов/Модераторов/Создателей только двое @god_gas и @nnvjvsvsh \nЕсли кто-то другой будет к вам обращаться, то это мошенники, не видитесь на обман!', parse_mode='html')
            await message.answer(f'Этот бот создан исключительно для того чтобы вы могли найти модели для себя или использовать их в своих целях, играх, приложениях и т.д.', parse_mode='html')
            await message.answer(f'Также у нас есть частный телеграмм-канал «Mod Space - новости» - https://t.me/+_NrXIhGBkhs3MTgy', parse_mode='html')
            await message.answer(f'Оплата производится перед публикацией модели в каталог. \nCтоимость публикации составляет 1/5 (одна пятая) от той суммы за которую вы хотите продавать свою модель. \nНапример: если вы планируете выставить за 1000 рублей свою модель, то стоимость публикации будет равна 200 рублей (1/5). \nМинимальная цена за слот 129 рублей. \nПроценты с продаж мы не берём.', parse_mode='html')
            await message.answer(f'Модели выкладываются только платно. Мы оцениваем труд каждого по заслугам! \nЕсли вы планируете выложить большое количество моделей (от 20 моделей), то цену можно обговорить. \nТакже присутствует сотрудничество и реклама для этого нужно написать Модераторам/Админам.', parse_mode='html', reply_markup=markupinfo)
        elif message.text == 'Каталог 📚':
            markupshop = types.ReplyKeyboardMarkup(resize_keyboard = True)
            btn1 = types.KeyboardButton('Главное меню 💎')
            btn2 = types.KeyboardButton('Личный кабинет 🏠')
            markupshop.row(btn1, btn2)
            markupshop.add(types.KeyboardButton('Открыть каталог', web_app=WebAppInfo(url='https://modspace3d.github.io/telegtam/')))
            await message.answer('Каталог нашего магазина', reply_markup=markupshop)



if __name__ == '__main__':
    executor.start_polling(dp)