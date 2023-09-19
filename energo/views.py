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
        html_table = "🐱‍‍🚀"

    # Если введена только фамилия
    elif people_ls == "" and people_fam != "" and people_imia == "":
        pass
    # Если введена фамилия и имя
    elif people_ls == "" and people_fam != "" and people_imia != "":
        pass

    # Если введен лицевой счет
    elif people_ls != "":
        pass

    return render(request, 'energo.html')
