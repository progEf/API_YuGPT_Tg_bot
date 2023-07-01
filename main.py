from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher, FSMContext
from aiogram.utils import executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, callback_query
from aiogram.dispatcher.filters import Text
import schedule
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Command

from keybord.one_displey import kb_client, kb_client_1, kb_client_2
from parsing.API_PARS import request_parsing
from parsing.parsing_RBK import pars_rbc

storage = MemoryStorage()
TOKEN = 'TOKEN'
bot = Bot(token=TOKEN)
dp: Dispatcher = Dispatcher(bot, storage=storage)


async def on_startup(_):
    print('Бот вышел онлайн')


class MenuState(StatesGroup):
    MAIN_MENU = State()  # Главное меню
    SUB_MENU = State()  # Подменю


@dp.message_handler(commands=['start', 'help'])
async def comand_start(message: types.message):
    await  bot.send_message(message.from_user.id, 'Привет', reply_markup=kb_client)


@dp.message_handler(Text(equals='Вставить свою ссылку'))
async def cor12t(message: types.message, state: FSMContext):
    await  bot.send_message(message.from_user.id, 'Вставьте ссылку на статью', reply_markup=kb_client_1)


@dp.message_handler(Text(equals='Вернуться обратно'))
async def cor1sda2t(message: types.message, state: FSMContext):
    if message.text == 'Вернуться обратно':
        await  bot.send_message(message.from_user.id, 'Вы перешли на основное меню', reply_markup=kb_client)


@dp.message_handler(Text(equals='Посмотреть новости'))
async def cor1sda2t(message: types.message, state: FSMContext):
        await  bot.send_message(message.from_user.id, 'Новости', reply_markup=kb_client_2(pars_rbc()))
        await  bot.send_message(message.from_user.id, pars_rbc()[0][0])
        await  bot.send_message(message.from_user.id, pars_rbc()[1][0])
        await  bot.send_message(message.from_user.id, pars_rbc()[2][0])
        await  bot.send_message(message.from_user.id, pars_rbc()[3][0])
        await  bot.send_message(message.from_user.id, pars_rbc()[4][0])
@dp.message_handler(Text(equals=pars_rbc()[0][0]))
async def cor1sda2t(message: types.message, state: FSMContext):


    await  bot.send_message(message.from_user.id, pars_rbc()[0][1], reply_markup=kb_client_2(pars_rbc()) )


@dp.message_handler(Text(equals='Обновить'))
async def cor1sda2t(message: types.message, state: FSMContext):
    pars_rbc()
    await  bot.send_message(message.from_user.id, 'agsa', reply_markup=kb_client_2(pars_rbc()))
#Вернуться
@dp.message_handler(Text(equals='Вернуться'))
async def cor1sda2t(message: types.message, state: FSMContext):
    await  bot.send_message(message.from_user.id, 'Вы перешли на основное меню', reply_markup=kb_client)

@dp.message_handler()
async def handle_message(message: types.Message, state: FSMContext):
    pars_rbc()

    user_input = message.text  # Получаем текст, который написал пользователь

    if user_input == pars_rbc()[0][0]:
        a = request_parsing(pars_rbc()[0][1])
        s = str()
        for i in a:
            s += i + '\n\n'
        await message.answer(s)
        print('asfasgasfdasf')
    elif user_input == pars_rbc()[1][0]:
        a = request_parsing(pars_rbc()[1][1])
        s = str()
        for i in a:
            s += i + '\n\n'
        await message.answer(s)
    elif user_input == pars_rbc()[2][0]:
        a = request_parsing(pars_rbc()[2][1])
        s = str()
        for i in a:
            s += i + '\n\n'
        await message.answer(s)
    elif user_input == pars_rbc()[3][0]:
        a = request_parsing(pars_rbc()[3][1])
        s = str()
        for i in a:
            s += i + '\n\n'
        await message.answer(s)
    elif user_input == pars_rbc()[4][0]:
        a = request_parsing(pars_rbc()[4][1])
        s = str()
        for i in a:
            s += i + '\n\n'
        await message.answer(s)
    elif user_input.find('http') != -1: #and pars_rbc()[0][1] != message.text and pars_rbc()[1][1] != message.text and \
            #pars_rbc()[2][1] != message.text and pars_rbc()[3][1] != message.text and pars_rbc()[4][1] != message.text:
        a = request_parsing(user_input)
        s = str()
        for i in a:
            s += i + '\n\n'
        await message.answer(s)




executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
