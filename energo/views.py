from datetime import datetime

from django.shortcuts import render
from functools import lru_cache
import for_energo


@lru_cache(maxsize=None)
def energo(request):
    # tables
    html_table = []
    common_table = []
    pay_table = []
    result_table = []

    # request from form
    people_ls = request.POST.get("supplier-ls")
    people_fam = request.POST.get("supplier-fam")
    people_imia = request.POST.get("supplier-imia")

    if people_ls == "" and people_fam == "" and people_imia == "":
        html_table = "----"

    # Если введена только фамилия
    elif people_ls == "" and people_fam != "" and people_imia == "":
        html_table.append(['Л/счет', 'Фамилия Имя Отчество', 'Адрес'])
        sprrab_tuples = for_energo.sprrab_tuples
        for i in sprrab_tuples:
            if str(i[2]).lower().startswith(people_fam.lower()):
                ls = str(i[1])
                if i[11] is not None:
                    temp_str = [
                        f"{'' if i[4] is None else i[4]}", f"{'' if i[5] is None else i[5]}",
                        f"{'' if i[6] is None else i[6]}", f"{'' if i[7] is None else i[7]}",
                        f"д. {'' if i[8] is None else i[8]}{'' if i[9] is None else i[9]}", f"кв {i[11]}"]
                else:
                    temp_str = [
                        f"{'' if i[4] is None else i[4]}", f"{'' if i[5] is None else i[5]}",
                        f"{'' if i[6] is None else i[6]}", f"{'' if i[7] is None else i[7]}",
                        f"д. {'' if i[8] is None else i[8]}{'' if i[9] is None else i[9]}"
                    ]

                result = [
                    f"{ls[:-2]}",
                    f"{i[2]}",
                    "; ".join(temp_str).replace(" ;", "").lstrip('; ')
                ]
                if result not in html_table:
                    html_table.append(result)

    # Если введена фамилия и имя
    elif people_ls == "" and people_fam != "" and people_imia != "":
        html_table.clear()

        html_table.append(['Л/счет', 'Фамилия Имя Отчество', 'Адрес'])
        sprrab_tuples = for_energo.sprrab_tuples

        for i in sprrab_tuples:
            fam_imia = str(i[2]).lower().split(' ')

            if fam_imia[0].startswith(people_fam.lower()) and fam_imia[1].startswith(people_imia.lower()):
                ls = str(i[1])
                if i[11] is not None:
                    temp_str = [
                        f"{'' if i[4] is None else i[4]}", f"{'' if i[5] is None else i[5]}",
                        f"{'' if i[6] is None else i[6]}", f"{'' if i[7] is None else i[7]}",
                        f"д. {'' if i[8] is None else i[8]}{'' if i[9] is None else i[9]}", f"кв {i[11]}"]
                else:
                    temp_str = [
                        f"{'' if i[4] is None else i[4]}", f"{'' if i[5] is None else i[5]}",
                        f"{'' if i[6] is None else i[6]}", f"{'' if i[7] is None else i[7]}",
                        f"д. {'' if i[8] is None else i[8]}{'' if i[9] is None else i[9]}"
                    ]

                result = [
                    f"{ls[:-2]}",
                    i[2],
                    "; ".join(temp_str).replace(" ;", "").lstrip('; ')
                ]
                if result not in html_table:
                    html_table.append(result)

    # Если введен лицевой счет
    elif people_ls != "":
        sprrab_tuples = for_energo.sprrab_tuples
        pay_tuples = for_energo.sprrab_tuples
        tarif_tuples = for_energo.energ_tarif_tuples

    return render(request, 'energo.html', {
        'html_table': html_table,
        'common_table': common_table,
        'pay_table': pay_table,
        'result_table': result_table,
    })
