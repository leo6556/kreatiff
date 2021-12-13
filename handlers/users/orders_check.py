
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram import types, Dispatcher
from aiogram.types import ContentType

from states.sighup import *
from keyboards.inline.panel_state_sighup import *
from DB.db3_manage import *
from keyboards.inline.show_right_order import *

from aiogram import types, Dispatcher
from aiogram.types import ParseMode
from loader import dp, bot

@dp.message_handler(commands='myorders')
async def show_orders(message : types.Message):
    id = message.from_user.id
    read = await show_right_order(id)
    if len(read) == 0:
        await message.answer(text='У вас пока нет заказов, /sighup - записаться')

    for i in read:
        text = [
            f'*Ваш заказ:* 🔖 # {i[1]}',
            f'*Дата* - {i[3]}',
            f'*Услуга* - {i[2]}',
            f'*Время* - {i[4]}',
            f'*Мастер* - {i[5]}',
            f'*Ваш номер* - {i[6]}',

        ]
        await message.answer(text='\n'.join(text), parse_mode=ParseMode.MARKDOWN, reply_markup=markup22)




@dp.callback_query_handler(Text(startswith='show_'))
async def call_right_order(callback : types.CallbackQuery):
    cur_text = callback.message.text

    if callback.data == 'show_more':
        text = cur_text + '\n' + '📍Адрес: просп. Просвещения, 15' + '\n' + '📍Ежедневно c 10:00 до 22:00' "\n" + '📍Связь: +7 (911) 138-99-08'
        await callback.message.edit_text(text=text, reply_markup=markup33)
        await callback.answer()

    elif callback.data == 'show_stop':
        text = cur_text + '\n\n' + '*Вы уверены, что хотите удалить заказ?*🤔'
        await callback.message.edit_text(text=text, reply_markup=markup44, parse_mode=ParseMode.MARKDOWN)
        await callback.answer()

    elif callback.data == 'show_less':
        spl = cur_text.split('📍')
        await callback.message.edit_text(text=spl[0], reply_markup=markup22)
        await callback.answer()

    elif callback.data == 'show_less_back':
        spl = cur_text.split("Ваш номер - ")
        await callback.message.edit_text(text=spl[0]+"Ваш номер - "+spl[1][:11], reply_markup=markup22)
        await callback.answer()

    elif callback.data == 'show_del':
        spl = cur_text.split('#')
        order_num = spl[1][1:5]

        data = await show_right_order_to_del(order_num)
        await del_order(order_num)
        print(data)

        admin = await show_all_admin()

        for j in admin:
            for i in data:
                text = [
                    f'*Клиент отменил заказ* 😌 "{i[2]}" на {i[3]} в {i[4]}',
                    f'*Мастер:* {i[5]}',
                    f'*Номер клиента:* {i[6]}',
                ]
                await bot.send_message(j, text='\n'.join(text), parse_mode=ParseMode.MARKDOWN)


        await callback.message.edit_text('Заказ расформирован 😌')