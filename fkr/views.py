from django.shortcuts import render
from DjangoAIO.settings import BASE_DIR
import sqlite3


def fkr(request):
    # TMPRAB
    connection = sqlite3.connect(f"{BASE_DIR / 'FKR.sqlite3'}")
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM TMPRAB')
    tmp_tuples = cursor.fetchall()

    # sprrab
    cursor.execute('SELECT * FROM sprrab')
    sprrab_tuples = cursor.fetchall()

    # sprdom
    cursor.execute('SELECT * FROM sprdom')
    sprdom_tuples = cursor.fetchall()

    # Pays772
    cursor.execute('SELECT * FROM Pays772')
    Pays772_tuples = cursor.fetchall()
    connection.close()

    return render(request, 'fkr.html', {
        'TMPRAB': tmp_tuples,
        'sprrab': sprrab_tuples,
        'sprdom': sprdom_tuples,
        'Pays772': Pays772_tuples,
    })
