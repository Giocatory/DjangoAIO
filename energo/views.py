from datetime import datetime

from django.shortcuts import render
from functools import lru_cache
import for_energo


@lru_cache(maxsize=None)
def energo(request):
    # total vars
    six_month_inf = []
    six_month_values = [0, 0, 0, 0, 0]
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
        '202309': 3.464,
        '202310': 3.464,
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
        sprrab202309_tuples = for_energo.sprrab202309_tuples
        sprrab202310_tuples = for_energo.sprrab202310_tuples
        pays_tuples = for_energo.pays_tuples

        six_month_inf.append(["Киловатты", "Тариф", "Сальдо", "Оплата", "Субсидия"])

        # common_table
        for i in sprrab202310_tuples:
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
        pay_table.append(["Дата", "Киловатты", "Тариф", "Сальдо", "Оплата", "Субсидия"])
        for i in pays_tuples:
            ls = str(i[0])
            if people_ls == ls[:-2]:
                if str(i[2]) == "202211":
                    break

                # sprrab202310_tuples
                subsid1023 = for_energo.subsid1023
                subsid_total = 0
                for s in subsid1023:
                    if str(people_ls) == str(s[0]):
                        subsid_total = s[2]

                for spr in sprrab202310_tuples:
                    if str(i[2]) == str(spr[14]):
                        ls = str(spr[0])
                        if ls == people_ls:
                            pay_table.append([
                                f"{i[2]}",
                                f"{spr[10]}",
                                tarif[f"{i[2]}"],
                                f"{i[1]}",
                                f"{i[4]}",
                                subsid_total
                            ])
                            total_sumo += float(str(i[4]).replace(",", "."))
                            last_saldo = [f"{i[2]}", f"{i[1]}"]
                            total_middle_klv += int(spr[10])
                            total_sum_klv += float(str(spr[10])) * tarif[f"{i[2]}"]

                            six_month_values[0] += int(spr[10])
                            six_month_values[1] = tarif[f"{i[2]}"]
                            six_month_values[2] += float(str(i[1]).replace(",", '.'))
                            six_month_values[3] += float(str(i[4]).replace(",", "."))
                            six_month_values[4] += subsid_total
                            break
                    else:
                        break

                # sprrab202309_tuples
                subsid0923 = for_energo.subsid0923
                subsid_total = 0
                for s in subsid0923:
                    if str(people_ls) == str(s[0]):
                        subsid_total = s[2]

                for spr in sprrab202309_tuples:
                    if str(i[2]) == str(spr[14]):
                        ls = str(spr[0])
                        if ls == people_ls:
                            pay_table.append([
                                f"{i[2]}",
                                f"{spr[10]}",
                                tarif[f"{i[2]}"],
                                f"{i[1]}",
                                f"{i[4]}",
                                subsid_total
                            ])
                            total_sumo += float(str(i[4]).replace(",", "."))
                            total_middle_klv += int(spr[10])
                            total_sum_klv += float(str(spr[10])) * tarif[f"{i[2]}"]

                            six_month_values[0] += int(spr[10])
                            six_month_values[1] = tarif[f"{i[2]}"]
                            six_month_values[2] += float(str(i[1]).replace(",", '.'))
                            six_month_values[3] += float(str(i[4]).replace(",", "."))
                            six_month_values[4] += subsid_total
                            break
                    else:
                        break

                # sprrab202308_tuples
                subsid0823 = for_energo.subsid0823
                subsid_total = 0
                for s in subsid0823:
                    if str(people_ls) == str(s[0]):
                        subsid_total = s[2]

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
                                subsid_total
                            ])
                            total_sumo += float(str(i[4]).replace(",", "."))
                            total_middle_klv += int(spr[10])
                            total_sum_klv += float(str(spr[10])) * tarif[f"{i[2]}"]

                            six_month_values[0] += int(spr[10])
                            six_month_values[1] = tarif[f"{i[2]}"]
                            six_month_values[2] += float(str(i[1]).replace(",", '.'))
                            six_month_values[3] += float(str(i[4]).replace(",", "."))
                            six_month_values[4] += subsid_total
                            break
                    else:
                        break

                # sprrab202307_tuples
                subsid0723 = for_energo.subsid0723
                subsid_total = 0
                for s in subsid0723:
                    if str(people_ls) == str(s[0]):
                        subsid_total = s[2]

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
                                subsid_total
                            ])
                            total_sumo += float(str(i[4]).replace(",", "."))
                            total_middle_klv += int(spr[10])
                            total_sum_klv += float(str(spr[10])) * tarif[f"{i[2]}"]

                            six_month_values[0] += int(spr[10])
                            six_month_values[1] = tarif[f"{i[2]}"]
                            six_month_values[2] += float(str(i[1]).replace(",", '.'))
                            six_month_values[3] += float(str(i[4]).replace(",", "."))
                            six_month_values[4] += subsid_total
                            break
                    else:
                        break

                # sprrab202306_tuples
                subsid0623 = for_energo.subsid0623
                subsid_total = 0
                for s in subsid0623:
                    if str(people_ls) == str(s[0]):
                        subsid_total = s[2]

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
                                subsid_total
                            ])
                            total_sumo += float(str(i[4]).replace(",", "."))
                            total_middle_klv += int(spr[10])
                            total_sum_klv += float(str(spr[10])) * tarif[f"{i[2]}"]

                            six_month_values[0] += int(spr[10])
                            six_month_values[1] = tarif[f"{i[2]}"]
                            six_month_values[2] += float(str(i[1]).replace(",", '.'))
                            six_month_values[3] += float(str(i[4]).replace(",", "."))
                            six_month_values[4] += subsid_total
                            break
                    else:
                        break

                # sprrab202305_tuples
                subsid0523 = for_energo.subsid0523
                subsid_total = 0
                for s in subsid0523:
                    if str(people_ls) == str(s[0]):
                        subsid_total = s[2]

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
                                subsid_total
                            ])
                            total_sumo += float(str(i[4]).replace(",", "."))
                            total_middle_klv += int(spr[10])
                            total_sum_klv += float(str(spr[10])) * tarif[f"{i[2]}"]

                            six_month_values[0] += int(spr[10])
                            six_month_values[1] = tarif[f"{i[2]}"]
                            six_month_values[2] += float(str(i[1]).replace(",", '.'))
                            six_month_values[3] += float(str(i[4]).replace(",", "."))
                            six_month_values[4] += subsid_total
                            break
                    else:
                        break

                # sprrab202304_tuples
                subsid0423 = for_energo.subsid0423
                subsid_total = 0
                for s in subsid0423:
                    if str(people_ls) == str(s[0]):
                        subsid_total = s[2]

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
                                subsid_total
                            ])
                            total_sumo += float(str(i[4]).replace(",", "."))
                            total_middle_klv += int(spr[10])
                            total_sum_klv += float(str(spr[10])) * tarif[f"{i[2]}"]
                            break
                    else:
                        break

                # sprrab202303_tuples
                subsid0323 = for_energo.subsid0323
                subsid_total = 0
                for s in subsid0323:
                    if str(people_ls) == str(s[0]):
                        subsid_total = s[2]

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
                                subsid_total
                            ])
                            total_sumo += float(str(i[4]).replace(",", "."))
                            total_middle_klv += int(spr[10])
                            total_sum_klv += float(str(spr[10])) * tarif[f"{i[2]}"]
                            break
                    else:
                        break

                # sprrab202302_tuples
                subsid0223 = for_energo.subsid0223
                subsid_total = 0
                for s in subsid0223:
                    if str(people_ls) == str(s[0]):
                        subsid_total = s[2]

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
                                subsid_total
                            ])
                            total_sumo += float(str(i[4]).replace(",", "."))
                            total_middle_klv += int(spr[10])
                            total_sum_klv += float(str(spr[10])) * tarif[f"{i[2]}"]
                            break
                    else:
                        break

                # sprrab202301_tuples
                subsid0123 = for_energo.subsid0123
                subsid_total = 0
                for s in subsid0123:
                    if str(people_ls) == str(s[0]):
                        subsid_total = s[2]

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
                                subsid_total
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
                                0
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

    six_month_values[0] = f"{six_month_values[0]:.2f}"
    six_month_values[1] = f"{six_month_values[1]:.2f}"
    six_month_values[2] = f"{six_month_values[2]:.2f}"
    six_month_values[3] = f"{six_month_values[3]:.2f}"
    six_month_values[4] = f"{six_month_values[4]:.2f}"
    six_month_inf.append(six_month_values)

    return render(request, 'energo.html', {
        'html_table': html_table,
        'common_table': common_table,
        'pay_table': pay_table,
        'result_table': result_table,
        'searched_ls': searched_ls,
        'six_month_inf': six_month_inf,
    })


