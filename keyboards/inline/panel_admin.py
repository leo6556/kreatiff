# from aiogram import types
# from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ParseMode
#
# async def main_admin_panel(message : types.Message):
#     markup = InlineKeyboardMarkup()
#     but1 = InlineKeyboardButton('Добавить админа', callback_data='re_admin')
#     but2 = InlineKeyboardButton('Редактировать каталог услуг', callback_data='re_cat')
#     but3 = InlineKeyboardButton('Редактировать прайс', callback_data='re_price')
#     markup.row(but1).row(but2).row(but3)
#     await message.answer('Выберите нужную функцию', reply_markup=markup)
#
# async def red_price_panel(callback : types.CallbackQuery):
#     markup = InlineKeyboardMarkup()
#     but1 = InlineKeyboardButton('Добавить', callback_data='red_add')
#     but2 = InlineKeyboardButton('Удалить', callback_data='red_del')
#     markup.row(but1, but2)
#     await callback.message.edit_text('Что нужно?', reply_markup=markup)
#
# async def red_price_round_1(callback : types.CallbackQuery, cat):
#     markup_main_panel = InlineKeyboardMarkup()
#     but1 = InlineKeyboardButton("Косметология", callback_data=f"{cat}_cos")
#     but2 = InlineKeyboardButton("Парикмахерская", callback_data=f"{cat}_bar")
#     but3 = InlineKeyboardButton("Маникюр", callback_data=f"{cat}_use_man")
#     but4 = InlineKeyboardButton("Педикюр", callback_data=f"{cat}_use_ped")
#     markup_main_panel.row(but1, but2).row(but3, but4)
#     await callback.message.edit_text('В какую категорию хотитке добавить?', reply_markup=markup_main_panel)
#
#
# async def red_price_round_2_bar(callback : types.CallbackQuery, cat):
#     markup_main_panel_bar = InlineKeyboardMarkup()
#     butt1 = InlineKeyboardButton('Женский зал', callback_data=f"{cat}_use_hall_w")
#     butt2 = InlineKeyboardButton('Мужcкой + детский', callback_data=f"{cat}_use_bar_m")
#     butt304 = InlineKeyboardButton('Назад', callback_data=f'{cat}_back_to_round_1')
#     markup_main_panel_bar.row(butt1, butt2).add(butt304)
#     await callback.message.edit_text('Выберите необходимый зал 💇🏼‍♀️', reply_markup=markup_main_panel_bar)
#     await callback.answer()
#
#
# async def red_price_round_3_bar(callback : types.CallbackQuery, cat):
#     markup_main_panel_bar_women = InlineKeyboardMarkup()
#     butt3 = InlineKeyboardButton('Стрижки', callback_data=f'{cat}_use_cut')
#     butt4 = InlineKeyboardButton('Укладки-прически', callback_data=f'{cat}_use_laying')
#     butt5 = InlineKeyboardButton('Наращивание-окрашивание', callback_data=f'{cat}_use_coloring')
#     butt6 = InlineKeyboardButton('Уход за волосами', callback_data=f'{cat}_use_care')
#     butt7 = InlineKeyboardButton('Назад', callback_data=f'{cat}_back_to_round_1')
#     markup_main_panel_bar_women.row(butt3, butt4).row(butt6, butt5).add(butt7)
#     await callback.message.edit_text('Выберите подкатегорию 💆🏼‍♀️', reply_markup=markup_main_panel_bar_women, parse_mode=ParseMode.MARKDOWN)
#     await callback.answer()
#
#
# async def red_price_round_2_cos(callback : types.CallbackQuery, cat):
#     markup_main_panel_cos = InlineKeyboardMarkup()
#     butt8 = InlineKeyboardButton('Брови', callback_data=f'{cat}_use_brow')
#     butt9 = InlineKeyboardButton('Ресницы', callback_data=f'{cat}_use_lash')
#     butt10 = InlineKeyboardButton('Другое', callback_data=f'{cat}_use_ear')
#     butt11 = InlineKeyboardButton('Лаз. эпиляция', callback_data=f'{cat}_use_epil')
#     butt12 = InlineKeyboardButton('Депиляция воском', callback_data=f'{cat}_use_depil')
#     butt13 = InlineKeyboardButton('Уход за кожей', callback_data=f'{cat}_use_face')
#     butt14 = InlineKeyboardButton('Назад', callback_data=f'{cat}_back_to_round_1')
#     markup_main_panel_cos.row(butt8, butt9).row(butt12, butt13).row(butt11, butt10).add(butt14)
#     await callback.message.edit_text('Выберите нужную подкатегорию 💆🏼‍♀️', reply_markup=markup_main_panel_cos, parse_mode=ParseMode.MARKDOWN)
#     await callback.answer()
#
# async def markup_for_end():
#     markup = InlineKeyboardMarkup()
#     but1 = InlineKeyboardButton('Подтвердить', callback_data='Отменить')
#     but2 = InlineKeyboardButton('Отменить', callback_data='Отменить')
#     markup.row(but1, but2)
#     return markup
#
