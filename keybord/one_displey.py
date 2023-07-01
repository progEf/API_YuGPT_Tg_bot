from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


b1 = KeyboardButton('Вставить свою ссылку')
b2 = KeyboardButton('Посмотреть новости')

kb_client = ReplyKeyboardMarkup(resize_keyboard=True)
kb_client.add(b1).add(b2)

a2 = KeyboardButton('Вернуться обратно')
kb_client_1 = ReplyKeyboardMarkup(resize_keyboard=True)

kb_client_1.add(a2)
def kb_client_2(pars_rbc):
    c =  KeyboardButton(pars_rbc[0][0])
    c1 = KeyboardButton(pars_rbc[1][0])
    c2 = KeyboardButton(pars_rbc[2][0])
    c3 = KeyboardButton(pars_rbc[3][0])
    c4 = KeyboardButton(pars_rbc[4][0])
    c5 = KeyboardButton('Обновить')
    c6 = KeyboardButton('Вернуться')

    kb_client_2 = ReplyKeyboardMarkup(resize_keyboard=True)
    return kb_client_2.add(c).add(c1).add(c2).add(c3).add(c4).add(c5).add(c6)
