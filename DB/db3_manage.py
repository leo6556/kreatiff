import sqlite3 as sq
import time

with sq.connect('DB/database3.db') as con:
    cur = con.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS order_b(user_id TEXT, order_num TEXT, order_service TEXT, order_date TEXT, order_time, order_master TEXT, order_number TEXT, sms_1 TEXT, sms_2 TEXT)')

async def save_order(v1,v2,v3,v4,v5,v6,v7):
    cur.execute(f'INSERT INTO order_b (user_id, order_num, order_service,'
                f'order_date, order_time, order_master, order_number, sms_1) VALUES("{v1}", "{v2}", "{v3}", "{v4}"'
                f', "{v5}", "{v6}", "{v7}", "0")')
    con.commit()

async def show_right_order(id):
    return cur.execute('SELECT user_id, order_num, order_service,'
                f'order_date, order_time, order_master, order_number FROM order_b WHERE {id} = user_id').fetchall()

async def del_order(order_num):
    cur.execute(f'DELETE FROM order_b WHERE order_num = {order_num}')
    con.commit()

async def show_order_for_admin():
    t = time.asctime()
    d = int(t[7:10])
    m = t[4:7]

    month = {'Sep': 'сен', 'Oct': 'окт', 'Nov': 'ноя', 'Dec': 'дек', 'Jan': 'янв', 'Feb': 'фев', 'Mar': 'мар',
             'Apr': 'апр', 'May': 'мая', 'Jun': 'июн',
             'Jul': 'июл', 'Aug': 'авг'}
    month2 = {'Sep': 'окт', 'Oct': 'ноя', 'Nov': 'дек', 'Dec': 'янв', 'Jan': 'фев', 'Feb': 'мар', 'Mar': 'апр',
              'Apr': 'мая', 'May': 'июн', 'Jun': 'июл',
              'Jul': 'авг', 'Aug': 'сен'}
    d_month = {'Sep': 30, 'Oct': 31, 'Nov': 30, 'Dec': 31, 'Jan': 31, 'Feb': 28, 'Mar': 31,
               'Apr': 30, 'May': 31, 'Jun': 30,
               'Jul': 31, 'Aug': 31}



    if d_month[m] == 31:
        if d <= 30:
            list = [f'{int(d)} {month[m]}', f'{int(d) + 1} {month[m]}']
        else:
            list = [f'31 {month[m]}', f'1 {month2[m]}']
    elif d_month[m] == 30:
        if d <= 29:
            list = [f'{int(d)} {month[m]}', f'{int(d) + 1} {month[m]}']
        else:
            list = [f'30 {month[m]}', f'1 {month2[m]}']
    else:
        if d <= 27:
            list = [f'{int(d)} {month[m]}', f'{int(d) + 1} {month[m]}']
            print(list)
        else:
            list = [f'31 {month[m]}', f'1 {month2[m]}']
    r = cur.execute(f'SELECT * FROM order_b WHERE order_date = "{list[0]}" or order_date = "{list[1]}"').fetchall()

    # Удаление устаревших заказов

    all = cur.execute('SELECT order_num, order_date FROM order_b').fetchall()
    list_month = ['окт', 'ноя', 'дек', 'янв','фев', 'мар','апр','мая', 'июн', 'июл','авг', 'сен']

    for i in all:
        if i[1][-3:] == month[m]:
            if int(i[1][:2]) < d:
                cur.execute(f'DELETE FROM order_b WHERE order_num = {i[0]}')
                con.commit()
        else:
            if list_month.index(i[1][-3:]) < list_month.index(month[m]):
                cur.execute(f'DELETE FROM order_b WHERE order_num = {i[0]}')
                con.commit()
    return r

async def do_point_warning(v):
    cur.execute(f'UPDATE order_b SET sms_1 = "1" WHERE order_num = "{v}"')
    con.commit()



async def show_right_order_to_del(id):
    return cur.execute(f'SELECT * FROM order_b WHERE order_num = {id}').fetchall()