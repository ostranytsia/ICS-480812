""" Аналіз руху основних засобів
"""

# Підключити функції з модуля 'data_service'
from data_service import get_move_mean, get_dovidnik

# Структура аналізу руху основних засобів вихідних даних
analysis = {
    'enterprise_name'   : '',    # Назва підприємства 
    'type_of_funs'      : '',    # Вид основних засобів
    'remainder_2018'    : 0.0,   # Залишок на 01.01.2018
    'received_2018'     : 0.0,   # Надійшло у 2018
    'dropped_out_2018'  : 0.0,   # Вибуло у 2018
    'remainder_2019'    : 0.0,   # Залишок на 01.01.2019
    'cost_changes'      : 0.0    # Зміни вартості за рік
}


move_means = get_move_mean()
dovidniks = get_dovidnik()

def analysis_means():
    """ Формування аналізу руху основних засобів
    """

    def get_dovidnik_name(dovidnik_code):
        """ Повертає назву засоба по його коду

        Args:
            dovidnik_name ([type]): код засоба

        Returns:
            [type]: назва засобу
        """

        for dovidnik in dovidniks:
            if dovidnik[0] == dovidnik_code:
                return dovidnik[1]

        return "*** Код засобу не знайдений"

    # Накопичувач аналізу руху основних засобів
    analysis_list = []

    for move_mean in move_means:

        # Створити копію шаблона
        analysis_tmp = analysis.copy()

        analysis_tmp['enterprise_name'] = move_mean[0]
        analysis_tmp['remainder_2018'] = move_mean[2]
        analysis_tmp['received_2018'] = move_mean[3]
        analysis_tmp['dropped_out_2018'] = move_mean[4]
        analysis_tmp['remainder_2019'] = analysis_tmp['remainder_2018'] + analysis_tmp['received_2018'] - analysis_tmp['dropped_out_2018']
        analysis_tmp['cost_changes'] = analysis_tmp['remainder_2019'] - analysis_tmp['remainder_2018'] 
        analysis_tmp['type_of_funs'] = get_dovidnik_name(move_mean[1])

        analysis_list.append(analysis_tmp)

    return analysis_list

result = analysis_means()

for r in result:
    print(r)