from aiogram import types
from aiogram.dispatcher.filters import Text
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from loader import dp

import sqlite3 as sq
from loader import bot, dp
from aiogram import types

with sq.connect('DB\database.db') as con:
    cur = con.cursor()
    cur.execute('CREATE TABLE IF NOt EXISTS price_man (name TEXT, price TEXT, sms_1 TEXT, sms_2 TEXT)')
    cur.execute('CREATE TABLE IF NOt EXISTS price_ped (name TEXT, price TEXT, sms_1 TEXT, sms_2 TEXT)')
    cur.execute('CREATE TABLE IF NOt EXISTS price_bar_m (name TEXT, price TEXT, sms_1 TEXT, sms_2 TEXT)')

    cur.execute('CREATE TABLE IF NOt EXISTS price_bar_cut (name TEXT, price TEXT, sms_1 TEXT, sms_2 TEXT)')
    cur.execute('CREATE TABLE IF NOt EXISTS price_bar_laying (name TEXT, price TEXT, sms_1 TEXT, sms_2 TEXT)')
    cur.execute('CREATE TABLE IF NOt EXISTS price_bar_care (name TEXT, price TEXT, sms_1 TEXT, sms_2 TEXT)')
    cur.execute('CREATE TABLE IF NOt EXISTS price_bar_coloring (name TEXT, price TEXT, sms_1 TEXT, sms_2 TEXT)')

    cur.execute('CREATE TABLE IF NOt EXISTS price_cos_brow (name TEXT, price TEXT, sms_1 TEXT, sms_2 TEXT)')
    cur.execute('CREATE TABLE IF NOt EXISTS price_cos_lash (name TEXT, price TEXT, sms_1 TEXT, sms_2 TEXT)')
    cur.execute('CREATE TABLE IF NOt EXISTS price_cos_ear (name TEXT, price TEXT, sms_1 TEXT, sms_2 TEXT)')
    cur.execute('CREATE TABLE IF NOt EXISTS price_cos_epil (name TEXT, price TEXT, sms_1 TEXT, sms_2 TEXT)')
    cur.execute('CREATE TABLE IF NOt EXISTS price_cos_depil (name TEXT, price TEXT, sms_1 TEXT, sms_2 TEXT)')
    cur.execute('CREATE TABLE IF NOt EXISTS price_cos_face (name TEXT, price TEXT, sms_1 TEXT, sms_2 TEXT)')


async def show_price_man():
    return cur.execute('SELECT name, price FROM price_man').fetchall()

async def show_price_ped():
    return cur.execute('SELECT name, price FROM price_ped').fetchall()

async def show_price_bar_m():
    return cur.execute('SELECT name, price FROM price_bar_m').fetchall()

async def show_price_cut():
    return cur.execute('SELECT name, price FROM price_bar_cut').fetchall()

async def show_price_coloring():
    return cur.execute('SELECT name, price FROM price_bar_coloring').fetchall()

async def show_price_laying():
    return cur.execute('SELECT name, price FROM price_bar_laying').fetchall()

async def show_price_care():
    return cur.execute('SELECT name, price FROM price_bar_care').fetchall()

async def show_price_lash():
    return cur.execute('SELECT name, price FROM price_cos_lash').fetchall()

async def show_price_face():
    return cur.execute('SELECT name, price FROM price_cos_face').fetchall()

async def show_price_epil():
    return cur.execute('SELECT name, price FROM price_cos_epil').fetchall()

async def show_price_depil():
    return cur.execute('SELECT name, price FROM price_cos_depil').fetchall()

async def show_price_brow():
    return cur.execute('SELECT name, price FROM price_cos_brow').fetchall()

async def show_price_ear():
    return cur.execute('SELECT name, price FROM price_cos_ear').fetchall()




from DB.db_manage import *
from keyboards.inline.panel_price import *

# ШАБЛОН

async def shablon_cos(func, func_2, callback, title, nexty, backy):
    read = await func()
    text = f'услуги {title}:'
    for i in read:
        text = text + '\n' + f'💈 {i[0]} -- {i[1]}'
    await func_2(callback.message, text, nexty, backy)

# *******************
# @dp.message_handler(commands='price')
# async def start_price(message : types.Message):
#     await main_panel(message)


