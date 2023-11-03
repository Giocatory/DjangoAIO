import sqlite3
from DjangoAIO.settings import BASE_DIR


def ikibzyak_connect_db():
    connection = sqlite3.connect(f"{BASE_DIR / 'jku/ikibzyak.db'}")
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM PAY')
    PAY_tuples = cursor.fetchall()

    # s1022
    cursor.execute('SELECT * FROM `s1022`')
    s1022 = cursor.fetchall()

    # s1122
    cursor.execute('SELECT * FROM `s1122`')
    s1122 = cursor.fetchall()

    # s1222
    cursor.execute('SELECT * FROM `s1222`')
    s1222 = cursor.fetchall()

    # s0123
    cursor.execute('SELECT * FROM `s0123`')
    s0123 = cursor.fetchall()

    # s0223
    cursor.execute('SELECT * FROM `s0223`')
    s0223 = cursor.fetchall()

    # s0323
    cursor.execute('SELECT * FROM `s0323`')
    s0323 = cursor.fetchall()

    # s0423
    cursor.execute('SELECT * FROM `s0423`')
    s0423 = cursor.fetchall()

    # s0523
    cursor.execute('SELECT * FROM `s0523`')
    s0523 = cursor.fetchall()

    # s0623
    cursor.execute('SELECT * FROM `s0623`')
    s0623 = cursor.fetchall()

    # s0723
    cursor.execute('SELECT * FROM `s0723`')
    s0723 = cursor.fetchall()

    # s0823
    cursor.execute('SELECT * FROM `s0823`')
    s0823 = cursor.fetchall()

    # s0923
    cursor.execute('SELECT * FROM `s0923`')
    s0923 = cursor.fetchall()
    connection.close()

    return {
        'PAY_tuples': PAY_tuples,
        's1022': s1022,
        's1122': s1122,
        's1222': s1222,
        's0123': s0123,
        's0223': s0223,
        's0323': s0323,
        's0423': s0423,
        's0523': s0523,
        's0623': s0623,
        's0723': s0723,
        's0823': s0823,
        's0923': s0923,
    }


result = ikibzyak_connect_db()
PAY_tuples = result['PAY_tuples']
s1022 = result['s1022']
s1122 = result['s1122']
s1222 = result['s1222']
s0123 = result['s0123']
s0223 = result['s0223']
s0323 = result['s0323']
s0423 = result['s0423']
s0523 = result['s0523']
s0623 = result['s0623']
s0723 = result['s0723']
s0823 = result['s0823']
s0923 = result['s0923']
