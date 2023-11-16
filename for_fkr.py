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

    # Pay772-10-2023
    cursor.execute('SELECT * FROM `Pay772-10-2023`')
    Pay772_10_2023 = cursor.fetchall()

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

    # subs1123
    cursor.execute('SELECT * FROM `subs1123`')
    subs1123 = cursor.fetchall()

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
        'Pay772_10_2023': Pay772_10_2023,
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
        'subs1123': subs1123,
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
Pay772_10_2023 = result['Pay772_10_2023']
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
subs1123 = result['subs1123']
