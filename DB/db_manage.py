import sqlite3 as sq
from loader import bot, dp
from aiogram import types

from aiogram import types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ParseMode


with sq.connect('DB/database_price.db') as con:
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
    read = cur.execute('SELECT name, price FROM price_man').fetchall()
    print(read)
    return read

async def show_price_ped():
    read = cur.execute('SELECT name, price FROM price_ped').fetchall()
    return read

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



async def edit_del_shablon(callback : types.CallbackQuery, v1):
    v2 = v1[8:]
    print(v2)

    read = cur.execute(f'SELECT name, price, rowid FROM price{v2}').fetchall()
    print(read)
    markup = InlineKeyboardMarkup()
    for i in read:
        markup.row(InlineKeyboardButton(f'{i[0]}', callback_data=f'enel{v2}_{i[2]}'))
    markup.row(InlineKeyboardButton('назад', callback_data=f'edit_back_1'))
    await callback.message.edit_text('Нажмите на услугу, которую хотите удалить из прайса 🗑', reply_markup = markup)

async def edit_end_del(v1, v2):
    if len(v1) == 1:
        cur.execute(f'DELETE FROM price_{v1[0]} WHERE rowid = {v2}')
        con.commit()
    else:
        cur.execute(f'DELETE FROM price_{v1[0]}_{v1[1]} WHERE rowid = {v2}')
        con.commit()



async def edit_cha_shablon(callback : types.CallbackQuery, v1):
    v2 = v1[8:]
    read = cur.execute(f'SELECT name, price, rowid FROM price{v2}').fetchall()
    print(read)
    markup = InlineKeyboardMarkup()
    for i in read:
        markup.row(InlineKeyboardButton(f'{i[0]}', callback_data=f'chpr{v2}_{i[2]}')).row(InlineKeyboardButton(f'{i[1]}', callback_data=f'chpr{v2}_{i[2]}'))
    markup.row(InlineKeyboardButton('назад', callback_data=f'edit_back_1'))
    await callback.message.edit_text('Нажмите на услугу, которой хотите поменять цену\n\n/stop_add -- отменить добавление', reply_markup=markup)
    await callback.answer()

async def edit_cha_end(v1, v2, v3):
    if len(v1) == 1:
        cur.execute(f'UPDATE price_{v1[0]} SET price = "{v3} ₽" WHERE rowid = {v2}')
        con.commit()
    else:
        cur.execute(f'UPDATE price_{v1[0]}_{v1[1]} SET price = "{v3} ₽" WHERE rowid = {v2}')
        con.commit()


async def edit_add_shablon(v1, v2, v3):
    v6 = v1[8:]
    print(v6)

    cur.execute(f'INSERT INTO price{v6} (name, price) VALUES ("{v2}", "{v3} ₽")')
    con.commit()
