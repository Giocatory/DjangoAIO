import sqlite3
from DjangoAIO.settings import BASE_DIR


def fkr_connect_db():
    connection = sqlite3.connect(f"{BASE_DIR / 'FKR.sqlite3'}")
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM sprrab')
    sprrab_tuples = cursor.fetchall()

    cursor.execute('SELECT * FROM sprdom')
    sprdom_tuples = cursor.fetchall()

    # Pay772-01-2023
    cursor.execute('SELECT * FROM `Pay772-01-2023`')
    Pay772_01_2023 = cursor.fetchall()

    # Pay772-02-2023
    cursor.execute('SELECT * FROM `Pay772-02-2023`')
    Pay772_02_2023 = cursor.fetchall()

    # Pay772-03-2023
    cursor.execute('SELECT * FROM `Pay772-03-2023`')
    Pay772_03_2023 = cursor.fetchall()

    # Pay772-04-2023
    cursor.execute('SELECT * FROM `Pay772-04-2023`')
    Pay772_04_2023 = cursor.fetchall()

    # Pay772-05-2023
    cursor.execute('SELECT * FROM `Pay772-05-2023`')
    Pay772_05_2023 = cursor.fetchall()

    # Pay772-06-2023
    cursor.execute('SELECT * FROM `Pay772-06-2023`')
    Pay772_06_2023 = cursor.fetchall()

    # Pay772-07-2023
    cursor.execute('SELECT * FROM `Pay772-07-2023`')
    Pay772_07_2023 = cursor.fetchall()

    # Pay772-08-2023
    cursor.execute('SELECT * FROM `Pay772-08-2023`')
    Pay772_08_2023 = cursor.fetchall()

    # Pay772-09-2023
    cursor.execute('SELECT * FROM `Pay772-09-2023`')
    Pay772_09_2023 = cursor.fetchall()
    connection.close()

    return {
        'sprrab_tuples': sprrab_tuples,
        'sprdom_tuples': sprdom_tuples,
        'Pay772_01_2023': Pay772_01_2023,
        'Pay772_02_2023': Pay772_02_2023,
        'Pay772_03_2023': Pay772_03_2023,
        'Pay772_04_2023': Pay772_04_2023,
        'Pay772_05_2023': Pay772_05_2023,
        'Pay772_06_2023': Pay772_06_2023,
        'Pay772_07_2023': Pay772_07_2023,
        'Pay772_08_2023': Pay772_08_2023,
        'Pay772_09_2023': Pay772_09_2023,
    }


result = fkr_connect_db()
sprrab_tuples = result['sprrab_tuples']
sprdom_tuples = result['sprdom_tuples']
Pay772_01_2023 = result['Pay772_01_2023']
Pay772_02_2023 = result['Pay772_02_2023']
Pay772_03_2023 = result['Pay772_03_2023']
Pay772_04_2023 = result['Pay772_04_2023']
Pay772_05_2023 = result['Pay772_05_2023']
Pay772_06_2023 = result['Pay772_06_2023']
Pay772_07_2023 = result['Pay772_07_2023']
Pay772_08_2023 = result['Pay772_08_2023']
Pay772_09_2023 = result['Pay772_09_2023']
