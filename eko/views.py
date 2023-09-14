from functools import lru_cache
from django.shortcuts import render

import for_eko
from DjangoAIO.settings import BASE_DIR
import sqlite3


@lru_cache(maxsize=None)
def eko(request):
    # create table
    html_table = []
    statement_info = []
    pay_table = []
    client_ls = None

    people_ls = request.POST.get("supplier-ls")
    people_fam = request.POST.get("supplier-fam")
    people_imia = request.POST.get("supplier-imia")

    if people_ls == "" and people_fam == "" and people_imia == "":
        html_table = "🐱‍‍🚀"

    # Если введена только фамилия
    elif people_ls == "" and people_fam != "" and people_imia == "":
        html_table.append(['Л/счет', 'Фамилия Имя Отчество', 'Город', 'Адрес'])
        sprrab_tuples = for_eko.sprrab_tuples
        sprdom_tuples = for_eko.sprdom_tuples

        for i in sprrab_tuples:
            if str(i[2]).lower() == people_fam.lower():
                for j in sprdom_tuples:
                    if i[5] == j[1] and i[6] == j[3]:
                        if i[7] is None:
                            temp = ' '
                            html_table.append([i[1], f"{i[2]} {i[3]} {i[4]}", j[2], f"Улица {j[4]}, дом {j[5]}, кв {temp}"])
                        else:
                            html_table.append([i[1], f"{i[2]} {i[3]} {i[4]}", j[2], f"Улица {j[4]}, дом {j[5]}, кв {i[7]}"])

    # Если введена фамилия и имя
    elif people_ls == "" and people_fam != "" and people_imia != "":
        html_table = []
        html_table.append(['Л/счет', 'Фамилия Имя Отчество', 'Город', 'Адрес'])

        sprrab_tuples = for_eko.sprrab_tuples
        sprdom_tuples = for_eko.sprdom_tuples

        for i in sprrab_tuples:
            if str(i[2]).lower() == people_fam.lower() and str(i[3]).lower() == people_imia.lower():
                for j in sprdom_tuples:
                    if i[5] == j[1] and i[6] == j[3]:
                        if i[7] is None:
                            temp = ' '
                            html_table.append(
                                [i[1], f"{i[2]} {i[3]} {i[4]}", j[2], f"Улица {j[4]}, дом {j[5]}, кв {temp}"])
                        else:
                            html_table.append(
                                [i[1], f"{i[2]} {i[3]} {i[4]}", j[2], f"Улица {j[4]}, дом {j[5]}, кв {i[7]}"])

    # Если введен лицевой счет
    elif people_ls != "":
        sprrab_tuples = for_eko.sprrab_tuples
        sprdom_tuples = for_eko.sprdom_tuples

        statement_info = []
        statement_info.append('ООО "Эко-Альянс"')

        for i in sprrab_tuples:
            if str(i[1]) == people_ls:
                statement_info.append(f"Л/счет: {i[1]}")
                client_ls = i[1]
                statement_info.append(f"ФИО: {i[2]} {i[3]} {i[4]}")

                for j in sprdom_tuples:
                    if i[5] == j[1] and i[6] == j[3]:
                        if i[7] is None:
                            temp = ' '
                            statement_info.append(f"Адрес: город - {j[2]}, улица - {j[4]}, дом {j[5]}, кв {temp}")
                        else:
                            statement_info.append(f"Адрес: город - {j[2]}, улица - {j[4]}, дом {j[5]}, кв {i[7]}")
                            statement_info.append(f"")
                        break

                statement_info.append(f"Кол-во проживающих: {i[8]}")
                statement_info.append(f"Тариф: {i[10]}")
                statement_info.append(f"Норм.: {i[11]}")

        pay_table.append(["Год, месяц", "Сальдо на начало месяца", "Начислено", "Оплачено", "Долг (Кол-во мес.)"])

        # Pay979-11-2022
        Pay979_11_2022 = for_eko.Pay979_11_2022

        for i in Pay979_11_2022:
            if client_ls == i[1]:
                pay_table.append([i[2], i[3], i[4], i[5], i[11]])

        # Pay979-12-2022
        Pay979_12_2022 = for_eko.Pay979_12_2022

        for i in Pay979_12_2022:
            if client_ls == i[1]:
                pay_table.append([i[2], i[3], i[4], i[5], i[11]])

        # Pay979-1-2023
        Pay979_1_2023 = for_eko.Pay979_1_2023

        for i in Pay979_1_2023:
            if client_ls == i[1]:
                pay_table.append([i[2], i[3], i[4], i[5], i[11]])

        # Pay979-2-2023
        Pay979_2_2023 = for_eko.Pay979_2_2023

        for i in Pay979_2_2023:
            if client_ls == i[1]:
                pay_table.append([i[2], i[3], i[4], i[5], i[11]])

        # Pay979-3-2023
        Pay979_3_2023 = for_eko.Pay979_3_2023

        for i in Pay979_3_2023:
            if client_ls == i[1]:
                pay_table.append([i[2], i[3], i[4], i[5], i[11]])

        # Pay979-4-2023
        Pay979_4_2023 = for_eko.Pay979_4_2023

        for i in Pay979_4_2023:
            if client_ls == i[1]:
                pay_table.append([i[2], i[3], i[4], i[5], i[11]])

        # Pay979-5-2023
        Pay979_5_2023 = for_eko.Pay979_5_2023

        for i in Pay979_5_2023:
            if client_ls == i[1]:
                pay_table.append([i[2], i[3], i[4], i[5], i[11]])

        # Pay979-6-2023
        Pay979_6_2023 = for_eko.Pay979_6_2023

        for i in Pay979_6_2023:
            if client_ls == i[1]:
                pay_table.append([i[2], i[3], i[4], i[5], i[11]])

        # Pay979-7-2023
        Pay979_7_2023 = for_eko.Pay979_7_2023

        for i in Pay979_7_2023:
            if client_ls == i[1]:
                pay_table.append([i[2], i[3], i[4], i[5], i[11]])

        # Pay979-8-2023
        Pay979_8_2023 = for_eko.Pay979_8_2023

        for i in Pay979_8_2023:
            if client_ls == i[1]:
                pay_table.append([i[2], i[3], i[4], i[5], i[11]])

        # Pay979-9-2023
        Pay979_9_2023 = for_eko.Pay979_9_2023

        for i in Pay979_9_2023:
            if client_ls == i[1]:
                pay_table.append([i[2], i[3], i[4], i[5], i[11]])

    specialist_stamp = ["М П", "Специалист ОСЗН"]

    return render(request, 'eko.html', {
        'html_table': html_table,
        'statement_info': statement_info,
        'pay_table': pay_table,
        'specialist_stamp': specialist_stamp,
    })
