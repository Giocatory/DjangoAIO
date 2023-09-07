from django.http import HttpResponse
from django.shortcuts import render
from DjangoAIO.settings import BASE_DIR
import sqlite3


def fkr(request):
    # connection = sqlite3.connect(f"{BASE_DIR / 'FKR.sqlite3'}")
    # cursor = connection.cursor()
    # cursor.execute('SELECT * FROM sprrab')
    # sprrab_tuples = cursor.fetchall()
    # connection.close()

    # create table
    html_table = []
    statement_info = []
    pay_table = []

    people_ls = request.POST.get("supplier-ls")
    people_fam = request.POST.get("supplier-fam")
    people_imia = request.POST.get("supplier-imia")

    if people_ls == "" and people_fam == "" and people_imia == "":
        html_table = "Вы не ввели данные для поиска"
    elif people_ls == "" and people_fam != "" and people_imia == "":
        html_table.append(['Л/счет', 'Фамилия Имя Отчество'])
        connection = sqlite3.connect(f"{BASE_DIR / 'FKR.sqlite3'}")
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM sprrab')
        sprrab_tuples = cursor.fetchall()
        connection.close()
        for i in sprrab_tuples:
            if str(i[2]).lower() == people_fam.lower():
                html_table.append([i[1], f"{i[2]} {i[3]} {i[4]}"])
    elif people_ls == "" and people_fam != "" and people_imia != "":
        html_table.clear()
        html_table.append(['Л/счет', 'Фамилия Имя Отчество'])
        connection = sqlite3.connect(f"{BASE_DIR / 'FKR.sqlite3'}")
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM sprrab')
        sprrab_tuples = cursor.fetchall()
        connection.close()
        for i in sprrab_tuples:
            if str(i[2]).lower() == people_fam.lower() and str(i[3]).lower() == people_imia.lower():
                html_table.append([i[1], f"{i[2]} {i[3]} {i[4]}"])
    elif people_ls != "":
        connection = sqlite3.connect(f"{BASE_DIR / 'FKR.sqlite3'}")
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM sprrab')
        sprrab_tuples = cursor.fetchall()
        connection.close()

        connection = sqlite3.connect(f"{BASE_DIR / 'FKR.sqlite3'}")
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM sprdom')
        sprdom_tuples = cursor.fetchall()
        connection.close()

        statement_info.clear()
        statement_info.append('НО "Фонд капитального ремонта"')

        for i in sprrab_tuples:
            if str(i[1]) == people_ls:
                statement_info.append(f"Л/счет: {i[1]}")
                statement_info.append(f"ФИО: {i[2]} {i[3]} {i[4]}")
                statement_info.append(f"Площадь общая: {i[9]}")
                statement_info.append(f"Тариф на капитальный ремонт: {i[11]}")

                for j in sprdom_tuples:
                    if i[5] == j[1] and i[6] == j[3] and i[7] == j[5]:
                        statement_info.append(f"Адрес: {j[2]} {j[4]} дом {j[5]} кв {i[8]}")

    return render(request, 'fkr.html', {
        'html_table': html_table,
        'statement_info': statement_info,
        'pay_table': pay_table,
    })
