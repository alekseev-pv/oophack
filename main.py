import colorama
from battle import fight_with_map, start_fight
from other_utils import create_percs, create_stuff, equip_percs

if __name__ == "__main__":
    colorama.init()
    items = create_stuff()
    percs = create_percs(count=10)
    equip_percs(percs, items)
    visual_format = input('Формат игры:\n'
                          '1 - текстовый\n'
                          '2 - миникарта.\n'
                          'Введите цифру: ')
    while visual_format not in ('1', '2'):
        print('Некорректный ввод \n')
        visual_format = input('Формат игры:\n'
                              '1 - текстовый\n'
                              '2 - миникарта.\n'
                              'Введите цифру: ')
    if int(visual_format) == 1:
        start_fight(percs)
    elif int(visual_format) == 2:
        fight_with_map(percs, 0.3)
    else:
        print('Что-то пошло не так \n')
    print(20 * '- ')
    print(percs[0])