@lru_cache(maxsize=None)
def energo_spravka(request):
    # total vars
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
        '202309': 3.464,
        '202310': 3.464,
    }
    spravka_arr = []
    specialist = ["Специалист", "Северного ОСЗН"]

    # request from form
    people_ls = request.POST.get("supplier-ls")

    # connect
    sprrab202310_tuples = for_energo.sprrab202310_tuples
    pays_tuples = for_energo.pays_tuples

    # date
    if datetime.now().month < 10:
        current_date = f"Дата выдачи: {datetime.now().day}.0{datetime.now().month}.{datetime.now().year}"
    else:
        current_date = f"Дата выдачи: {datetime.now().day}.{datetime.now().month}.{datetime.now().year}"

    # spravka_arr
    for spr in sprrab202310_tuples:
        temp_str = []
        if str(spr[0]) == people_ls:
            if spr[9] is not None:
                temp_str = [
                    f"{'' if spr[2] is None else spr[2]}", f"{'' if spr[3] is None else spr[3]}",
                    f"{'' if spr[4] is None else spr[4]}", f"{'' if spr[5] is None else spr[5]}",
                    f"д. {'' if spr[6] is None else spr[6]}{'' if spr[7] is None else spr[7]}", f"кв {spr[9]}"
                ]
            else:
                temp_str = [
                    f"{'' if spr[2] is None else spr[2]}", f"{'' if spr[3] is None else spr[3]}",
                    f"{'' if spr[4] is None else spr[4]}", f"{'' if spr[5] is None else spr[5]}",
                    f"д. {'' if spr[6] is None else spr[6]}{'' if spr[7] is None else spr[7]}"
                ]
            spravka_arr.append(f"ФИО: {spr[1]}")
            spravka_arr.append(f"Лицевой счет №{spr[0]}")
            spravka_arr.append(f"Проживающий по адресу: {'; '.join(temp_str).replace(' ;', '').lstrip('; ')}")
            temp_eval = float(str(spr[10])) * tarif[f'{spr[14]}']
            spravka_arr.append(f"Месячное потребление: {spr[10]}кВт.ч. на сумму "
                               f"{temp_eval:.2f}")
            break

    # pay_table
    for pay in pays_tuples:
        ls = str(pay[0])
        if people_ls == ls[:-2]:
            if str(pay[2]) == "202211":
                break
            spravka_arr.append(f"Оплата составила: {pay[4]}")
            spravka_arr.append(f"Задолженность или переплата по электроэнергии составляет на {pay[2]}"
                               f" в размере {pay[1]}")
            break

    spravka_arr.append(f"Справка дана по месту требования")

    return render(request, 'energo_spravka.html', {
        'current_date': current_date,
        'spravka_arr': spravka_arr,
        'specialist': specialist,
    })
