import crud_functions
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from humanfriendly.terminal import message

api = ''
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

class RegistrationState(StatesGroup):
    username = State()
    email = State()
    age = State()
    balance = State()

products = crud_functions.get_all_products()

@dp.message_handler(commands=['start'])
async def start_message(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(types.KeyboardButton('Рассчитать'))
    keyboard.add(types.KeyboardButton('Информация'))
    keyboard.add(types.KeyboardButton('Купить'))
    keyboard.add(types.KeyboardButton('Регистрация'))
    await message.answer('Привет!\nЯ бот помогаюший твоему здоровию!', reply_markup=keyboard)

@dp.message_handler(text=['Рассчитать'])
async def set_age(message):
    await message.answer('Введите свой возраст:')
    await UserState.age.set()

@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(age=message.text)
    await message.answer('Введите свой рост:')
    await UserState.growth.set()

@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth=message.text)
    await message.answer('Введите свой вес:')
    await UserState.weight.set()

@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight=message.text)
    data = await state.get_data()
    calories = 10 * int(data['weight']) + 6.25 * int(data['growth']) - 5 * int(data['age']) + 5
    await message.answer(f'Ваша норма калорий {calories}')
    await state.finish()

@dp.message_handler(text=['Купить'])
async def get_buying_list(message):
    products = crud_functions.get_all_products()
    for product in products:
        await message.answer(f'Название: {product["name"]} | Описание: {product["description"]} | Цена: {product["price"]}')
        await message.answer_photo(open(f'{product["name"]}.jpg', 'rb'))

    keyboard = types.InlineKeyboardMarkup()
    for product in products:
        keyboard.add(types.InlineKeyboardButton(text=product['name'], callback_data=f'product_buying_{product["name"]}'))

    await message.answer('Выберите продукт для покупки:', reply_markup=keyboard)

@dp.callback_query_handler(text_contains='product_buying_')
async def send_confirm_message(call):
    product_name = call.data.split('_')[2]
    await call.message.answer('Вы успешно приобрели продукт!')

@dp.message_handler(text=['Регистрация'])
async def sing_up(message):
    await message.answer('Введите имя пользователя (только латинский алфавит):')
    await RegistrationState.username.set()

@dp.message_handler(state=RegistrationState.username)
async def set_username(message, state):
    if not crud_functions.is_included(message.text):
        await state.update_data(username=message.text)
        await message.answer('Введите свой email:')
        await RegistrationState.email.set()
    else:
        await message.answer('Пользователь существует, введите другое имя')
        await RegistrationState.username.set()

@dp.message_handler(state=RegistrationState.email)
async def set_email(message, state):
    await state.update_data(email=message.text)
    await message.answer('Введите свой возраст:')
    await RegistrationState.age.set()

@dp.message_handler(state=RegistrationState.age)
async def set_age(message, state):
    await state.update_data(age=message.text)
    data = await state.get_data()
    crud_functions.add_user(data['username'], data['email'], data['age'])
    await message.answer('Регистрация прошла успешно!')
    await state.finish()

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
