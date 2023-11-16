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

    # Pay979-11-2023
    cursor.execute('SELECT * FROM `Pay979-11-2023`')
    Pay979_11_2023 = cursor.fetchall()

    # subs
    # subs0123
    cursor.execute('SELECT * FROM `subs0123`')
    subs0123 = cursor.fetchall()

    # subs0223
    cursor.execute('SELECT * FROM `subs0223`')
    subs0223 = cursor.fetchall()

    # subs0323
    cursor.execute('SELECT * FROM `subs0323`')
    subs0323 = cursor.fetchall()

    # subs0423
    cursor.execute('SELECT * FROM `subs0423`')
    subs0423 = cursor.fetchall()

    # subs0523
    cursor.execute('SELECT * FROM `subs0523`')
    subs0523 = cursor.fetchall()

    # subs0623
    cursor.execute('SELECT * FROM `subs0623`')
    subs0623 = cursor.fetchall()

    # subs0723
    cursor.execute('SELECT * FROM `subs0723`')
    subs0723 = cursor.fetchall()

    # subs0823
    cursor.execute('SELECT * FROM `subs0823`')
    subs0823 = cursor.fetchall()

    # subs0923
    cursor.execute('SELECT * FROM `subs0923`')
    subs0923 = cursor.fetchall()

    # subs1023
    cursor.execute('SELECT * FROM `subs1023`')
    subs1023 = cursor.fetchall()

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
        'Pay979_11_2023': Pay979_11_2023,
        # subs
        'subs0123': subs0123,
        'subs0223': subs0223,
        'subs0323': subs0323,
        'subs0423': subs0423,
        'subs0523': subs0523,
        'subs0623': subs0623,
        'subs0723': subs0723,
        'subs0823': subs0823,
        'subs0923': subs0923,
        'subs1023': subs1023,
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
Pay979_11_2023 = result['Pay979_11_2023']
# subs
subs0123 = result['subs0123']
subs0223 = result['subs0223']
subs0323 = result['subs0323']
subs0423 = result['subs0423']
subs0523 = result['subs0523']
subs0623 = result['subs0623']
subs0723 = result['subs0723']
subs0823 = result['subs0823']
subs0923 = result['subs0923']
subs1023 = result['subs1023']
