from functools import lru_cache
from django.shortcuts import render

import for_fkr
from DjangoAIO.settings import BASE_DIR
import sqlite3


@lru_cache(maxsize=None)
def fkr(request):
    # create table
    html_table = []
    statement_info = []
    pay_table = []
    client_ls = None
    other_owners = [["ФИО", "Доля"]]

    people_ls = request.POST.get("supplier-ls")
    people_fam = request.POST.get("supplier-fam")
    people_imia = request.POST.get("supplier-imia")

    if people_ls == "" and people_fam == "" and people_imia == "":
        html_table = "🐱‍‍🚀"
    elif people_ls == "" and people_fam != "" and people_imia == "":
        sprrab_tuples = for_fkr.sprrab_tuples

        for i in sprrab_tuples:
            if str(i[2]).lower() == people_fam.lower():
                html_table.append([i[1], f"{i[2]} {i[3]} {i[4]}"])
    elif people_ls == "" and people_fam != "" and people_imia != "":
        html_table.clear()
        html_table.append(['Л/счет', 'Фамилия Имя Отчество'])
        sprrab_tuples = for_fkr.sprrab_tuples

        for i in sprrab_tuples:
            if str(i[2]).lower() == people_fam.lower() and str(i[3]).lower() == people_imia.lower():
                html_table.append([i[1], f"{i[2]} {i[3]} {i[4]}"])
    elif people_ls != "":
        sprrab_tuples = for_fkr.sprrab_tuples
        sprdom_tuples = for_fkr.sprdom_tuples

        statement_info = []
        statement_info.append('НО "Фонд капитального ремонта"')

        for i in sprrab_tuples:
            if str(i[1]) == people_ls:
                statement_info.append(f"Л/счет: {i[1]}")
                client_ls = i[1]
                statement_info.append(f"ФИО: {i[2]} {i[3]} {i[4]}")
                statement_info.append(f"Площадь общая: {i[9]}")
                statement_info.append(f"Тариф на капитальный ремонт: {i[11]}")

                for j in sprdom_tuples:
                    if i[5] == j[1] and i[6] == j[3] and i[7] == j[5]:
                        statement_info.append(f"Адрес: город - {j[2]}, улица - {j[4]}, дом {j[5]}, кв {i[8]}")

                if i[10] is None or i[10] == "1":
                    continue
                elif i[12] is None or i[13] is None or i[14] is None:
                    continue
                else:
                    other_owners.append([f"{i[12]} {i[13]} {i[14]}", f"{i[10]}"])
                if i[15] is None or i[15] == "1":
                    continue
                elif i[16] is None or i[17] is None or i[18] is None:
                    continue
                else:
                    other_owners.append([f"{i[16]} {i[17]} {i[18]}", f"{i[15]}"])
                if i[19] is None or i[19] == "1":
                    continue
                elif i[20] is None or i[21] is None or i[22] is None:
                    continue
                else:
                    other_owners.append([f"{i[20]} {i[21]} {i[22]}", f"{i[19]}"])
                if i[23] is None or i[23] == "1":
                    continue
                elif i[24] is None or i[25] is None or i[26] is None:
                    continue
                else:
                    other_owners.append([f"{i[24]} {i[25]} {i[26]}", f"{i[23]}"])
                if i[27] is None or i[27] == "1":
                    continue
                elif i[28] is None or i[29] is None or i[30] is None:
                    continue
                else:
                    other_owners.append([f"{i[28]} {i[29]} {i[30]}", f"{i[27]}"])
                if i[31] is None or i[31] == "1":
                    continue
                elif i[32] is None or i[33] is None or i[34] is None:
                    continue
                else:
                    other_owners.append([f"{i[32]} {i[33]} {i[34]}", f"{i[31]}"])
                if i[35] is None or i[35] == "1":
                    continue
                elif i[36] is None or i[37] is None or i[38] is None:
                    continue
                else:
                    other_owners.append([f"{i[36]} {i[37]} {i[38]}", f"{i[35]}"])
                if i[39] is None or i[39] == "1":
                    continue
                elif i[40] is None or i[41] is None or i[42] is None:
                    continue
                else:
                    other_owners.append([f"{i[40]} {i[41]} {i[42]}", f"{i[39]}"])
                if i[43] is None or i[43] == "1":
                    continue
                elif i[44] is None or i[45] is None or i[46] is None:
                    continue
                else:
                    other_owners.append([f"{i[44]} {i[45]} {i[46]}", f"{i[43]}"])

        statement_info.append("Другие собственники:")

        pay_table.append(["Год, месяц", "Сальдо на начало месяца", "Начислено", "Оплачено", "Долг (Кол-во мес.)"])

        # Pay772-01-2023
        Pay772_01_2023 = for_fkr.Pay772_01_2023

        for i in Pay772_01_2023:
            if client_ls == i[1]:
                if i[11] is None:
                    temp = '0'
                    pay_table.append([i[2], i[3], i[4], i[5], temp])
                else:
                    pay_table.append([i[2], i[3], i[4], i[5], i[11]])
                break

        # Pay772-02-2023
        Pay772_02_2023 = for_fkr.Pay772_02_2023

        for i in Pay772_02_2023:
            if client_ls == i[1]:
                if i[11] is None:
                    temp = '0'
                    pay_table.append([i[2], i[3], i[4], i[5], temp])
                else:
                    pay_table.append([i[2], i[3], i[4], i[5], i[11]])
                break

        # Pay772-03-2023
        Pay772_03_2023 = for_fkr.Pay772_03_2023

        for i in Pay772_03_2023:
            if client_ls == i[1]:
                if i[11] is None:
                    temp = '0'
                    pay_table.append([i[2], i[3], i[4], i[5], temp])
                else:
                    pay_table.append([i[2], i[3], i[4], i[5], i[11]])
                break

        # Pay772-04-2023
        Pay772_04_2023 = for_fkr.Pay772_04_2023

        for i in Pay772_04_2023:
            if client_ls == i[1]:
                if i[11] is None:
                    temp = '0'
                    pay_table.append([i[2], i[3], i[4], i[5], temp])
                else:
                    pay_table.append([i[2], i[3], i[4], i[5], i[11]])
                break

        # Pay772-05-2023
        Pay772_05_2023 = for_fkr.Pay772_05_2023

        for i in Pay772_05_2023:
            if client_ls == i[1]:
                if i[11] is None:
                    temp = '0'
                    pay_table.append([i[2], i[3], i[4], i[5], temp])
                else:
                    pay_table.append([i[2], i[3], i[4], i[5], i[11]])
                break

        # Pay772-06-2023
        Pay772_06_2023 = for_fkr.Pay772_06_2023

        for i in Pay772_06_2023:
            if client_ls == i[1]:
                if i[11] is None:
                    temp = '0'
                    pay_table.append([i[2], i[3], i[4], i[5], temp])
                else:
                    pay_table.append([i[2], i[3], i[4], i[5], i[11]])
                break

        # Pay772-07-2023
        Pay772_07_2023 = for_fkr.Pay772_07_2023

        for i in Pay772_07_2023:
            if client_ls == i[1]:
                if i[11] is None:
                    temp = '0'
                    pay_table.append([i[2], i[3], i[4], i[5], temp])
                else:
                    pay_table.append([i[2], i[3], i[4], i[5], i[11]])
                break

        # Pay772-08-2023
        Pay772_08_2023 = for_fkr.Pay772_08_2023

        for i in Pay772_08_2023:
            if client_ls == i[1]:
                if i[11] is None:
                    temp = '0'
                    pay_table.append([i[2], i[3], i[4], i[5], temp])
                else:
                    pay_table.append([i[2], i[3], i[4], i[5], i[11]])
                break

    specialist_stamp = ["М П", "Специалист ОСЗН"]

    return render(request, 'fkr.html', {
        'html_table': html_table,
        'statement_info': statement_info,
        'pay_table': pay_table,
        'specialist_stamp': specialist_stamp,
        'other_owners': other_owners,
    })
