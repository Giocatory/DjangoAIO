from functools import lru_cache
from django.shortcuts import render
from DjangoAIO.settings import BASE_DIR
import sqlite3


@lru_cache(maxsize=None)
def eko(request):
    # create table
    html_table = []
    statement_info = []
    pay_table = []

    people_ls = request.POST.get("supplier-ls")
    people_fam = request.POST.get("supplier-fam")
    people_imia = request.POST.get("supplier-imia")

    # connection = sqlite3.connect(f"{BASE_DIR / 'EKO.sqlite3'}")
    # cursor = connection.cursor()
    # cursor.execute('SELECT * FROM sprrab')
    # sprrab_tuples = cursor.fetchall()
    # connection.close()

    if people_ls == "" and people_fam == "" and people_imia == "":
        html_table = "🐱‍‍🚀"
    elif people_ls == "" and people_fam != "" and people_imia == "":
        pass
    elif people_ls == "" and people_fam != "" and people_imia != "":
        pass
    elif people_ls != "":
        pass

    return render(request, 'eko.html', {
        'html_table': html_table,
        'statement_info': statement_info,
        'pay_table': pay_table,
    })
