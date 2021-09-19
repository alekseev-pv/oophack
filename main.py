from pprint import pprint

import fight.cli as cli
import fight.logic as logic


def main():
    count_heroes = cli.get_count_heroes()
    all_heroes = logic.dress_persons(
        logic.make_persons(count_heroes),
        logic.make_things(),
    )
    pprint(all_heroes)
    user_hero_id = cli.get_hero_id(count_heroes)
    user_hero_obj = list(filter(lambda x: x.id == user_hero_id, all_heroes))[0]
    odds = count_heroes - 1
    user_bet = cli.get_bet(odds)

    if user_bet:
        print(f'\nВаша ставка {user_bet} на {user_hero_obj}\n')

    while len(all_heroes) > 1:
        logic.make_arena(all_heroes)
    winner = all_heroes[0]
    print(f'Победитель: {winner}')

    if winner is user_hero_obj:
        print('Вы угадали!')
        logic.GLOBAL_USER_BALANCE = \
            logic.GLOBAL_USER_BALANCE + (user_bet * odds)
    else:
        print('В другой раз точно повезет!')
        logic.GLOBAL_USER_BALANCE = logic.GLOBAL_USER_BALANCE - user_bet

    user_balance = logic.get_user_balance()
    if user_balance > 0:
        more = cli.get_more()
        if more is True:
            main()
        else:
            print('До скорого!')
    else:
        print('Будут деньги — приходите ;-) ')


if __name__ == "__main__":
    main()
