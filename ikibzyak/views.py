from functools import lru_cache
from django.shortcuts import render

from jku import for_ikibzyak


@lru_cache(maxsize=None)
def ikibzyak(request):
    # create tables
    search_table = []
    statement_info = []
    html_table = []
    fact_info = []
    pay_table = []

    # global variables
    all_sum_opl = 0
    all_sum_nach = 0

    people_ls = request.POST.get("supplier-ls")
    people_fam = request.POST.get("supplier-fam")
    people_imia = request.POST.get("supplier-imia")

    if people_ls == "" and people_fam == "" and people_imia == "":
        html_table = "----"

    # Если введена только фамилия
    elif people_ls == "" and people_fam != "" and people_imia == "":
        search_table = []
        search_table.append(['Л/счет', 'Фамилия Имя Отчество', 'Адрес'])
        s_tuple = for_ikibzyak.s0123

        for i in s_tuple:
            if (str(i[2]).lower()).startswith(people_fam.lower()):
                search_table.append([i[1], f"{i[2]} {i[3]} {i[4]}", f"ул. {i[7]}, д. {i[8]}, кв. {i[9]}"])

    # Если введена фамилия и имя
    elif people_ls == "" and people_fam != "" and people_imia != "":
        search_table = []
        search_table.append(['Л/счет', 'Фамилия Имя Отчество', 'Адрес'])
        s_tuple = for_ikibzyak.s0123

        for i in s_tuple:
            if (str(i[2]).lower()).startswith(people_fam.lower()) and (str(i[3]).lower()).startswith(
                    people_imia.lower()):
                search_table.append([i[1], f"{i[2]} {i[3]} {i[4]}", f"ул. {i[7]}, д. {i[8]}, кв. {i[9]}"])

    # Если введен лицевой счет
    elif people_ls != "":
        statement_info = []
        html_table = []

        # s1023
        s1023 = for_ikibzyak.s1023

        for i in s1023:
            if people_ls == str(i[1]):
                statement_info.append(f"Л/счет: {i[1]}")
                statement_info.append(f"ФИО: {i[2]} {i[3]} {i[4]}")
                statement_info.append(f"Адрес: ул. {i[7]}, д. {i[8]}, кв. {i[9]}")
                statement_info.append(f"Жилая площадь: {i[10]}")
                statement_info.append(f"Состав семьи: {i[11]}")

        html_table.append([
            "Дата",
            "Теп.Тар",
            "Теп.Потр",
            "Теп.Сумма",
            "Теп.Опл",
            "ХВС.Тар",
            "ХВС.Потр",
            "ХВС.Сумма",
            "ХВС.Опл",
            "ГВС.Тар",
            "ГВС.Потр",
            "ГВС.Сумма",
            "ГВС.Опл",
            "КНС.Тар",
            "КНС.Потр",
            "КНС.Сумма",
            "КНС.Опл",
        ])

        for i in s1023:
            if people_ls == str(i[1]):
                html_table.append([
                    i[38],
                    i[30], i[31], i[32], i[33],
                    i[20], i[21], i[22], i[23],
                    i[25], i[26], i[27], i[28],
                    i[15], i[16], i[17], i[18],
                ])

        # s0923
        s0923 = for_ikibzyak.s0923
        for i in s0923:
            if people_ls == str(i[1]):
                html_table.append([
                    i[38],
                    i[30], i[31], i[32], i[33],
                    i[20], i[21], i[22], i[23],
                    i[25], i[26], i[27], i[28],
                    i[15], i[16], i[17], i[18],
                ])

        # s0823
        s0823 = for_ikibzyak.s0823
        for i in s0823:
            if people_ls == str(i[1]):
                html_table.append([
                    i[38],
                    i[30], i[31], i[32], i[33],
                    i[20], i[21], i[22], i[23],
                    i[25], i[26], i[27], i[28],
                    i[15], i[16], i[17], i[18],
                ])

        # s0723
        s0723 = for_ikibzyak.s0723
        for i in s0723:
            if people_ls == str(i[1]):
                html_table.append([
                    i[38],
                    i[30], i[31], i[32], i[33],
                    i[20], i[21], i[22], i[23],
                    i[25], i[26], i[27], i[28],
                    i[15], i[16], i[17], i[18],
                ])

        # s0623
        s0623 = for_ikibzyak.s0623
        for i in s0623:
            if people_ls == str(i[1]):
                html_table.append([
                    i[38],
                    i[30], i[31], i[32], i[33],
                    i[20], i[21], i[22], i[23],
                    i[25], i[26], i[27], i[28],
                    i[15], i[16], i[17], i[18],
                ])

        # s0523
        s0523 = for_ikibzyak.s0523
        for i in s0523:
            if people_ls == str(i[1]):
                html_table.append([
                    i[38],
                    i[30], i[31], i[32], i[33],
                    i[20], i[21], i[22], i[23],
                    i[25], i[26], i[27], i[28],
                    i[15], i[16], i[17], i[18],
                ])

        # s0423
        s0423 = for_ikibzyak.s0423
        for i in s0423:
            if people_ls == str(i[1]):
                html_table.append([
                    i[38],
                    i[30], i[31], i[32], i[33],
                    i[20], i[21], i[22], i[23],
                    i[25], i[26], i[27], i[28],
                    i[15], i[16], i[17], i[18],
                ])

        # s0323
        s0323 = for_ikibzyak.s0323
        for i in s0323:
            if people_ls == str(i[1]):
                html_table.append([
                    i[38],
                    i[30], i[31], i[32], i[33],
                    i[20], i[21], i[22], i[23],
                    i[25], i[26], i[27], i[28],
                    i[15], i[16], i[17], i[18],
                ])

        # s0323
        s0323 = for_ikibzyak.s0323
        for i in s0323:
            if people_ls == str(i[1]):
                html_table.append([
                    i[38],
                    i[30], i[31], i[32], i[33],
                    i[20], i[21], i[22], i[23],
                    i[25], i[26], i[27], i[28],
                    i[15], i[16], i[17], i[18],
                ])

        # s0223
        s0223 = for_ikibzyak.s0223
        for i in s0223:
            if people_ls == str(i[1]):
                html_table.append([
                    i[38],
                    i[30], i[31], i[32], i[33],
                    i[20], i[21], i[22], i[23],
                    i[25], i[26], i[27], i[28],
                    i[15], i[16], i[17], i[18],
                ])

        # s0123
        s0123 = for_ikibzyak.s0123
        for i in s0123:
            if people_ls == str(i[1]):
                html_table.append([
                    i[38],
                    i[30], i[31], i[32], i[33],
                    i[20], i[21], i[22], i[23],
                    i[25], i[26], i[27], i[28],
                    i[15], i[16], i[17], i[18],
                ])

        # s1222
        s1222 = for_ikibzyak.s1222
        for i in s1222:
            if people_ls == str(i[1]):
                html_table.append([
                    i[38],
                    i[30], i[31], i[32], i[33],
                    i[20], i[21], i[22], i[23],
                    i[25], i[26], i[27], i[28],
                    i[15], i[16], i[17], i[18],
                ])

        # s1122
        s1122 = for_ikibzyak.s1122
        for i in s1122:
            if people_ls == str(i[1]):
                html_table.append([
                    i[38],
                    i[30], i[31], i[32], i[33],
                    i[20], i[21], i[22], i[23],
                    i[25], i[26], i[27], i[28],
                    i[15], i[16], i[17], i[18],
                ])

        # s1022
        s1022 = for_ikibzyak.s1022
        for i in s1022:
            if people_ls == str(i[1]):
                html_table.append([
                    i[38],
                    i[30], i[31], i[32], i[33],
                    i[20], i[21], i[22], i[23],
                    i[25], i[26], i[27], i[28],
                    i[15], i[16], i[17], i[18],
                ])

        # pay_table
        fact_info = []
        pay_table = []

        pay_tuple = for_ikibzyak.PAY_tuples

        pay_table.append([
            "Дата",  # 2
            "Начало месяца",  # 4
            "Начисленно",  # 5
            "Оплачено",  # 6
            "Долг",  # 3
        ])

        for i in pay_tuple:
            if people_ls == str(i[1]):
                pay_table.append([
                    i[2], i[4], i[5], i[6], i[3]
                ])
                all_sum_opl += float(str(i[6]).replace(",", "."))
                all_sum_nach += float(str(i[5]).replace(",", "."))

        fact_info.append(f"Фактическая оплата за период 2022-10 по 2023-09 составляет {all_sum_opl:.2f}руб.")
        fact_info.append(f"Итого, начислено сумма за период 2022-10 по 2023-09 составляет {all_sum_nach:.2f}руб")

    return render(request, 'ikibzyak.html', {
        'search_table': search_table,
        'statement_info': statement_info,
        'html_table': html_table,
        'fact_info': fact_info,
        'pay_table': pay_table,
    })
