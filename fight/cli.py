import fight.logic as logic
import fight.settings as sett


def get_count_heroes(err_num=None):
    if err_num:
        print(f'{err_num} не получится!')
    else:
        print('Сколько героев будут биться на арене?')
    print(f'от 3 до {len(sett.NAMES_HEROES)}')
    int_input = int(input())
    if int_input > 32 or int_input < 3:
        return get_count_heroes(int_input)
    return int_input


def get_bet(odds, err_num=None):
    if err_num:
        print(f'{err_num} не получится!')
    else:
        print('\nРазмер ставки в ФайтКоинах:')
    user_balance = logic.get_user_balance()
    print(f'коэффициент боя 1 к {odds}')
    print(f'ваш баланс {user_balance}')
    float_input = float(input())
    if float_input > user_balance or float_input < 0:
        return get_bet(float_input)
    return float_input


def get_hero_id(count_heroes, err_num=None):
    if not err_num:
        print('\nНа кого будете ставить?:')
    print(f'укажите номер героя от 1 до {count_heroes}')
    int_input = int(input())
    if int_input < 1 or int_input > count_heroes:
        return get_hero_id(count_heroes, int_input)
    return int_input


def get_more():
    print('еще раз? Y/n')
    if str(input()) == 'n':
        return False
    return True
