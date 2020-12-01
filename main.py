""" Головний модуль задачі
- Виводить розрахункову табліцю на екран та в файл
- Виводить первинні данні на екран
"""

import os
from process_data import analysis_means
from data_service import show_dovidniks, show_move_means, get_dovidnik, get_move_mean

MAIN_MENU = \
""" 
~~~~~~~~   ОБРОБКА АНАЛІЗУ РУХУ ОСНОВНИХ ЗАСОБІВ   ~~~~~~~~

1 - Вивід таблиці аналізу засобів на екран
2 - Запис таблиці аналізу засобів в файл
3 - Вивід списка руху основних засобів
4 - Вивід списка довідника основних засобів

0 - Завершення роботи

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""

TITLE = "АНАЛІЗ РУХУ ОСНОВНИХ ЗАСОБІВ"

HEADER = \
"""
============================================================================================================================================
Підприємство  |         Засоби         | Залишок на 01.01.18 | Надійшло у 2018 | Вибуло у 2018 | Залишок на 01.01.19 | Зміни вартості за рік
============================================================================================================================================
"""

FOOTER =  \
'''
============================================================================================================================================

'''

STOP_MESSAGE = '\nДля продовження натисніть <Enter> '

def show_analysis(analysis_list):
    """ Виводить таблицю аналізу основних засобів

    Args:
        analysis_list ([type]): Список засобів
    """
    print(f"\n\n{TITLE:^141}")
    print(HEADER)

    for analysis in analysis_list:
        print(f"{analysis['enterprise_name']:15}",
              f"{analysis['type_of_funs']:23}",
              f"{analysis['remainder_2018']:^21.2f}",
              f"{analysis['received_2018']:^17.2f}",
              f"{analysis['dropped_out_2018']:^15.2f}",
              f"{analysis['remainder_2019']:^21.2f}",
              f"{analysis['cost_changes']:^22.2f}")

    print(FOOTER)

def write_analysis(analysis_list):
    """ Записує список аналізу у текстовий файл

    Args:
        analysis_list ([type]): список аналізу
    """

    with open('./data/analysis.txt', 'w') as analysis_file:
        for analysis in analysis_list:
            line = \
               analysis['enterprise_name'] + ';' +          \
               analysis['type_of_funs'] + ';' +             \
               str(analysis['remainder_2018']) + ';' +      \
               str(analysis['received_2018']) + ';' +       \
               str(analysis['dropped_out_2018']) + ';' +    \
               str(analysis['remainder_2019']) + ';' +      \
               str(analysis['cost_changes'])  + '\n' 
               
            analysis_file.write(line)  
            
    print('\n[INFO]: Файл успішно записано...')     

while True:

    # Виводить головне меню
    os.system('cls')
    print(MAIN_MENU)
    command_number = input("Введіть номер команди: ")

    # Обробка команд користувача
    if command_number == '0':
        print('\n[INFO]: Програма завершила роботу\n')
        exit(0)

    elif command_number == '1':
        analysis_list = analysis_means()
        show_analysis(analysis_list)
        input(STOP_MESSAGE)

    elif command_number == '2':
        analysis_list = analysis_means()
        write_analysis(analysis_list)
        input(STOP_MESSAGE)
        
    elif command_number == '3':
        move_means = get_move_mean()
        show_move_means(move_means)
        input(STOP_MESSAGE)
        
    elif command_number == '4':
        dovidniks = get_dovidnik()
        show_dovidniks(dovidniks)
        input(STOP_MESSAGE)