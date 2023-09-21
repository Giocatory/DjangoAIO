from datetime import datetime

from django.shortcuts import render
from functools import lru_cache
import for_energo


@lru_cache(maxsize=None)
def energo(request):
    # total vars
    searched_ls = ""
    tarif = {
        '202212': 3.464,
        '202301': 3.464,
        '202302': 3.464,
        '202303': 3.464,
        '202304': 3.464,
        '202305': 3.464,
        '202306': 3.464,
        '202307': 3.464,
        '202308': 3.464,
    }
    last_saldo = ["", ""]
    total_sumo = 0
    total_middle_klv = 0
    total_sum_klv = 0

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
        sprrab202308_tuples = for_energo.sprrab202308_tuples
        for i in sprrab202308_tuples:
            if str(i[1]).lower().startswith(people_fam.lower()):
                ls = str(i[0])
                if i[9] is not None:
                    temp_str = [
                        f"{'' if i[2] is None else i[2]}", f"{'' if i[3] is None else i[3]}",
                        f"{'' if i[4] is None else i[4]}", f"{'' if i[5] is None else i[5]}",
                        f"д. {'' if i[6] is None else i[6]}{'' if i[7] is None else i[7]}", f"кв {i[9]}"]
                else:
                    temp_str = [
                        f"{'' if i[2] is None else i[2]}", f"{'' if i[3] is None else i[3]}",
                        f"{'' if i[4] is None else i[4]}", f"{'' if i[5] is None else i[5]}",
                        f"д. {'' if i[6] is None else i[6]}{'' if i[7] is None else i[7]}"
                    ]

                result = [
                    f"{ls}",
                    f"{i[1]}",
                    "; ".join(temp_str).replace(" ;", "").lstrip('; ')
                ]
                if result not in html_table:
                    html_table.append(result)

    # Если введена фамилия и имя
    elif people_ls == "" and people_fam != "" and people_imia != "":
        html_table.clear()

        html_table.append(['Л/счет', 'Фамилия Имя Отчество', 'Адрес'])
        sprrab202308_tuples = for_energo.sprrab202308_tuples

        for i in sprrab202308_tuples:
            fam_imia = str(i[1]).lower().split(' ')

            if fam_imia[0].startswith(people_fam.lower()) and fam_imia[1].startswith(people_imia.lower()):
                ls = str(i[0])
                if i[9] is not None:
                    temp_str = [
                        f"{'' if i[2] is None else i[2]}", f"{'' if i[3] is None else i[3]}",
                        f"{'' if i[4] is None else i[4]}", f"{'' if i[5] is None else i[5]}",
                        f"д. {'' if i[6] is None else i[6]}{'' if i[7] is None else i[7]}", f"кв {i[9]}"
                    ]
                else:
                    temp_str = [
                        f"{'' if i[2] is None else i[2]}", f"{'' if i[3] is None else i[3]}",
                        f"{'' if i[4] is None else i[4]}", f"{'' if i[5] is None else i[5]}",
                        f"д. {'' if i[6] is None else i[6]}{'' if i[7] is None else i[7]}"
                    ]

                result = [
                    f"{ls}",
                    i[1],
                    "; ".join(temp_str).replace(" ;", "").lstrip('; ')
                ]
                if result not in html_table:
                    html_table.append(result)

    # Если введен лицевой счет
    elif people_ls != "":
        common_table.clear()
        pay_table.clear()
        result_table.clear()
        sprrab202212_tuples = for_energo.sprrab202212_tuples
        sprrab202301_tuples = for_energo.sprrab202301_tuples
        sprrab202302_tuples = for_energo.sprrab202302_tuples
        sprrab202303_tuples = for_energo.sprrab202303_tuples
        sprrab202304_tuples = for_energo.sprrab202304_tuples
        sprrab202305_tuples = for_energo.sprrab202305_tuples
        sprrab202306_tuples = for_energo.sprrab202306_tuples
        sprrab202307_tuples = for_energo.sprrab202307_tuples
        sprrab202308_tuples = for_energo.sprrab202308_tuples
        pays_tuples = for_energo.pays_tuples

        # common_table
        for i in sprrab202308_tuples:
            temp_str = []
            if str(i[0]) == people_ls:
                if i[9] is not None:
                    temp_str = [
                        f"{'' if i[2] is None else i[2]}", f"{'' if i[3] is None else i[3]}",
                        f"{'' if i[4] is None else i[4]}", f"{'' if i[5] is None else i[5]}",
                        f"д. {'' if i[6] is None else i[6]}{'' if i[7] is None else i[7]}", f"кв {i[9]}"
                    ]
                else:
                    temp_str = [
                        f"{'' if i[2] is None else i[2]}", f"{'' if i[3] is None else i[3]}",
                        f"{'' if i[4] is None else i[4]}", f"{'' if i[5] is None else i[5]}",
                        f"д. {'' if i[6] is None else i[6]}{'' if i[7] is None else i[7]}"
                    ]
                common_table.append(f"ФИО: {i[1]}")
                common_table.append(f"Л/счет: {i[0]}")
                common_table.append(f"Адрес: {'; '.join(temp_str).replace(' ;', '').lstrip('; ')}")
                searched_ls = str(i[0])
                break

        # pay_table
        pay_table.append(["Дата", "Киловатты", "Тариф", "Сальдо", "Оплата"])
        for i in pays_tuples:
            ls = str(i[0])
            if people_ls == ls[:-2]:
                if str(i[2]) == "202211":
                    break

                # sprrab202308_tuples
                for spr in sprrab202308_tuples:
                    if str(i[2]) == str(spr[14]):
                        ls = str(spr[0])
                        if ls == people_ls:
                            pay_table.append([
                                f"{i[2]}",
                                f"{spr[10]}",
                                tarif[f"{i[2]}"],
                                f"{i[1]}",
                                f"{i[4]}",
                            ])
                            total_sumo += float(str(i[4]).replace(",", "."))
                            last_saldo = [f"{i[2]}", f"{i[1]}"]
                            total_middle_klv += int(spr[10])
                            total_sum_klv += float(str(spr[10])) * tarif[f"{i[2]}"]
                            break
                    else:
                        break

                # sprrab202307_tuples
                for spr in sprrab202307_tuples:
                    if str(i[2]) == str(spr[14]):
                        ls = str(spr[0])
                        if ls == people_ls:
                            pay_table.append([
                                f"{i[2]}",
                                f"{spr[10]}",
                                tarif[f"{i[2]}"],
                                f"{i[1]}",
                                f"{i[4]}",
                            ])
                            total_sumo += float(str(i[4]).replace(",", "."))
                            total_middle_klv += int(spr[10])
                            total_sum_klv += float(str(spr[10])) * tarif[f"{i[2]}"]
                            break
                    else:
                        break

                # sprrab202306_tuples
                for spr in sprrab202306_tuples:
                    if str(i[2]) == str(spr[14]):
                        ls = str(spr[0])
                        if ls == people_ls:
                            pay_table.append([
                                f"{i[2]}",
                                f"{spr[10]}",
                                tarif[f"{i[2]}"],
                                f"{i[1]}",
                                f"{i[4]}",
                            ])
                            total_sumo += float(str(i[4]).replace(",", "."))
                            total_middle_klv += int(spr[10])
                            total_sum_klv += float(str(spr[10])) * tarif[f"{i[2]}"]
                            break
                    else:
                        break

                # sprrab202305_tuples
                for spr in sprrab202305_tuples:
                    if str(i[2]) == str(spr[14]):
                        ls = str(spr[0])
                        if ls == people_ls:
                            pay_table.append([
                                f"{i[2]}",
                                f"{spr[10]}",
                                tarif[f"{i[2]}"],
                                f"{i[1]}",
                                f"{i[4]}",
                            ])
                            total_sumo += float(str(i[4]).replace(",", "."))
                            total_middle_klv += int(spr[10])
                            total_sum_klv += float(str(spr[10])) * tarif[f"{i[2]}"]
                            break
                    else:
                        break

                # sprrab202304_tuples
                for spr in sprrab202304_tuples:
                    if str(i[2]) == str(spr[14]):
                        ls = str(spr[0])
                        if ls == people_ls:
                            pay_table.append([
                                f"{i[2]}",
                                f"{spr[10]}",
                                tarif[f"{i[2]}"],
                                f"{i[1]}",
                                f"{i[4]}",
                            ])
                            total_sumo += float(str(i[4]).replace(",", "."))
                            total_middle_klv += int(spr[10])
                            total_sum_klv += float(str(spr[10])) * tarif[f"{i[2]}"]
                            break
                    else:
                        break

                # sprrab202303_tuples
                for spr in sprrab202303_tuples:
                    if str(i[2]) == str(spr[14]):
                        ls = str(spr[0])
                        if ls[:-2] == people_ls:
                            pay_table.append([
                                f"{i[2]}",
                                f"{spr[10]}",
                                tarif[f"{i[2]}"],
                                f"{i[1]}",
                                f"{i[4]}",
                            ])
                            total_sumo += float(str(i[4]).replace(",", "."))
                            total_middle_klv += int(spr[10])
                            total_sum_klv += float(str(spr[10])) * tarif[f"{i[2]}"]
                            break
                    else:
                        break

                # sprrab202302_tuples
                for spr in sprrab202302_tuples:
                    if str(i[2]) == str(spr[14]):
                        ls = str(spr[0])
                        if ls[:-2] == people_ls:
                            pay_table.append([
                                f"{i[2]}",
                                f"{spr[10]}",
                                tarif[f"{i[2]}"],
                                f"{i[1]}",
                                f"{i[4]}",
                            ])
                            total_sumo += float(str(i[4]).replace(",", "."))
                            total_middle_klv += int(spr[10])
                            total_sum_klv += float(str(spr[10])) * tarif[f"{i[2]}"]
                            break
                    else:
                        break

                # sprrab202301_tuples
                for spr in sprrab202301_tuples:
                    if str(i[2]) == str(spr[14]):
                        ls = str(spr[0])
                        if ls[:-2] == people_ls:
                            pay_table.append([
                                f"{i[2]}",
                                f"{spr[10]}",
                                tarif[f"{i[2]}"],
                                f"{i[1]}",
                                f"{i[4]}",
                            ])
                            total_sumo += float(str(i[4]).replace(",", "."))
                            total_middle_klv += int(spr[10])
                            total_sum_klv += float(str(spr[10])) * tarif[f"{i[2]}"]
                            break
                    else:
                        break

                # sprrab202212_tuples
                for spr in sprrab202212_tuples:
                    if str(i[2]) == str(spr[14]):
                        ls = str(spr[0])
                        if ls == people_ls:
                            pay_table.append([
                                f"{i[2]}",
                                f"{spr[10]}",
                                tarif[f"{i[2]}"],
                                f"{i[1]}",
                                f"{i[4]}",
                            ])
                            total_sumo += float(str(i[4]).replace(",", "."))
                            total_middle_klv += int(spr[10])
                            total_sum_klv += float(str(spr[10])) * tarif[f"{i[2]}"]
                            break
                    else:
                        break

        # result_table
        result_table.append(f"SALDO составляет на {last_saldo[0]} в размере {last_saldo[1]} рублей")
        result_table.append(f"Оплата составила: {total_sumo:.2f} рублей")
        result_table.append(
            f"Среднее потребление составило: {total_middle_klv}кВт.ч. на сумму {total_sum_klv:.2f} рублей")

    return render(request, 'energo.html', {
        'html_table': html_table,
        'common_table': common_table,
        'pay_table': pay_table,
        'result_table': result_table,
        'searched_ls': searched_ls,
    })
