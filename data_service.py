""" Модуль для отримання даних про рух основних засобів та вивід їх на екран
"""

def get_move_mean():
    """ Повертає вміст файла "move_means.txt" у вигляді списка
    Returns:
        move_mean_list - список рядків файла
    """

    move_mean_list = [
        "Універсам 22;1;44 048,00;500,00;200,00",
        "Дніпрянка;1;22 456,00;365,00;123,00",
        "Універсам 22;2;5 564,00;2 571,00;135,00",
        "Дніпрянка;2;10 087,00;15 972,00;58,00",
        "Універсам 22;3;0,00;0,00;0,00",
        "Дніпрянка;3;206,00;34,00;50,00",
        "Універсам 22;4;116,00;64,00;23,00",
        "Дніпрянка;4;34,00;23,00;25,00"
    ]

    # Накопичувач руху основних засобів
    move_mean_drive = []

    for line in move_mean_list:
        line_list = line.split(';')
        move_mean_drive.append((line_list))


    return move_mean_drive


def show_move_means(move_means):
    """ Виводить список руху основних засобів

    Args:
        move_means (list): список руху основних засобів
    """

    # Задати інтервал виводу
    move_mean_code_from = input("З якого кода виду засобів виводити?")
    move_mean_code_to = input("По який код виду засобів виводити?")

    # Накопичує кількість виведених рядків
    kol_lines = 0

    for move_mean in move_means:
        if move_mean_code_from <= move_mean[1] <= move_mean_code_to:
            print("Підприємство: {:13} Код: {:2} Залишок: {:10} Надійшло: {:10} Вибуток: {:7}".format(move_mean[0], move_mean[1], move_mean[2], move_mean[3], move_mean[4]))
            kol_lines += 1

    # Перевірити чи був вивід хочаб одного рядка
    if kol_lines == 0:
        print("По Вашому запиту руху засобів нічого не знайдено.")


move_means = get_move_mean()
show_move_means(move_means)



def get_dovidnik():
    """ Повертає вміст файла "dovidniks.txt" у вигляді списка

    Returns:
        dovidnik_list - список рядків файла
    """

    dovidnik_list = [
        "1;Будівлі",
        "2;Машини та обладнання",
        "3;Транспортні засоби",
        "4;Інструмент та інвентар"
    ]

    # Накопичувач довідника основних засобів
    dovidnik_drive = []

    for line in dovidnik_list:
        line_list = line.split(';')
        dovidnik_drive.append((line_list))


    return dovidnik_drive


def show_dovidniks(dovidniks):
    """ Виводить список довідника

    Args:
        dovidniks (list): список довідника
    """

    # Задати інтервал виводу
    dovidnik_code_from = input("З якого кода довідника виводити?")
    dovidnik_code_to = input("По який код довідника виводити?")

    # Накопичує кількість виведених рядків
    kol_lines = 0

    for dovidnik in dovidniks:
        if dovidnik_code_from <= dovidnik[0] <= dovidnik_code_to:
            print("Код: {:2} Вид: {:25}".format(dovidnik[0], dovidnik[1]))
            kol_lines += 1

    # Перевірити чи був вивід хочаб одного рядка
    if kol_lines == 0:
        print("По Вашому запиту довідникіка нічого не знайдено.")


dovidniks = get_dovidnik()
show_dovidniks(dovidniks)