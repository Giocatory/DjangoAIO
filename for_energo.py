import sqlite3
from DjangoAIO.settings import BASE_DIR


def energo_connect_db():
    connection = sqlite3.connect(f"{BASE_DIR / 'Chita.sqlite3'}")
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM sprrab')
    sprrab_tuples = cursor.fetchall()

    cursor.execute('SELECT * FROM pay')
    pay_tuples = cursor.fetchall()

    cursor.execute('SELECT * FROM energ_tarif')
    energ_tarif_tuples = cursor.fetchall()

    connection.close()

    return {
        'sprrab_tuples': sprrab_tuples,
        'pay_tuples': pay_tuples,
        'energ_tarif_tuples': energ_tarif_tuples,
    }


result = energo_connect_db()
sprrab_tuples = result['sprrab_tuples']
pay_tuples = result['pay_tuples']
energ_tarif_tuples = result['energ_tarif_tuples']
