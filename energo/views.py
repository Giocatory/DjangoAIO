from datetime import datetime

from django.shortcuts import render
from functools import lru_cache
import for_energo


@lru_cache(maxsize=None)
def energo(request):
    # tables
    html_table = []

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
            result = []
            if str(i[2]).lower().startswith(people_fam.lower()):
                ls = str(i[1])
                if i[11] is not None:
                    temp_str = [i[4], i[5], i[6], i[7], f"{i[8]}{'' if i[9] is None else i[9]}", f"кв {i[11]}"]
                else:
                    temp_str = [i[4], i[5], i[6], i[7], f"{i[8]}{'' if i[9] is None else i[9]}"]

                result = [
                    f"{ls[:-2]}",
                    i[2],
                    "; ".join(temp_str)
                ]
                if result not in html_table:
                    html_table.append(result)

    # Если введена фамилия и имя
    elif people_ls == "" and people_fam != "" and people_imia != "":
        pass

    # Если введен лицевой счет
    elif people_ls != "":
        pass

    return render(request, 'energo.html', {
        'html_table': html_table,
    })
