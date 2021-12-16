from aiogram import types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ParseMode

async def main_admin_panel(message : types.Message):
    markup = InlineKeyboardMarkup()
    but1 = InlineKeyboardButton('Добавить админа', callback_data='fake_admin')
    but2 = InlineKeyboardButton('Редактировать каталог услуг', callback_data='red_cat')
    but3 = InlineKeyboardButton('Просмотр ближайших записей', callback_data='letmesee_order')
    but4 = InlineKeyboardButton('Редактировать прайс', callback_data="edi_price")
    markup.row(but1).row(but3).row(but2).row(but4)
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




# ********************************************УДАЛЕНИЕ\ДОБАВЛЕНИЕ\РЕДАКТИРОВАНИЕ ПРАЙСА


async def edit_price_panel(callback : types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    but1 = InlineKeyboardButton('Добавить запись в прайс', callback_data='edit_main_add')
    but2 = InlineKeyboardButton('Поменять цену', callback_data='edit_main_cha')
    but3 = InlineKeyboardButton('Удалить запись из прайса', callback_data='edit_main_del')
    markup.row(but2).row(but1).row(but3)
    await callback.message.edit_text('Вам требуется? 💁🏼‍♀', reply_markup=markup)
    await callback.answer()


# ****************************
# ****************************
# ****************************
async def edit_main_panel_price(callback : types.CallbackQuery, v1, v2):
    markup_main_panel = InlineKeyboardMarkup()
    but1 = InlineKeyboardButton("Косметология", callback_data=f"edit_cos_{v2}")
    but2 = InlineKeyboardButton("Парикмахерская", callback_data=f"edit_bar_{v2}")
    but3 = InlineKeyboardButton("Маникюр", callback_data=f"make_{v2}_man")
    but4 = InlineKeyboardButton("Педикюр", callback_data=f"make_{v2}_ped")
    but5 = InlineKeyboardButton("Назад", callback_data='edit_back_1')

    markup_main_panel.row(but1, but2).row(but3, but4).row(but5)
    await callback.message.edit_text(f'Выберите категорию {v1}', reply_markup=markup_main_panel, parse_mode=ParseMode.MARKDOWN)
    await callback.answer()

# Подкаталоги
async def edit_main_panel_bar_1(callback : types.CallbackQuery, v1):
    markup_main_panel_bar = InlineKeyboardMarkup()


    butt1 = InlineKeyboardButton('Женский зал', callback_data=f'edit_hall_w_{v1}')
    butt2 = InlineKeyboardButton('Мужcкой + детский', callback_data=f'make_{v1}_bar_m')
    butt304 = InlineKeyboardButton('Назад', callback_data=f'edit_back_2_{v1}')
    markup_main_panel_bar.row(butt1, butt2).add(butt304)
    await callback.message.edit_text('Выберите необходимый зал 💇🏼‍♀️', reply_markup=markup_main_panel_bar)
    await callback.answer()

async def edit_main_panel_bar_w(callback : types.CallbackQuery, v1):
    markup_main_panel_bar_women = InlineKeyboardMarkup()
    butt3 = InlineKeyboardButton('Стрижки', callback_data=f'make_{v1}_cut')
    butt4 = InlineKeyboardButton('Укладки-прически', callback_data=f'make_{v1}_bar_laying')
    butt5 = InlineKeyboardButton('Наращивание-окрашивание', callback_data=f'make_{v1}_bar_coloring')
    butt6 = InlineKeyboardButton('Уход за волосами', callback_data=f'make_{v1}_bar_care')
    butt7 = InlineKeyboardButton('Назад', callback_data=f"edit_bar_{v1}")
    markup_main_panel_bar_women.row(butt3, butt4).row(butt6, butt5).add(butt7)
    await callback.message.edit_text('Выберите подкатегорию ️', reply_markup=markup_main_panel_bar_women, parse_mode=ParseMode.MARKDOWN)
    await callback.answer()

async def edit_main_panel_cos(callback : types.CallbackQuery, v1):
    markup_main_panel_cos = InlineKeyboardMarkup()
    butt8 = InlineKeyboardButton('Брови', callback_data=f'make_{v1}_cos_brow')
    butt9 = InlineKeyboardButton('Ресницы', callback_data=f'make_{v1}_cos_lash')
    butt10 = InlineKeyboardButton('Другое', callback_data=f'make_{v1}_cos_ear')
    butt11 = InlineKeyboardButton('Лаз. эпиляция', callback_data=f'make_{v1}_cos_epil')
    butt12 = InlineKeyboardButton('Депиляция воском', callback_data=f'make_{v1}_cos_depil')
    butt13 = InlineKeyboardButton('Уход за кожей', callback_data=f'make_{v1}_cos_face')
    butt14 = InlineKeyboardButton('Назад', callback_data=f'edit_back_2_{v1}')
    markup_main_panel_cos.row(butt8, butt9).row(butt12, butt13).row(butt11, butt10).add(butt14)
    await callback.message.edit_text('Выберите нужную подкатегорию', reply_markup=markup_main_panel_cos, parse_mode=ParseMode.MARKDOWN)
    await callback.answer()

