import sqlite3
from DjangoAIO.settings import BASE_DIR


def eko_connect_db():
    connection = sqlite3.connect(f"{BASE_DIR / 'EKO.sqlite3'}")
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM sprrab')
    sprrab_tuples = cursor.fetchall()

    cursor.execute('SELECT * FROM sprdom')
    sprdom_tuples = cursor.fetchall()

    # Pay979-11-2022
    cursor.execute('SELECT * FROM `Pay979-11-2022`')
    Pay979_11_2022 = cursor.fetchall()

    # Pay979-12-2022
    cursor.execute('SELECT * FROM `Pay979-12-2022`')
    Pay979_12_2022 = cursor.fetchall()

    # Pay979-1-2023
    cursor.execute('SELECT * FROM `Pay979-1-2023`')
    Pay979_1_2023 = cursor.fetchall()

    # Pay979-2-2023
    cursor.execute('SELECT * FROM `Pay979-2-2023`')
    Pay979_2_2023 = cursor.fetchall()

    # Pay979-3-2023
    cursor.execute('SELECT * FROM `Pay979-3-2023`')
    Pay979_3_2023 = cursor.fetchall()

    # Pay979-4-2023
    cursor.execute('SELECT * FROM `Pay979-4-2023`')
    Pay979_4_2023 = cursor.fetchall()

    # Pay979-5-2023
    cursor.execute('SELECT * FROM `Pay979-5-2023`')
    Pay979_5_2023 = cursor.fetchall()

    # Pay979-6-2023
    cursor.execute('SELECT * FROM `Pay979-6-2023`')
    Pay979_6_2023 = cursor.fetchall()

    # Pay979-7-2023
    cursor.execute('SELECT * FROM `Pay979-7-2023`')
    Pay979_7_2023 = cursor.fetchall()

    # Pay979-8-2023
    cursor.execute('SELECT * FROM `Pay979-8-2023`')
    Pay979_8_2023 = cursor.fetchall()

    # Pay979-9-2023
    cursor.execute('SELECT * FROM `Pay979-9-2023`')
    Pay979_9_2023 = cursor.fetchall()

    # Pay979-10-2023
    cursor.execute('SELECT * FROM `Pay979-10-2023`')
    Pay979_10_2023 = cursor.fetchall()
    connection.close()


    return {
        'sprrab_tuples': sprrab_tuples,
        'sprdom_tuples': sprdom_tuples,
        'Pay979_11_2022': Pay979_11_2022,
        'Pay979_12_2022': Pay979_12_2022,
        'Pay979_1_2023': Pay979_1_2023,
        'Pay979_2_2023': Pay979_2_2023,
        'Pay979_3_2023': Pay979_3_2023,
        'Pay979_4_2023': Pay979_4_2023,
        'Pay979_5_2023': Pay979_5_2023,
        'Pay979_6_2023': Pay979_6_2023,
        'Pay979_7_2023': Pay979_7_2023,
        'Pay979_8_2023': Pay979_8_2023,
        'Pay979_9_2023': Pay979_9_2023,
        'Pay979_10_2023': Pay979_10_2023,
    }


result = eko_connect_db()
sprrab_tuples = result['sprrab_tuples']
sprdom_tuples = result['sprdom_tuples']
Pay979_11_2022 = result['Pay979_11_2022']
Pay979_12_2022 = result['Pay979_12_2022']
Pay979_1_2023 = result['Pay979_1_2023']
Pay979_2_2023 = result['Pay979_2_2023']
Pay979_3_2023 = result['Pay979_3_2023']
Pay979_4_2023 = result['Pay979_4_2023']
Pay979_5_2023 = result['Pay979_5_2023']
Pay979_6_2023 = result['Pay979_6_2023']
Pay979_7_2023 = result['Pay979_7_2023']
Pay979_8_2023 = result['Pay979_8_2023']
Pay979_9_2023 = result['Pay979_9_2023']
Pay979_10_2023 = result['Pay979_10_2023']
