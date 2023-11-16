import sqlite3
from DjangoAIO.settings import BASE_DIR


def energo_connect_db():
    connection = sqlite3.connect(f"{BASE_DIR / 'energo.sqlite3'}")
    cursor = connection.cursor()

    # sprrab202212
    cursor.execute('SELECT * FROM sprrab202212')
    sprrab202212_tuples = cursor.fetchall()

    # sprrab202301
    cursor.execute('SELECT * FROM sprrab202301')
    sprrab202301_tuples = cursor.fetchall()

    # sprrab202302
    cursor.execute('SELECT * FROM sprrab202302')
    sprrab202302_tuples = cursor.fetchall()

    # sprrab202303
    cursor.execute('SELECT * FROM sprrab202303')
    sprrab202303_tuples = cursor.fetchall()

    # sprrab202304
    cursor.execute('SELECT * FROM sprrab202304')
    sprrab202304_tuples = cursor.fetchall()

    # sprrab202305
    cursor.execute('SELECT * FROM sprrab202305')
    sprrab202305_tuples = cursor.fetchall()

    # sprrab202306
    cursor.execute('SELECT * FROM sprrab202306')
    sprrab202306_tuples = cursor.fetchall()

    # sprrab202307
    cursor.execute('SELECT * FROM sprrab202307')
    sprrab202307_tuples = cursor.fetchall()

    # sprrab202308
    cursor.execute('SELECT * FROM sprrab202308')
    sprrab202308_tuples = cursor.fetchall()

    # sprrab202309
    cursor.execute('SELECT * FROM sprrab202309')
    sprrab202309_tuples = cursor.fetchall()

    # sprrab202310
    cursor.execute('SELECT * FROM sprrab202310')
    sprrab202310_tuples = cursor.fetchall()

    cursor.execute('SELECT * FROM pay')
    pays_tuples = cursor.fetchall()



    connection.close()

    return {
        'sprrab202212_tuples': sprrab202212_tuples,
        'sprrab202301_tuples': sprrab202301_tuples,
        'sprrab202302_tuples': sprrab202302_tuples,
        'sprrab202303_tuples': sprrab202303_tuples,
        'sprrab202304_tuples': sprrab202304_tuples,
        'sprrab202305_tuples': sprrab202305_tuples,
        'sprrab202306_tuples': sprrab202306_tuples,
        'sprrab202307_tuples': sprrab202307_tuples,
        'sprrab202308_tuples': sprrab202308_tuples,
        'sprrab202309_tuples': sprrab202309_tuples,
        'sprrab202310_tuples': sprrab202310_tuples,
        'pays_tuples': pays_tuples,
    }


result = energo_connect_db()

sprrab202212_tuples = result['sprrab202212_tuples']
sprrab202301_tuples = result['sprrab202301_tuples']
sprrab202302_tuples = result['sprrab202302_tuples']
sprrab202303_tuples = result['sprrab202303_tuples']
sprrab202304_tuples = result['sprrab202304_tuples']
sprrab202305_tuples = result['sprrab202305_tuples']
sprrab202306_tuples = result['sprrab202306_tuples']
sprrab202307_tuples = result['sprrab202307_tuples']
sprrab202308_tuples = result['sprrab202308_tuples']
sprrab202309_tuples = result['sprrab202309_tuples']
sprrab202310_tuples = result['sprrab202310_tuples']
pays_tuples = result['pays_tuples']
