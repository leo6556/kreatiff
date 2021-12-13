# from aiogram import types
# from aiogram.dispatcher.filters import Text
# from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
#
# from aiogram.dispatcher import FSMContext
# from loader import dp
# from keyboards.inline.panel_admin import *
#
# from DB.db_manage import *
# from keyboards.inline.panel_admin import *
# from states.red_price import *
#
# @dp.message_handler(commands='admin')
# async def start_afmin(message : types.Message):
#     await main_admin_panel(message)
#
# @dp.callback_query_handler(Text(startswith='re_price'))
# async def red_price(callback : types.CallbackQuery):
#     await red_price_panel(callback)
#
# @dp.callback_query_handler(Text(startswith='red_'), state=None)
# async def add_in_price(callbback: types.CallbackQuery, state : FSMContext):
#     data = callbback.data
#
#     if data == 'red_cos':
#         await red_price_round_2_cos(callbback, cat='reg')
#     elif data == 'red_add':
#         await red_price_round_1(callbback, cat='reg')
#     elif data == 'red_bar':
#         await red_price_round_2_bar(callbback, cat='reg')
#     elif data == 'red_hall_w':
#         await red_price_round_3_bar(callbback, cat='reg')
#     elif data == 'red_back_to_round_1':
#         await red_price_round_1(callbback, cat='reg')
#
#     if data[:7] == 'red_use':
#         await Client.name.set()
#         async with state.proxy() as data:
#             data['callback'] = callbback.data
#         await callbback.message.edit_text('Введите название новой услуги')
#
# @dp.message_handler(state=Client.name)
# async def save_name(message : types.Message, state : FSMContext):
#     name = message.text
#     async with state.proxy() as data:
#         data['name'] = name
#     await message.answer('Теперь введице цену (только цифру)')
#     await Client.next()
#
# @dp.message_handler(state=Client.price)
# async def save_all(message : types.Message, state : FSMContext):
#     price = message.text
#
#     async with state.proxy() as data:
#         print(data['callback'])
#         data['price'] = price
#
#     await message.answer(f'Проверьте правильно ли зиписано: {data["name"]} - {data["price"]}P', reply_markup=await markup_for_end())
#
# @dp.callback_query_handler(Text(startswith=''), state=Client.price)
# async def end_add_price(callback : types.CallbackQuery, state : FSMContext):
#     if callback.data == '':
#         pass
#     else:
#         pass
#     await state.finish()
#
#
#
#
# @dp.callback_query_handler(Text(startswith=''))
# async def what_del(callback: types.CallbackQuery):
#     pass