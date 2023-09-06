from django.shortcuts import render
from DjangoAIO.settings import BASE_DIR
import sqlite3


def fkr(request):
    # TMPRAB
    connection = sqlite3.connect(f"{BASE_DIR / 'FKR.sqlite3'}")
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM TMPRAB')
    tmp_tuple = cursor.fetchall()

    # sprrab
    cursor.execute('SELECT * FROM sprrab')
    sprrab_tuple = cursor.fetchall()

    # sprdom
    cursor.execute('SELECT * FROM sprdom')
    sprdom_tuple = cursor.fetchall()

    # Pays772
    cursor.execute('SELECT * FROM Pays772')
    Pays772_tuple = cursor.fetchall()
    connection.close()

    return render(request, 'fkr.html', {
        'TMPRAB': tmp_tuple,
        'sprrab': sprrab_tuple,
        'sprdom': sprdom_tuple,
        'Pays772': Pays772_tuple,
    })
