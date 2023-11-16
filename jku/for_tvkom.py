import sqlite3
from DjangoAIO.settings import BASE_DIR


def tvkom_connect_db():
    connection = sqlite3.connect(f"{BASE_DIR / 'jku/tvkom.db'}")
    cursor = connection.cursor()

    # tvk1022g
    cursor.execute('SELECT * FROM `tvk1022g`')
    tvk1022g = cursor.fetchall()

    # tvk1122g
    cursor.execute('SELECT * FROM `tvk1122g`')
    tvk1122g = cursor.fetchall()

    # tvk1222g
    cursor.execute('SELECT * FROM `tvk1222g`')
    tvk1222g = cursor.fetchall()

    # tvk0123g
    cursor.execute('SELECT * FROM `tvk0123g`')
    tvk0123g = cursor.fetchall()

    # tvk0223g
    cursor.execute('SELECT * FROM `tvk0223g`')
    tvk0223g = cursor.fetchall()

    # tvk0323g
    cursor.execute('SELECT * FROM `tvk0323g`')
    tvk0323g = cursor.fetchall()

    # tvk0423g
    cursor.execute('SELECT * FROM `tvk0423g`')
    tvk0423g = cursor.fetchall()

    # tvk0523g
    cursor.execute('SELECT * FROM `tvk0523g`')
    tvk0523g = cursor.fetchall()

    # tvk0623g
    cursor.execute('SELECT * FROM `tvk0623g`')
    tvk0623g = cursor.fetchall()

    # tvk0723g
    cursor.execute('SELECT * FROM `tvk0723g`')
    tvk0723g = cursor.fetchall()

    # tvk0823g
    cursor.execute('SELECT * FROM `tvk0823g`')
    tvk0823g = cursor.fetchall()

    # tvk0923g
    cursor.execute('SELECT * FROM `tvk0923g`')
    tvk0923g = cursor.fetchall()

    # tvk1023g
    cursor.execute('SELECT * FROM `tvk1023g`')
    tvk1023g = cursor.fetchall()

    connection.close()

    return {
        'tvk1022g': tvk1022g,
        'tvk1122g': tvk1122g,
        'tvk1222g': tvk1222g,
        'tvk0123g': tvk0123g,
        'tvk0223g': tvk0223g,
        'tvk0323g': tvk0323g,
        'tvk0423g': tvk0423g,
        'tvk0523g': tvk0523g,
        'tvk0623g': tvk0623g,
        'tvk0723g': tvk0723g,
        'tvk0823g': tvk0823g,
        'tvk0923g': tvk0923g,
        'tvk1023g': tvk1023g,
    }


result = tvkom_connect_db()
tvk1022g = result['tvk1022g']
tvk1122g = result['tvk1122g']
tvk1222g = result['tvk1222g']
tvk0123g = result['tvk0123g']
tvk0223g = result['tvk0223g']
tvk0323g = result['tvk0323g']
tvk0423g = result['tvk0423g']
tvk0523g = result['tvk0523g']
tvk0623g = result['tvk0623g']
tvk0723g = result['tvk0723g']
tvk0823g = result['tvk0823g']
tvk0923g = result['tvk0923g']
tvk1023g = result['tvk1023g']
