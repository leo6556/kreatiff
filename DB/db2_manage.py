import sqlite3 as sq

with sq.connect('DB/database2.db') as con:
    cur = con.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS order_face(name TEXT, master TEXT, sms_1 TEXT, sms_2 TEXT)')
    cur.execute('CREATE TABLE IF NOT EXISTS order_lash(name TEXT, master TEXT, sms_1 TEXT, sms_2 TEXT)')
    cur.execute('CREATE TABLE IF NOT EXISTS order_brow(name TEXT, master TEXT, sms_1 TEXT, sms_2 TEXT)')
    cur.execute('CREATE TABLE IF NOT EXISTS order_man(name TEXT, master TEXT, sms_1 TEXT, sms_2 TEXT)')
    cur.execute('CREATE TABLE IF NOT EXISTS order_depil(name TEXT, master TEXT, sms_1 TEXT, sms_2 TEXT)')
    cur.execute('CREATE TABLE IF NOT EXISTS order_bar(name TEXT, master TEXT, sms_1 TEXT, sms_2 TEXT)')
    cur.execute('CREATE TABLE IF NOT EXISTS order_care(name TEXT, master TEXT, sms_1 TEXT, sms_2 TEXT)')
    cur.execute('CREATE TABLE IF NOT EXISTS order_else(name TEXT, master TEXT, sms_1 TEXT, sms_2 TEXT)')
    cur.execute('CREATE TABLE IF NOT EXISTS admin_main(user_id, sms_1, sms_2)')

async def shablon_show_order(table):
    return cur.execute(f'SELECT name, master FROM {table}').fetchall()

async def del_service(v1, v2):
    cur.execute(f'DELETE FROM order_{v1} WHERE name = "{v2}"')
    con.commit()


async def insert_service(v1, v2, v3):
    cur.execute(f'INSERT INTO {v1} (name, master) VALUES ("{v2}", "{v3}")')
    con.commit()

async def del_in_db_admin(var):

    cur.execute(f'DELETE FROM admin_main WHERE user_id = "{var}"')
    con.commit()

async def add_in_db_admin(var):
    cur.execute(f'INSERT INTO admin_main (user_id) VALUES ("{var}")')
    # cur.execute(f'DELETE FROM admin_main WHERE user_id = "{var}"')
    con.commit()

async def show_all_admin():
    a = cur.execute('SELECT user_id FROM admin_main').fetchall()
    cur_list = []
    for i in a:
        if i[0] not in cur_list:
            cur_list.append(i[0])
    return cur_list

async def check_admin(var):
    r = cur.execute(f'SELECT user_id FROM admin_main WHERE user_id = "{var}"').fetchall()
    if len(r) >= 1:
        return 'yes'
    else:
        return 'no'
