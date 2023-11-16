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

    # если ничего не введено
    if people_ls == "" and people_fam == "" and people_imia == "":
        html_table = "🐱‍‍🚀"

    # если введена только фамилия
    elif people_ls == "" and people_fam != "" and people_imia == "":
        sprrab_tuples = for_fkr.sprrab_tuples
        sprdom_tuples = for_fkr.sprdom_tuples

        html_table.append(['Л/счет', 'Фамилия Имя Отчество', 'Город', 'Адрес'])

        for i in sprrab_tuples:
            if (str(i[2]).lower()).startswith(people_fam.lower()):
                for j in sprdom_tuples:
                    if i[5] == j[1] and i[6] == j[3] and i[7] == j[5]:
                        html_table.append([i[1], f"{i[2]} {i[3]} {i[4]}", j[2], f"{j[4]}, д {j[5]}, кв {i[8]}"])

    # Если введены фамилия и имя
    elif people_ls == "" and people_fam != "" and people_imia != "":
        sprrab_tuples = for_fkr.sprrab_tuples
        sprdom_tuples = for_fkr.sprdom_tuples

        html_table = []
        html_table.append(['Л/счет', 'Фамилия Имя Отчество', 'Город', 'Адрес'])

        for i in sprrab_tuples:
            if (str(i[2]).lower()).startswith(people_fam.lower()) and (str(i[3]).lower()).startswith(people_imia.lower()):
                for j in sprdom_tuples:
                    if i[5] == j[1] and i[6] == j[3] and i[7] == j[5]:
                        html_table.append([i[1], f"{i[2]} {i[3]} {i[4]}", j[2], f"{j[4]}, д {j[5]}, кв {i[8]}"])

    # если введен лицевой счет
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

        pay_table.append([
            "Год, месяц",
            "Сальдо на начало месяца",
            "Начислено",
            "Оплачено",
            "Долг (Кол-во мес.)",
            "Субсидия"])

        # Pay772-01-2023
        Pay772_01_2023 = for_fkr.Pay772_01_2023
        subs0123 = for_fkr.subs0123
        subs_temp = 0

        for i in subs0123:
            if str(client_ls) == str(i[0]):
                subs_temp = i[2]

        for i in Pay772_01_2023:
            if client_ls == i[1]:
                if i[11] is None:
                    temp = '0'
                    pay_table.append([i[2], i[3], i[4], i[5], temp, subs_temp])
                else:
                    pay_table.append([i[2], i[3], i[4], i[5], i[11], subs_temp])
                break

        # Pay772-02-2023
        Pay772_02_2023 = for_fkr.Pay772_02_2023
        subs0223 = for_fkr.subs0223
        subs_temp = 0

        for i in subs0223:
            if str(client_ls) == str(i[0]):
                subs_temp = i[2]

        for i in Pay772_02_2023:
            if client_ls == i[1]:
                if i[11] is None:
                    temp = '0'
                    pay_table.append([i[2], i[3], i[4], i[5], temp, subs_temp])
                else:
                    pay_table.append([i[2], i[3], i[4], i[5], i[11], subs_temp])
                break

        # Pay772-03-2023
        Pay772_03_2023 = for_fkr.Pay772_03_2023
        subs0323 = for_fkr.subs0323
        subs_temp = 0

        for i in subs0323:
            if str(client_ls) == str(i[0]):
                subs_temp = i[2]

        for i in Pay772_03_2023:
            if client_ls == i[1]:
                if i[11] is None:
                    temp = '0'
                    pay_table.append([i[2], i[3], i[4], i[5], temp, subs_temp])
                else:
                    pay_table.append([i[2], i[3], i[4], i[5], i[11], subs_temp])
                break

        # Pay772-04-2023
        Pay772_04_2023 = for_fkr.Pay772_04_2023
        subs0423 = for_fkr.subs0423
        subs_temp = 0

        for i in subs0423:
            if str(client_ls) == str(i[0]):
                subs_temp = i[2]

        for i in Pay772_04_2023:
            if client_ls == i[1]:
                if i[11] is None:
                    temp = '0'
                    pay_table.append([i[2], i[3], i[4], i[5], temp, subs_temp])
                else:
                    pay_table.append([i[2], i[3], i[4], i[5], i[11], subs_temp])
                break

        # Pay772-05-2023
        Pay772_05_2023 = for_fkr.Pay772_05_2023
        subs0523 = for_fkr.subs0523
        subs_temp = 0

        for i in subs0523:
            if str(client_ls) == str(i[0]):
                subs_temp = i[2]

        for i in Pay772_05_2023:
            if client_ls == i[1]:
                if i[11] is None:
                    temp = '0'
                    pay_table.append([i[2], i[3], i[4], i[5], temp, subs_temp])
                else:
                    pay_table.append([i[2], i[3], i[4], i[5], i[11], subs_temp])
                break

        # Pay772-06-2023
        Pay772_06_2023 = for_fkr.Pay772_06_2023
        subs0623 = for_fkr.subs0623
        subs_temp = 0

        for i in subs0623:
            if str(client_ls) == str(i[0]):
                subs_temp = i[2]

        for i in Pay772_06_2023:
            if client_ls == i[1]:
                if i[11] is None:
                    temp = '0'
                    pay_table.append([i[2], i[3], i[4], i[5], temp, subs_temp])
                else:
                    pay_table.append([i[2], i[3], i[4], i[5], i[11], subs_temp])
                break

        # Pay772-07-2023
        Pay772_07_2023 = for_fkr.Pay772_07_2023
        subs0723 = for_fkr.subs0723
        subs_temp = 0

        for i in subs0723:
            if str(client_ls) == str(i[0]):
                subs_temp = i[2]

        for i in Pay772_07_2023:
            if client_ls == i[1]:
                if i[11] is None:
                    temp = '0'
                    pay_table.append([i[2], i[3], i[4], i[5], temp, subs_temp])
                else:
                    pay_table.append([i[2], i[3], i[4], i[5], i[11], subs_temp])
                break

        # Pay772-08-2023
        Pay772_08_2023 = for_fkr.Pay772_08_2023
        subs0823 = for_fkr.subs0823
        subs_temp = 0

        for i in subs0823:
            if str(client_ls) == str(i[0]):
                subs_temp = i[2]

        for i in Pay772_08_2023:
            if client_ls == i[1]:
                if i[11] is None:
                    temp = '0'
                    pay_table.append([i[2], i[3], i[4], i[5], temp, subs_temp])
                else:
                    pay_table.append([i[2], i[3], i[4], i[5], i[11], subs_temp])
                break

        # Pay772-09-2023
        Pay772_09_2023 = for_fkr.Pay772_09_2023
        subs0923 = for_fkr.subs0923
        subs_temp = 0

        for i in subs0923:
            if str(client_ls) == str(i[0]):
                subs_temp = i[2]

        for i in Pay772_09_2023:
            if client_ls == i[1]:
                if i[11] is None:
                    temp = '0'
                    pay_table.append([i[2], i[3], i[4], i[5], temp, subs_temp])
                else:
                    pay_table.append([i[2], i[3], i[4], i[5], i[11], subs_temp])
                break

        # Pay772-10-2023
        Pay772_10_2023 = for_fkr.Pay772_10_2023
        subs1023 = for_fkr.subs1023
        subs_temp = 0

        for i in subs1023:
            if str(client_ls) == str(i[0]):
                subs_temp = i[2]

        for i in Pay772_10_2023:
            if client_ls == i[1]:
                if i[11] is None:
                    temp = '0'
                    pay_table.append([i[2], i[3], i[4], i[5], temp, subs_temp])
                else:
                    pay_table.append([i[2], i[3], i[4], i[5], i[11], subs_temp])
                break

    specialist_stamp = ["М П", "Специалист ОСЗН"]

    return render(request, 'fkr.html', {
        'html_table': html_table,
        'statement_info': statement_info,
        'pay_table': pay_table,
        'specialist_stamp': specialist_stamp,
        'other_owners': other_owners,
    })
