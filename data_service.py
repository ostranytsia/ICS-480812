""" Модуль для отримання даних про рух основних засобів та вивід їх на екран
"""

def get_move_mean():
    """ Повертає вміст файла "move_means.txt" у вигляді списка
    Returns:
        move_mean_list - список рядків файла
    """

    with open('./data/move_means.txt', encoding="utf8") as move_mean_file:
        move_mean_list = move_mean_file.readlines()

    # Накопичувач руху основних засобів
    move_mean_drive = []

    for line in move_mean_list:
        line_list = line.split(';')
        line_list[2] = float(line_list[2])
        line_list[3] = float(line_list[3])
        line_list[4] = float(line_list[4])
        move_mean_drive.append(line_list)


    return move_mean_drive


def show_move_means(move_means):
    """ Виводить список руху основних засобів

    Args:
        move_means (list): список руху основних засобів
    """

    # Задати інтервал виводу
    move_mean_code_from = input("\nЗ якого кода виду засобів виводити? ")
    move_mean_code_to = input("По який код виду засобів виводити? ")

    # Накопичує кількість виведених рядків
    kol_lines = 0

    print()

    for move_mean in move_means:
        if move_mean_code_from <= move_mean[1] <= move_mean_code_to:
            print("Підприємство: {:13} Код: {:2}  Залишок: {:7}  Надійшло: {:7}  Вибуток: {:5}".format(move_mean[0], move_mean[1], move_mean[2], move_mean[3], move_mean[4]))
            kol_lines += 1

    # Перевірити чи був вивід хочаб одного рядка
    if kol_lines == 0:
        print("[ПОМИЛКА]: По Вашому запиту руху засобів нічого не знайдено.")


# move_means = get_move_mean()
# show_move_means(move_means)



def get_dovidnik():
    """ Повертає вміст файла "dovidniks.txt" у вигляді списка

    Returns:
        dovidnik_list - список рядків файла
    """

    with open('./data/dovidniks.txt', encoding="utf8") as dovidnik_file:
        dovidnik_list = dovidnik_file.readlines()

    # Накопичувач довідника основних засобів
    dovidnik_drive = []

    for line in dovidnik_list:
        line_list = line.split(';')
        line_list[1] = line_list[1][:-1]  # Видаляє '\n' в кінці
        dovidnik_drive.append(line_list)


    return dovidnik_drive


def show_dovidniks(dovidniks):
    """ Виводить список довідника

    Args:
        dovidniks (list): список довідника
    """

    # Задати інтервал виводу
    dovidnik_code_from = input("\nЗ якого кода довідника виводити? ")
    dovidnik_code_to = input("По який код довідника виводити? ")

    # Накопичує кількість виведених рядків
    kol_lines = 0

    print()

    for dovidnik in dovidniks:
        if dovidnik_code_from <= dovidnik[0] <= dovidnik_code_to:
            print("Код: {:2} Вид: {:25}".format(dovidnik[0], dovidnik[1]))
            kol_lines += 1

    # Перевірити чи був вивід хочаб одного рядка
    if kol_lines == 0:
        print("[ПОМИЛКА]: По Вашому запиту довідникіка нічого не знайдено.")


# dovidniks = get_dovidnik()
# show_dovidniks(dovidniks)