@dp.callback_query_handler(Text(startswith='pri_'))
async def show_price(callback : types.CallbackQuery):

    data = callback.data
    ch = 0

    if data == 'pri_man':
        read = await show_price_man()
        print(read)
        text = '*Услуги маникюра* 💅🏼'

        for i in read:
            text = text + '\n' + f'💈 {i[0]} -- {i[1]}'
            ch += 1
            if ch == 9:
                break
        await sec_cat_man(callback, text)
    elif data == 'pri_ped':
        read = await show_price_ped()
        text = '*Услуги педикюра:* 🦶🏼'

        for i in read:
            text = text + '\n' + f'💈 {i[0]} -- {i[1]}'
            ch += 1
            if ch == 7:
                break
        await sec_cat_ped(callback, text)
        await callback.answer()

    if data == 'pri_bar':
        await main_panel_bar_1(callback)
    elif data == 'pri_cos':
        await main_panel_cos(callback)
    elif data == 'pri_bar_m':
        read = await show_price_bar_m()
        text = '*Услуги парикмахера* 💇🏻‍♂️'

        for i in read:
            text = text + '\n' + f'💈 {i[0]} -- {i[1]}'
        await third_cat_bar_m(callback, text)
    elif data == 'pri_cut':
        read = await show_price_cut()
        text = '*Услуги парикмахера* 💇🏼‍♀️'
        for i in read:
            text = text + '\n' + f'💈 {i[0]} -- {i[1]}'
        await third_cat_bar_cut(callback, text)
    elif data == 'pri_laying':
        read = await show_price_laying()
        text = '*Укладка* 💆🏼‍♀️'
        for i in read:
            text = text + '\n' + f'💈 {i[0]} -- {i[1]}'
        await third_cat_bar_laying(callback, text)
    elif data == 'pri_care':
        read = await show_price_care()
        text = '*Уход за волосами* 👩🏻‍🦰'

        for i in read:
            text = text + '\n' + f'💈 {i[0]} -- {i[1]}'
        await third_cat_bar_care(callback, text)
    elif data == 'pri_coloring':
        read = await show_price_coloring()
        text = '*Наращивание и окрашивание* 🧑🏼‍🎤'
        for i in read:
            text = text + '\n' + f'💈 {i[0]} -- {i[1]}'
        await third_cat_bar_coloring(callback, text)

    if data == 'pri_lash':
        read = await show_price_lash()
        text = f'*Ресницы* 🧏🏼‍♀️'
        for i in read:
            text = text + '\n' + f'💈 {i[0]} -- {i[1]}'
        await shablon(callback, text, 'cos_lash', 'panel_cos')
    elif data == 'pri_face':
        read = await show_price_face()
        text = f'*Уход за кожей* 👩🏼‍🦲'
        for i in read:
            text = text + '\n' + f'💈 {i[0]} -- {i[1]}'
        await shablon(callback, text, 'cos_face', 'panel_cos')
    elif data == 'pri_epil':
        read = await show_price_epil()
        text = f'*Лазерная эпиляция* 🧖🏼'
        for i in read:
            text = text + '\n' + f'💈 {i[0]} -- {i[1]}'
        await shablon(callback, text, 'cos_epil', 'panel_cos')
    elif data == 'pri_depil':
        read = await show_price_depil()
        text = f'*Услуги депиляции* 🪒'
        for i in read:
            text = text + '\n' + f'💈 {i[0]} -- {i[1]}'
        await shablon(callback, text, 'cos_depil', 'panel_cos')
    elif data == 'pri_brow':
        read = await show_price_brow()
        text = f'*Брови* 🧏🏼‍♀️'
        for i in read:
            text = text + '\n' + f'💈 {i[0]} -- {i[1]}'
        await shablon(callback, text, 'cos_brow', 'panel_cos')
    elif data == 'pri_ear':
        read = await show_price_ear()
        text = f'*Другое* 💁🏼‍♀️'
        for i in read:
            text = text + '\n' + f'💈 {i[0]} -- {i[1]}'
        await shablon(callback, text, 'cos_ear', 'panel_cos')

@dp.callback_query_handler(Text(startswith='sub_'))
async def subcategory(callback : types.CallbackQuery):

    if callback.data == 'sub_hall_w':
        await main_panel_bar_w(callback)
        await callback.answer()


@dp.callback_query_handler(Text(startswith='next'))
async def rewind(callback : types.CallbackQuery):

    if callback.data == 'next_man':
        if callback.message.text[:1] == 'У':
            read = await show_price_man()
            read = read[9:]
            text = '*продолжение: Услуги маникюра* 💅🏼'
            for i in read:
                text = text + '\n' + f'💈 {i[0]} -- {i[1]}'
            await sec_cat_man(callback, text)
        else:
            read = await show_price_man()
            read = read[:9]
            text = '*Услуги маникюра* 💅🏼'
            for i in read:
                text = text + '\n' + f'💈 {i[0]} -- {i[1]}'
            await sec_cat_man(callback, text)
    elif callback.data == 'next_ped':
        if callback.message.text[:1] == 'У':
            read = await show_price_ped()
            read = read[7:]
            text = '*продолжение: Услуги педикюра:* 🦶🏼'
            for i in read:
                text = text + '\n' + f'💈 {i[0]} -- {i[1]}'
            await sec_cat_ped(callback, text)
        else:
            read = await show_price_ped()
            read = read[:7]
            text = '*Услуги педикюра:* 🦶🏼'
            for i in read:
                text = text + '\n' + f'💈 {i[0]} -- {i[1]}'
            await sec_cat_ped(callback, text)


@dp.callback_query_handler(Text(startswith='back'))
async def back_man(callback : types.CallbackQuery):

    if callback.data == 'back_panel_bar':
        await main_panel_bar_w(callback)
        await callback.answer()
    elif callback.data == 'back_man' or callback.data == 'back_ped':
        markup = InlineKeyboardMarkup().row(InlineKeyboardButton("Косметология", callback_data="pri_cos"),
                                            InlineKeyboardButton("Парикмахерская", callback_data="pri_bar")).row(
            InlineKeyboardButton("Маникюр", callback_data="pri_man"),
            InlineKeyboardButton("Педикюр", callback_data="pri_ped"))
        await callback.message.edit_text('Выберите категорию', reply_markup=markup)
        await callback.answer()
    elif callback.data == 'back_bar_hall':
        await main_panel_bar_1(callback)
        await callback.answer()
    elif callback.data == 'back_panel_cos':
        await main_panel_cos(callback)
        await callback.answer()





# def reg_price(dp : Dispatcher):
#     dp.register_message_handler(start_price, commands='price')
#
    # dp.register_message_handler(save_number, state=Driver.number)
    # dp.register_callback_query_handler(stat, lambda x: x.data.startswith('dri1'), state=None)
    # dp.register_callback_query_handler(save_when, lambda x: x.data.startswith('1'), state=Driver.when)
    # dp.register_callback_query_handler(ending, lambda x: x.data.startswith('check'), state=Driver.end)




# @ dp.callback_query_handler(lambda x: x.data and x.data.startswith('del '))


