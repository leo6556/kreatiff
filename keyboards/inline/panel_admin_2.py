from aiogram import types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ParseMode

async def main_admin_panel(message : types.Message):
    markup = InlineKeyboardMarkup()
    but1 = InlineKeyboardButton('Добавить админа', callback_data='fake_admin')
    but2 = InlineKeyboardButton('Редактировать каталог услуг', callback_data='red_cat')
    but3 = InlineKeyboardButton('Просмотр ближайших записей', callback_data='letmesee_order')
    markup.row(but1).row(but3).row(but2)
    await message.answer('Выберите нужную функцию ⚙️', reply_markup=markup)

async def red_price_panel(callback : types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    but1 = InlineKeyboardButton('Добавить услугу', callback_data='redact_add')
    but2 = InlineKeyboardButton('Удалить услугу', callback_data='redact_del')
    markup.row(but1, but2)
    await callback.message.edit_text('Вам требуется? 💁🏼‍♀', reply_markup=markup)
    await callback.answer()



async def main_panel_for_edit(callback : types.CallbackQuery, cat, cat2):
    markup = InlineKeyboardMarkup()

    but1 = InlineKeyboardButton('Уход за кожей лица', callback_data=f'{cat}_order_face')
    but2 = InlineKeyboardButton('Брови', callback_data=f'{cat}_order_brow')
    but3 = InlineKeyboardButton('Ресницы', callback_data=f'{cat}_order_lash')
    but4 = InlineKeyboardButton('Ман- и педикюр', callback_data=f'{cat}_order_man')
    but5 = InlineKeyboardButton('Депиляция', callback_data=f'{cat}_order_depil')
    but6 = InlineKeyboardButton('Парикмахерская', callback_data=f'{cat}_order_bar')
    but7 = InlineKeyboardButton('Уход за волосами', callback_data=f'{cat}_order_care')
    but8 = InlineKeyboardButton('Другое', callback_data=f'{cat}_order_else')
    but9 = InlineKeyboardButton('назад', callback_data='redact_aa')

    markup.row(but1, but7).row(but3, but2).row(but6, but5).row(but4, but8).row(but9)
    await callback.message.edit_text(f'{cat2} 💆🏼‍♀️', reply_markup=markup)
    await callback.answer()



async def end_q():
    markup = InlineKeyboardMarkup()
    but1 = InlineKeyboardButton('Добавить', callback_data='dothisshit')
    but2 = InlineKeyboardButton('Отменить', callback_data="donotdo")
    markup.row(but1, but2)
    return markup

async def markup_for_warning(i):
    markup = InlineKeyboardMarkup()
    if i[7] == '0':
        but_1 = InlineKeyboardButton('Отправить надпоминание', callback_data=f'warn_{i[0]}_{i[1]}_{i[3]}')
    else:
        but_1 = InlineKeyboardButton('Отправить надпоминание (повторно)', callback_data=f'warn_{i[0]}_{i[1]}_{i[3]}')
    return markup.row(but_1)

