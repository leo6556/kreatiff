from aiogram import types
from aiogram.dispatcher.filters import Text
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from aiogram.dispatcher import FSMContext

from DB.db2_manage import *
from DB.db3_manage import show_order_for_admin, do_point_warning
from keyboards.inline.panel_state_sighup import shablon
from loader import dp

from DB.db_manage import *
from keyboards.inline.panel_admin_2 import *
from states.red_price import *


async def shablon_e(callback : types.CallbackQuery, table, state : FSMContext, pm):
    read = await shablon_show_order(f'{table}')
    dict = {}

    markup = InlineKeyboardMarkup()
    for i in read:
        markup.add(InlineKeyboardButton(f'{i[0]}', callback_data=f'deli{pm}_{i[0]}'))
        dict[i[0]] = i[1]
    markup.add(InlineKeyboardButton('Назад', callback_data="redact_del"))

    async with state.proxy() as data:
        data['master_1'] = dict

    await callback.message.edit_text('Какую услугу удалить? 💆🏼‍♀️', reply_markup=markup)
    await callback.answer()


@dp.message_handler(commands='admin')
async def start_afmin(message : types.Message):
    di = await check_admin(message.from_user.id)
    if di == 'yes':
        await main_admin_panel(message)
    else:
        await message.answer('Вы не являетесь админом')

@dp.callback_query_handler(Text(startswith='red_'))
async def red_price(callback : types.CallbackQuery):
    await red_price_panel(callback)



@dp.callback_query_handler(Text(startswith='redact'))
async def gg(callback : types.CallbackQuery):
    if callback.data == 'redact_add':
        await main_panel_for_edit(callback, cat='add', cat2='Выберите в какую категорию нужно добавить услугу')
    elif callback.data == 'redact_del':
        await main_panel_for_edit(callback, cat='del', cat2='Выберите из какой категории нужно удалить услугу')
    if callback.data == 'redact_aa':
        markup = InlineKeyboardMarkup()
        but1 = InlineKeyboardButton('Добавить админа', callback_data='fake_admin')
        but2 = InlineKeyboardButton('Редактировать каталог услуг', callback_data='red_cat')
        but3 = InlineKeyboardButton('Просмотр ближайших записей', callback_data='letmesee_order')
        markup.row(but1).row(but3).row(but2)
        await callback.message.edit_text('Выберите нужную функцию ⚙️', reply_markup=markup)
        await callback.answer()

# **************************** Удаление услуги


@dp.callback_query_handler(Text(startswith='del'), state=None)
async def delit(callback : types.CallbackQuery, state : FSMContext):
    data = callback.data[4:]
    pm = callback.data.split('_')[-1]
    print((data, pm))
    if data == 'order_face':
        await shablon_e(callback, table=f'{data}', state=state, pm=pm)
    elif data == 'order_lash':
        await shablon_e(callback, table=f'{data}', state=state, pm=pm)
    elif data == 'order_brow':
        await shablon_e(callback, table=f'{data}', state=state, pm=pm)
    elif data == 'order_depil':
        await shablon_e(callback, table=f'{data}', state=state, pm=pm)
    elif data == 'order_man':
        await shablon_e(callback, table=f'{data}', state=state, pm=pm)
    elif data == 'order_bar':
        await shablon_e(callback, table=f'{data}', state=state, pm=pm)
    elif data == 'order_care':
        await shablon_e(callback, table=f'{data}', state=state, pm=pm)
    elif data == 'order_else':
        await shablon_e(callback, table=f'{data}', state=state, pm=pm)

    if callback.data[:4] == 'deli':
        current = callback.data.split('_')
        await del_service(v1=f'{current[0][4:]}', v2=f'{current[1]}')
        await callback.message.edit_text('Услуга удалена из списка')


# **************************** Добавление услуги

@dp.message_handler(commands='stop_add', state="*")
async def do_this_shit(message : types.Message, state : FSMContext):
    await message.answer('Добавление отменено')
    await state.finish()

@dp.callback_query_handler(Text(startswith='add'), state=None)
async def addit(callback : types.CallbackQuery, state : FSMContext):
    async with state.proxy() as data:
        data['callback'] = callback.data
    await Client.name.set()

    await callback.message.edit_text('*Введите название услуги:*\n\n/stop\_add -- отменить добавление', parse_mode=ParseMode.MARKDOWN)


@dp.message_handler(state=Client.name)
async def save_name(message : types.Message, state : FSMContext):
    name = message.text
    if len(name) > 32:
        await message.answer('Добавление отменено 😕 лишком длинное название (более 32 символов), попытайтесь сократить')
        await state.finish()
        await main_admin_panel(message)
    else:
        async with state.proxy() as data:
            data['name'] = name
        await message.answer(
            '*Теперь введите мастера который выполняют работу*\nЕсли их несколько, то строго через одну запятую.', parse_mode=ParseMode.MARKDOWN)
        await Client.next()


@dp.message_handler(state=Client.master)
async def save_master(message : types.Message, state:FSMContext):
    master = message.text
    async  with state.proxy() as data:
        data['master'] = master

    text = [
        f'*Проверте детали*',
        f'*услуга:* {data["name"]}',
        f'*мастер:* {data["master"]}'
    ]
    await message.answer(text='\n'.join(text), reply_markup=await end_q(), parse_mode=ParseMode.MARKDOWN)

@dp.callback_query_handler(Text(startswith='do'), state=Client.master)
async def ggg(callback : types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        pass
    if callback.data == 'dothisshit':
        await insert_service(data['callback'][4:], data['name'], data['master'] )
        await callback.message.edit_text('Услуга добавлена')
        await state.finish()
    else:
        await callback.message.edit_text('Добавление отменено')
        await state.finish()



# **************************** Добавление админа-справка

@dp.callback_query_handler(Text(startswith='fake_admin'))
async def add_admin(callback : types.CallbackQuery):
    text = [
        '*Для того чтобы добавить админа, надо:* 👩🏻‍💻',
        '*1.* отправить команду /stayadmin c того телефона, который должен стать админом',
        '*2.* ввести код доступа: "50200"',
        '',
        '/admin -- вернуться в панель управления'

    ]
    await callback.message.edit_text(text='\n'.join(text), parse_mode=ParseMode.MARKDOWN)



# **************************** Просмотр ближайших заказов

@dp.callback_query_handler(Text(startswith='letmesee'))
async def letmesee(callback : types.CallbackQuery):
    read = await show_order_for_admin()
    if len(read) >= 1:
        for i in read:
            text = [
                f'   *Заказ* 🔖 #{i[1]} ',
                f'*Дата* - {i[3]}',
                f'*Услуга* - {i[2]}',
                f'*Время* - {i[4]}',
                f'*Мастер* - {i[5]}',
                f'*Номер клиента:* - {i[6]}'
            ]
            await callback.message.answer(text='\n'.join(text), reply_markup=await markup_for_warning(i),
                                          parse_mode=ParseMode.MARKDOWN)
    else:
        await callback.message.edit_text('На ближайшие 2 дня нет записей')


@dp.callback_query_handler(Text(startswith='warn'))
async def do_warning(callback : types.CallbackQuery):
    d = callback.data.split('_')
    await bot.send_message(chat_id=d[1], text=f'Надпоминаем ☺ у вас  запись в салон красоты на {d[3]} \n/myorders -- посмотреть свои заказы')
    await do_point_warning(d[2])
    await callback.message.edit_text('Клиенту отправлено надпоминание!')