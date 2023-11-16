from functools import lru_cache
from django.shortcuts import render

from jku import for_tvkom


@lru_cache(maxsize=None)
def tvkom(request):
    # create tables
    search_table = []
    statement_info = []
    html_table = []

    people_ls = request.POST.get("supplier-ls")
    people_fam = request.POST.get("supplier-fam")
    people_imia = request.POST.get("supplier-imia")

    if people_ls == "" and people_fam == "" and people_imia == "":
        html_table = "----"

        # Если введена только фамилия
    elif people_ls == "" and people_fam != "" and people_imia == "":
        search_table = []
        search_table.append(['Л/счет', 'Фамилия Имя Отчество', 'Адрес'])
        s_tuple = for_tvkom.tvk1023g

        for i in s_tuple:
            if (str(i[2]).lower()).startswith(people_fam.lower()):
                search_table.append([i[1], f"{i[2]} {i[3]} {i[4]}", f"ул. {i[5]}, д. {i[6]}, кв. {i[9]}"])

        # Если введена фамилия и имя
    elif people_ls == "" and people_fam != "" and people_imia != "":
        search_table = []
        search_table.append(['Л/счет', 'Фамилия Имя Отчество', 'Адрес'])
        s_tuple = for_tvkom.tvk1023g

        for i in s_tuple:
            if (str(i[2]).lower()).startswith(people_fam.lower()) and (str(i[3]).lower()).startswith(
                    people_imia.lower()):
                search_table.append([i[1], f"{i[2]} {i[3]} {i[4]}", f"ул. {i[5]}, д. {i[6]}, кв. {i[9]}"])

    # Если введен лицевой счет
    elif people_ls != "":
        statement_info = []
        html_table = []

        # tvk1023 - statement
        tvk1023g = for_tvkom.tvk1023g

        for i in tvk1023g:
            if people_ls == str(i[1]):
                statement_info.append(f"ФИО: {i[2]} {i[3]} {i[4]}")
                statement_info.append(f"Л/сч: {i[1]}")
                statement_info.append(f"Адрес: ул. {i[5]}, д. {i[6]}, кв. {i[9]}")
                statement_info.append(f"Жил. площадь: {i[12]}")
                statement_info.append(f"Состав семьи: {i[10]}")

        # html_table
        html_table.append([
            "Дата",
            "ХВС.Тар",
            "ХВС.Потр",
            "ХВС.Сумма",
            "ХВС.Опл",
            "КНС.Тар",
            "КНС.Потр",
            "КНС.Сумма",
            "КНС.Опл",
            "Теп.Тар",
            "Теп.Потр",
            "Теп.Сумма",
            "Теп.Опл",
            "Доп.Теп.Тар",
            "Доп.Теп.Потр",
            "Доп.Теп.Сумма",
            "Доп.Теп.Опл",
        ])

        # tvk1023
        for i in tvk1023g:
            if people_ls == str(i[1]):
                html_table.append([
                    i[0],
                    f"{float(str(i[21]).replace(',', '.')):.2f}",
                    f"{float(str(i[22]).replace(',', '.')):.2f}",
                    f"{float(str(i[23]).replace(',', '.')):.2f}",
                    f"{float(str(i[24]).replace(',', '.')):.2f}",
                    f"{float(str(i[25]).replace(',', '.')):.2f}",
                    f"{float(str(i[26]).replace(',', '.')):.2f}",
                    f"{float(str(i[27]).replace(',', '.')):.2f}",
                    f"{float(str(i[28]).replace(',', '.')):.2f}",
                    f"{float(str(i[17]).replace(',', '.')):.2f}",
                    f"{float(str(i[18]).replace(',', '.')):.2f}",
                    f"{float(str(i[19]).replace(',', '.')):.2f}",
                    f"{float(str(i[20]).replace(',', '.')):.2f}",
                    f"{float(str(i[29]).replace(',', '.')):.2f}",
                    f"{float(str(i[30]).replace(',', '.')):.2f}",
                    f"{float(str(i[31]).replace(',', '.')):.2f}",
                    f"{float(str(i[32]).replace(',', '.')):.2f}",
                ])

        # tvk0923g
        tvk0923g = for_tvkom.tvk0923g

        for i in tvk0923g:
            if people_ls == str(i[1]):
                html_table.append([
                    i[0],
                    f"{float(str(i[21]).replace(',', '.')):.2f}",
                    f"{float(str(i[22]).replace(',', '.')):.2f}",
                    f"{float(str(i[23]).replace(',', '.')):.2f}",
                    f"{float(str(i[24]).replace(',', '.')):.2f}",
                    f"{float(str(i[25]).replace(',', '.')):.2f}",
                    f"{float(str(i[26]).replace(',', '.')):.2f}",
                    f"{float(str(i[27]).replace(',', '.')):.2f}",
                    f"{float(str(i[28]).replace(',', '.')):.2f}",
                    f"{float(str(i[17]).replace(',', '.')):.2f}",
                    f"{float(str(i[18]).replace(',', '.')):.2f}",
                    f"{float(str(i[19]).replace(',', '.')):.2f}",
                    f"{float(str(i[20]).replace(',', '.')):.2f}",
                    f"{float(str(i[29]).replace(',', '.')):.2f}",
                    f"{float(str(i[30]).replace(',', '.')):.2f}",
                    f"{float(str(i[31]).replace(',', '.')):.2f}",
                    f"{float(str(i[32]).replace(',', '.')):.2f}",
                ])

        # tvk0823g
        tvk0823g = for_tvkom.tvk0823g

        for i in tvk0823g:
            if people_ls == str(i[1]):
                html_table.append([
                    i[0],
                    f"{float(str(i[21]).replace(',', '.')):.2f}",
                    f"{float(str(i[22]).replace(',', '.')):.2f}",
                    f"{float(str(i[23]).replace(',', '.')):.2f}",
                    f"{float(str(i[24]).replace(',', '.')):.2f}",
                    f"{float(str(i[25]).replace(',', '.')):.2f}",
                    f"{float(str(i[26]).replace(',', '.')):.2f}",
                    f"{float(str(i[27]).replace(',', '.')):.2f}",
                    f"{float(str(i[28]).replace(',', '.')):.2f}",
                    f"{float(str(i[17]).replace(',', '.')):.2f}",
                    f"{float(str(i[18]).replace(',', '.')):.2f}",
                    f"{float(str(i[19]).replace(',', '.')):.2f}",
                    f"{float(str(i[20]).replace(',', '.')):.2f}",
                    f"{float(str(i[29]).replace(',', '.')):.2f}",
                    f"{float(str(i[30]).replace(',', '.')):.2f}",
                    f"{float(str(i[31]).replace(',', '.')):.2f}",
                    f"{float(str(i[32]).replace(',', '.')):.2f}",
                ])

        # tvk0723g
        tvk0723g = for_tvkom.tvk0723g

        for i in tvk0723g:
            if people_ls == str(i[1]):
                html_table.append([
                    i[0],
                    f"{float(str(i[21]).replace(',', '.')):.2f}",
                    f"{float(str(i[22]).replace(',', '.')):.2f}",
                    f"{float(str(i[23]).replace(',', '.')):.2f}",
                    f"{float(str(i[24]).replace(',', '.')):.2f}",
                    f"{float(str(i[25]).replace(',', '.')):.2f}",
                    f"{float(str(i[26]).replace(',', '.')):.2f}",
                    f"{float(str(i[27]).replace(',', '.')):.2f}",
                    f"{float(str(i[28]).replace(',', '.')):.2f}",
                    f"{float(str(i[17]).replace(',', '.')):.2f}",
                    f"{float(str(i[18]).replace(',', '.')):.2f}",
                    f"{float(str(i[19]).replace(',', '.')):.2f}",
                    f"{float(str(i[20]).replace(',', '.')):.2f}",
                    f"{float(str(i[29]).replace(',', '.')):.2f}",
                    f"{float(str(i[30]).replace(',', '.')):.2f}",
                    f"{float(str(i[31]).replace(',', '.')):.2f}",
                    f"{float(str(i[32]).replace(',', '.')):.2f}",
                ])

        # tvk0623g
        tvk0623g = for_tvkom.tvk0623g

        for i in tvk0623g:
            if people_ls == str(i[1]):
                html_table.append([
                    i[0],
                    f"{float(str(i[21]).replace(',', '.')):.2f}",
                    f"{float(str(i[22]).replace(',', '.')):.2f}",
                    f"{float(str(i[23]).replace(',', '.')):.2f}",
                    f"{float(str(i[24]).replace(',', '.')):.2f}",
                    f"{float(str(i[25]).replace(',', '.')):.2f}",
                    f"{float(str(i[26]).replace(',', '.')):.2f}",
                    f"{float(str(i[27]).replace(',', '.')):.2f}",
                    f"{float(str(i[28]).replace(',', '.')):.2f}",
                    f"{float(str(i[17]).replace(',', '.')):.2f}",
                    f"{float(str(i[18]).replace(',', '.')):.2f}",
                    f"{float(str(i[19]).replace(',', '.')):.2f}",
                    f"{float(str(i[20]).replace(',', '.')):.2f}",
                    f"{float(str(i[29]).replace(',', '.')):.2f}",
                    f"{float(str(i[30]).replace(',', '.')):.2f}",
                    f"{float(str(i[31]).replace(',', '.')):.2f}",
                    f"{float(str(i[32]).replace(',', '.')):.2f}",
                ])

        # tvk0523g
        tvk0523g = for_tvkom.tvk0523g

        for i in tvk0523g:
            if people_ls == str(i[1]):
                html_table.append([
                    i[0],
                    f"{float(str(i[21]).replace(',', '.')):.2f}",
                    f"{float(str(i[22]).replace(',', '.')):.2f}",
                    f"{float(str(i[23]).replace(',', '.')):.2f}",
                    f"{float(str(i[24]).replace(',', '.')):.2f}",
                    f"{float(str(i[25]).replace(',', '.')):.2f}",
                    f"{float(str(i[26]).replace(',', '.')):.2f}",
                    f"{float(str(i[27]).replace(',', '.')):.2f}",
                    f"{float(str(i[28]).replace(',', '.')):.2f}",
                    f"{float(str(i[17]).replace(',', '.')):.2f}",
                    f"{float(str(i[18]).replace(',', '.')):.2f}",
                    f"{float(str(i[19]).replace(',', '.')):.2f}",
                    f"{float(str(i[20]).replace(',', '.')):.2f}",
                    f"{float(str(i[29]).replace(',', '.')):.2f}",
                    f"{float(str(i[30]).replace(',', '.')):.2f}",
                    f"{float(str(i[31]).replace(',', '.')):.2f}",
                    f"{float(str(i[32]).replace(',', '.')):.2f}",
                ])

        # tvk0423g
        tvk0423g = for_tvkom.tvk0423g

        for i in tvk0423g:
            if people_ls == str(i[1]):
                html_table.append([
                    i[0],
                    f"{float(str(i[21]).replace(',', '.')):.2f}",
                    f"{float(str(i[22]).replace(',', '.')):.2f}",
                    f"{float(str(i[23]).replace(',', '.')):.2f}",
                    f"{float(str(i[24]).replace(',', '.')):.2f}",
                    f"{float(str(i[25]).replace(',', '.')):.2f}",
                    f"{float(str(i[26]).replace(',', '.')):.2f}",
                    f"{float(str(i[27]).replace(',', '.')):.2f}",
                    f"{float(str(i[28]).replace(',', '.')):.2f}",
                    f"{float(str(i[17]).replace(',', '.')):.2f}",
                    f"{float(str(i[18]).replace(',', '.')):.2f}",
                    f"{float(str(i[19]).replace(',', '.')):.2f}",
                    f"{float(str(i[20]).replace(',', '.')):.2f}",
                    f"{float(str(i[29]).replace(',', '.')):.2f}",
                    f"{float(str(i[30]).replace(',', '.')):.2f}",
                    f"{float(str(i[31]).replace(',', '.')):.2f}",
                    f"{float(str(i[32]).replace(',', '.')):.2f}",
                ])

        # tvk0323g
        tvk0323g = for_tvkom.tvk0323g

        for i in tvk0323g:
            if people_ls == str(i[1]):
                html_table.append([
                    i[0],
                    f"{float(str(i[21]).replace(',', '.')):.2f}",
                    f"{float(str(i[22]).replace(',', '.')):.2f}",
                    f"{float(str(i[23]).replace(',', '.')):.2f}",
                    f"{float(str(i[24]).replace(',', '.')):.2f}",
                    f"{float(str(i[25]).replace(',', '.')):.2f}",
                    f"{float(str(i[26]).replace(',', '.')):.2f}",
                    f"{float(str(i[27]).replace(',', '.')):.2f}",
                    f"{float(str(i[28]).replace(',', '.')):.2f}",
                    f"{float(str(i[17]).replace(',', '.')):.2f}",
                    f"{float(str(i[18]).replace(',', '.')):.2f}",
                    f"{float(str(i[19]).replace(',', '.')):.2f}",
                    f"{float(str(i[20]).replace(',', '.')):.2f}",
                    f"{float(str(i[29]).replace(',', '.')):.2f}",
                    f"{float(str(i[30]).replace(',', '.')):.2f}",
                    f"{float(str(i[31]).replace(',', '.')):.2f}",
                    f"{float(str(i[32]).replace(',', '.')):.2f}",
                ])

        # tvk0223g
        tvk0223g = for_tvkom.tvk0223g

        for i in tvk0223g:
            if people_ls == str(i[1]):
                html_table.append([
                    i[0],
                    f"{float(str(i[21]).replace(',', '.')):.2f}",
                    f"{float(str(i[22]).replace(',', '.')):.2f}",
                    f"{float(str(i[23]).replace(',', '.')):.2f}",
                    f"{float(str(i[24]).replace(',', '.')):.2f}",
                    f"{float(str(i[25]).replace(',', '.')):.2f}",
                    f"{float(str(i[26]).replace(',', '.')):.2f}",
                    f"{float(str(i[27]).replace(',', '.')):.2f}",
                    f"{float(str(i[28]).replace(',', '.')):.2f}",
                    f"{float(str(i[17]).replace(',', '.')):.2f}",
                    f"{float(str(i[18]).replace(',', '.')):.2f}",
                    f"{float(str(i[19]).replace(',', '.')):.2f}",
                    f"{float(str(i[20]).replace(',', '.')):.2f}",
                    f"{float(str(i[29]).replace(',', '.')):.2f}",
                    f"{float(str(i[30]).replace(',', '.')):.2f}",
                    f"{float(str(i[31]).replace(',', '.')):.2f}",
                    f"{float(str(i[32]).replace(',', '.')):.2f}",
                ])

        # tvk0123g
        tvk0123g = for_tvkom.tvk0123g

        for i in tvk0123g:
            if people_ls == str(i[1]):
                html_table.append([
                    i[0],
                    f"{float(str(i[21]).replace(',', '.')):.2f}",
                    f"{float(str(i[22]).replace(',', '.')):.2f}",
                    f"{float(str(i[23]).replace(',', '.')):.2f}",
                    f"{float(str(i[24]).replace(',', '.')):.2f}",
                    f"{float(str(i[25]).replace(',', '.')):.2f}",
                    f"{float(str(i[26]).replace(',', '.')):.2f}",
                    f"{float(str(i[27]).replace(',', '.')):.2f}",
                    f"{float(str(i[28]).replace(',', '.')):.2f}",
                    f"{float(str(i[17]).replace(',', '.')):.2f}",
                    f"{float(str(i[18]).replace(',', '.')):.2f}",
                    f"{float(str(i[19]).replace(',', '.')):.2f}",
                    f"{float(str(i[20]).replace(',', '.')):.2f}",
                    f"{float(str(i[29]).replace(',', '.')):.2f}",
                    f"{float(str(i[30]).replace(',', '.')):.2f}",
                    f"{float(str(i[31]).replace(',', '.')):.2f}",
                    f"{float(str(i[32]).replace(',', '.')):.2f}",
                ])

        # tvk1222g
        tvk1222g = for_tvkom.tvk1222g

        for i in tvk1222g:
            if people_ls == str(i[1]):
                html_table.append([
                    i[0],
                    f"{float(str(i[21]).replace(',', '.')):.2f}",
                    f"{float(str(i[22]).replace(',', '.')):.2f}",
                    f"{float(str(i[23]).replace(',', '.')):.2f}",
                    f"{float(str(i[24]).replace(',', '.')):.2f}",
                    f"{float(str(i[25]).replace(',', '.')):.2f}",
                    f"{float(str(i[26]).replace(',', '.')):.2f}",
                    f"{float(str(i[27]).replace(',', '.')):.2f}",
                    f"{float(str(i[28]).replace(',', '.')):.2f}",
                    f"{float(str(i[17]).replace(',', '.')):.2f}",
                    f"{float(str(i[18]).replace(',', '.')):.2f}",
                    f"{float(str(i[19]).replace(',', '.')):.2f}",
                    f"{float(str(i[20]).replace(',', '.')):.2f}",
                    f"{float(str(i[29]).replace(',', '.')):.2f}",
                    f"{float(str(i[30]).replace(',', '.')):.2f}",
                    f"{float(str(i[31]).replace(',', '.')):.2f}",
                    f"{float(str(i[32]).replace(',', '.')):.2f}",
                ])

        # tvk1122g
        tvk1122g = for_tvkom.tvk1122g

        for i in tvk1122g:
            if people_ls == str(i[1]):
                html_table.append([
                    i[0],
                    f"{float(str(i[21]).replace(',', '.')):.2f}",
                    f"{float(str(i[22]).replace(',', '.')):.2f}",
                    f"{float(str(i[23]).replace(',', '.')):.2f}",
                    f"{float(str(i[24]).replace(',', '.')):.2f}",
                    f"{float(str(i[25]).replace(',', '.')):.2f}",
                    f"{float(str(i[26]).replace(',', '.')):.2f}",
                    f"{float(str(i[27]).replace(',', '.')):.2f}",
                    f"{float(str(i[28]).replace(',', '.')):.2f}",
                    f"{float(str(i[17]).replace(',', '.')):.2f}",
                    f"{float(str(i[18]).replace(',', '.')):.2f}",
                    f"{float(str(i[19]).replace(',', '.')):.2f}",
                    f"{float(str(i[20]).replace(',', '.')):.2f}",
                    f"{float(str(i[29]).replace(',', '.')):.2f}",
                    f"{float(str(i[30]).replace(',', '.')):.2f}",
                    f"{float(str(i[31]).replace(',', '.')):.2f}",
                    f"{float(str(i[32]).replace(',', '.')):.2f}",
                ])

        # tvk1022g
        tvk1022g = for_tvkom.tvk1022g

        for i in tvk1022g:
            if people_ls == str(i[1]):
                html_table.append([
                    i[0],
                    f"{float(str(i[21]).replace(',', '.')):.2f}",
                    f"{float(str(i[22]).replace(',', '.')):.2f}",
                    f"{float(str(i[23]).replace(',', '.')):.2f}",
                    f"{float(str(i[24]).replace(',', '.')):.2f}",
                    f"{float(str(i[25]).replace(',', '.')):.2f}",
                    f"{float(str(i[26]).replace(',', '.')):.2f}",
                    f"{float(str(i[27]).replace(',', '.')):.2f}",
                    f"{float(str(i[28]).replace(',', '.')):.2f}",
                    f"{float(str(i[17]).replace(',', '.')):.2f}",
                    f"{float(str(i[18]).replace(',', '.')):.2f}",
                    f"{float(str(i[19]).replace(',', '.')):.2f}",
                    f"{float(str(i[20]).replace(',', '.')):.2f}",
                    f"{float(str(i[29]).replace(',', '.')):.2f}",
                    f"{float(str(i[30]).replace(',', '.')):.2f}",
                    f"{float(str(i[31]).replace(',', '.')):.2f}",
                    f"{float(str(i[32]).replace(',', '.')):.2f}",
                ])

    return render(request, 'tvkom.html', {
        'search_table': search_table,
        'statement_info': statement_info,
        'html_table': html_table,
    })
