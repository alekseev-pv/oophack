from colorama import Fore, init

import inputs
import solo_adventure
from arena_battle import Arena
from classes import Person

init(autoreset=True)


def border():
    print(Fore.LIGHTGREEN_EX + '--------------------------')


def main_menu():
    border()
    print(
        'Добро пожаловать в игру "Арена", созданную в рамках'
        ' хакатона в Яндекс.Практикуме 18.09.21'
        )
    print('Автор Erduyta')
    print('Команды:')
    print(Fore.YELLOW + 'help' + Fore.RESET + ' - вы здесь в первые')
    print(Fore.YELLOW + 'solo' + Fore.RESET + ' - начать компанию')
    print(
        Fore.YELLOW + 'arena' + Fore.RESET + ' - начать случайную '
        'битву на арене'
        )
    print(
        Fore.YELLOW + 'quit' + Fore.RESET + ' or ' + Fore.YELLOW +
        'q' + Fore.RESET + ' - выход'
        )
    inputs.main_menu()


def help():
    border()
    print(
        'Компания - это не большое текстовое приключение с продвинутыми '
        'механиками, которое я сделал, где вы создаете героя и '
        'помогате жителям деревни'
        )
    print(
        'Случайная битва на арене - это игра, которую необходимо было '
        'подготовить в рамках хакатона'
        )
    main_menu()


def arena():
    border()
    print('Бой на арене:')
    arena = Arena()
    victorius = arena.participants[0]
    print(f'Побеждает {victorius.name}' + Fore.RESET + '!!')
    main_menu()


def defend_action_arena(attacker, defender, damage):
    print(
        f'{attacker.name}' + Fore.RESET + f' наносит удар по {defender.name} '
        + Fore.RESET + 'на ' + Fore.RED + f'{damage} урона!'
        )


def solo_menu():
    border()
    print('Выберите класс:')
    print(
        Fore.YELLOW + 'paladin' + Fore.RESET + ' - Воин с большим количеством '
        'здоровья и защиты'
        )
    print(
        Fore.YELLOW + 'warrior' + Fore.RESET + ' - Воин с большим '
        'количеством урона'
        )
    inputs.solo_menu()


def solo_name():
    border()
    print('Введите имя:')
    x = input()
    return Fore.BLUE + x


def solo_ui(hero):
    border()
    print(Fore.LIGHTRED_EX + f'Здровье {round(hero.hp, 1)}/{hero.max_hp}')
    # print('inventory - открыть снаряжение')
    print(Fore.YELLOW + 'quit' + Fore.RESET + ' - выйти')


def solo_start(adventure):
    solo_ui(adventure.hero)
    print(
        'Вы прибыли в деревню Окорочка по личному приказу короля. О '
        'деревни ходят неприятные слухи. Говорят, что на протяжении '
        'последнего месяца всем жителям снится один и тот же кошмар. '
        )
    print('')
    print(
        'Вы стоите на центральной площади деревни, на вас глазеют '
        'какие-то мальчишки. Впереди веднеется вывеска трактира.'
        )
    print(Fore.YELLOW + 'tavern' + Fore.RESET + ' - зайти в трактир')
    print(Fore.YELLOW + 'children' + Fore.RESET + ' - поговорить с детьми')
    inputs.solo_start(adventure)


def children_1(adventure):
    solo_ui(adventure.hero)
    print(
        'Детей трое: два мальчика и девочка. Когда вы приблизились, '
        'девочка спряталась за спины мальчикам и робко выглядывала '
        'оттуда. Мальчики были явно смущены и немного испуганы, но '
        'пытались этого не показывать.'
        )
    print('')
    print('Что вы хотите узнать у детей?')
    print(Fore.YELLOW + 'elder' + Fore.RESET + ' - про старейшину')
    print(Fore.YELLOW + 'dream' + Fore.RESET + ' - про сны')
    print(Fore.YELLOW + 'pub' + Fore.RESET + ' - где трактир')
    print(Fore.YELLOW + 'leave' + Fore.RESET + ' - закончить разговор')
    inputs.children_talk(adventure)


def children_talk_pub(adventure):
    # solo_ui(adventure.hero)
    border()
    print(
        'Один из мальчиков встрепенулся, указал вам за спину и '
        'сказал: "Так вон же вывеска"'
        )
    children_1(adventure)


def children_talk_elder(adventure):
    # solo_ui(adventure.hero)
    border()
    print(
        'Мальчики переглянулись, потом один из них спросил: "Что '
        'такое старейшина?"'
    )
    print('Вы попытались объяснить, но они явно не понимали.')
    print(
        'Наконец, девочка сзади сказала: "Вас, наверно, '
        'интересует дядя Майк. Он живёт за пабом, совсем рядом, '
        'правда, он сейчас приболел.'
        )
    adventure.elder = True
    children_1(adventure)


def children_talk_dream(adventure):
    # solo_ui(adventure.hero)
    border()
    print(
        'До одного из мальчиков наконец-то дошло, его глаза '
        'загорелись, на лице отобразилось просветление: "Вас '
        'наверно прислали разобраться с этим?"'
        )
    print('')
    print(
        'Второй мальчик подал голос: "Мне снится, что я играю '
        'в деревни, а начинаю чувствовать, как будто за мной '
        'наблюдают. Хотя вокруг никого нет. Я оглядываюсь, '
        'начинаю идти домой, но моего дома словно нет. Я иду '
        'по знакомым улицам, но никак не могу найти свой дом. '
        'А чувство слешки растёт. Я чувствую словно дыхание за '
        'спиной, оборачиваюсь и... Сон обрывается."'
        )
    adventure.child_dream = True
    children_1(adventure)


def solo_main_place(adventure):
    solo_ui(adventure.hero)
    print(
        'Вы стоите на центральной площади деревни. Дети куда-то '
        'запропастились. Впереди виднеется вывеска трактира.'
        )
    print(Fore.YELLOW + 'tavern' + Fore.RESET + ' - зайти в трактир')
    if adventure.elder:
        print(
            Fore.YELLOW + 'elder' + Fore.RESET + ' - пойти в дом к '
            'старейшине'
            )
    if adventure.elder2:
        print(
            Fore.YELLOW + 'elder+' + Fore.RESET + ' - пойти в дом к старейшине'
            ' путем, который '
            'посоветовал бармен'
            )
    if adventure.witch:
        print(
            Fore.YELLOW + 'witch' + Fore.RESET + ' - пойти на холм, про '
            'который говорил старейшина Майк'
            )
    inputs.solo_main_place(adventure)


def children_talk_leave(adventure):
    border()
    print(
        'Дети смотрят вам вслед. Девочка говорит: "Он показался '
        'мне хорошим"'
        )
    solo_main_place(adventure)


def tavern_1(adventure):
    solo_ui(adventure.hero)
    print(
        'В пабе почти нет людей. За стойкой бармен с ужасными '
        'синяками под глазами. Вы подходите к нему, он вас словно '
        'не замечает. Про что спросить?'
        )
    print('')
    print(Fore.YELLOW + 'dream' + Fore.RESET + ' - про сон')
    print(Fore.YELLOW + 'elder' + Fore.RESET + ' - про старейшину')
    print(Fore.YELLOW + 'rest' + Fore.RESET + ' - восстановить здоровье')
    print(Fore.YELLOW + 'leave' + Fore.RESET + ' - выйти')
    inputs.tavern_1(adventure)


def tavern_1_elder(adventure):
    border()
    print(
        'Бармен словно проснулся. Поднял глаза. Вяло произнес: '
        '"Вас интересует Майк. Он живет совсем близко, за пабом. '
        'Только когда пойдете к нему обойдите паб слева, а то '
        'собаки совсем дичают от этого сна."'
        )
    adventure.elder2 = True
    adventure.elder = True
    tavern_1(adventure)


def tavern_1_dream(adventure):
    border()
    print(
        'Бармен словно проснулся: '
        '"Сон как сон. Единственное постоянное ощущение присутствия '
        'кого-то, явственное до жути. Я никак не могу из-за этого '
        'выспаться!" Он показал на мешки под глазами.'
        )
    adventure.child_dream = True
    tavern_1(adventure)


def tavern_1_rest(adventure):
    border()
    print(
        'Вы отдыхаете. Здоровье восполнено'
        )
    adventure.hero.hp = adventure.hero.max_hp
    tavern_1(adventure)


def inventory(adventure):
    print('error :(')  # TODO


def game_over():
    border()
    border()
    print('ВЫ ПОГИБЛИ!!!')
    border()
    main_menu()


def elder2(adventure):
    solo_ui(adventure.hero)
    print(
        'Вы доходите до дома старейшины. Стучитесь. Дверь оказывается не '
        'заперта и открывается от вашего стука. Вы настораживаетесь и '
        'проходите внутрь. Из спальни доносятся невнятные звуки. Вы проходите '
        'в спальню, на кровати спит мужчина. Должно быть жто Майк. Вы '
        'подходите к постели и чувствуете чье-то присутствие. Необъяснимое '
        'чувство холодком пробежалось по вашей спине и крепко засело где-то в '
        'области затылка. Паника медленно начинает путать ваши мысли. С каждом'
        ' шагом чувство набирает силу. Кажется, будто воздух вокруг постели'
        ' более густой. Идти становится тяжелее, так же начинает казаться, что'
        ' пространство над постелью как-то неестественно более темное.'
        )
    print(
        'Вы с большим трудом делаете последний шаг. И темнота словно '
        'расступается однако эффект присутствия становится невыносимым. '
        'Вы выхватываете меч:'
        )
    enemy = Person(Fore.MAGENTA + '????', 7, 6, 0.2)
    fight = solo_adventure.SoloBattle(adventure, enemy)
    if fight.if_win:
        print('Вы одолеваете, а собственно что?')
        print(
            Fore.LIGHTRED_EX +
            f'Здоровье: {round(adventure.hero.hp, 1)}/{adventure.hero.max_hp} '
            + Fore.RESET +
            'напишите '
            + Fore.YELLOW +
            'nice'
            + Fore.RESET + ' для продолжения'
            )
        inputs.nice()
        elder3(adventure)
    else:
        game_over()


def elder(adventure):
    border()
    print(
        'Вы проходите за таверну и идете вдоль домов. '
        'Сзади слышится лай. Вы оборачиваетесь и видете собаку с ухоженной '
        'ласняшейся шерстью и одичавшим взглядом. Она бросается на вас:'
        )
    enemy = Person('Собака', 7, 3, 0.1)
    fight = solo_adventure.SoloBattle(adventure, enemy)
    if fight.if_win:
        print(
            Fore.LIGHTRED_EX +
            f'Здоровье: {round(adventure.hero.hp, 1)}/{adventure.hero.max_hp} '
            + Fore.RESET +
            'напишите '
            + Fore.YELLOW +
            'nice'
            + Fore.RESET +
            ' для продолжения'
            )
        inputs.nice()
        print('Вы продолжаете свой путь к дому старейшины.')
        elder2(adventure)
    else:
        game_over()


def elder3(adventure):
    solo_ui(adventure.hero)
    print(
        'Старейшина просыпается, тяжело вздыхает, заспанно смотрит на вас:'
        ' "Мне приснился ужасный сон." Вы тяжело дыша после боя смотрите на '
        'него. Про что спросить у старейшины?'
        )
    print(
        Fore.YELLOW + 'dream' + Fore.RESET + ' про сны, знает ли он с чем'
        ' это связано?'
        )
    print(Fore.YELLOW + 'leave' + Fore.RESET + ' покинуть старейшину')
    inputs.elder3(adventure)


def elder_dream(adventure):
    border()
    print(
        'Майк всполошился и казалось набрался сил. Теперь стало '
        'заметно, что у него тоже синяки под глазами. Он заговорил: '
        '"Я уверен, что в этом замешена ведьма, которая живет на холме'
        ' около деревни. Я считаю вам необходимо наведаться к ней!"'
        )
    adventure.witch = True
    elder3(adventure)


def witch(adventure):
    solo_ui(adventure.hero)
    print(
        'Вы уверенной поступью идете от деревни к холму, про который'
        ' говорил Майк. Вы подходите ближе на холме виднеется небольшой'
        ' дом. Вы чувствуете на двери дома какое-то заклинание.'
        ' Касаетесь ручки и ощущаете как через руку проходит электрический'
        ' разряд!'
        )
    print(Fore.RED + 'Он наносит вам 1 урона!')
    adventure.hero.hp = adventure.hero.hp - 1
    if adventure.hero.hp <= 0:
        game_over()
    else:
        print(
            Fore.LIGHTRED_EX +
            f'Здоровье: {round(adventure.hero.hp, 1)}/{adventure.hero.max_hp} '
            + Fore.RESET +
            'напишите '
            + Fore.YELLOW +
            'nice'
            + Fore.RESET +
            ' для продолжения'
            )
        inputs.nice()
        print('Вы проходите в дом.')
        witch_hut(adventure)


def witch_hut(adventure):
    solo_ui(adventure.hero)
    print(
        'Вы узнаете ту же атмосферу, что была в доме старейшины. Гнетущие '
        'ощущение присутствия. Впереди виднеется небольшая кровать с красивой '
        'женщиной на ней. Ведьме явно снится беспокойный сон, она дергается и '
        'время от времени вскрикивает. Над ней так же как и над Майком '
        'сгустилась темнота, словно бы живая. Вы оголяете меч и твердо '
        'направляетесь к постели. Каждый шаг дается все труднее. Вы подходите '
        'вплотную к постели, протягиваете руку в стальной рукавице к '
        'затемненному пространству. Ведьма неожиданно кричит особенно громко. '
        'Ее тело выгибается дугой на кровати. Еще один стон. И она падает '
        'обратно на кровать и затихает. В этот же момент вы оборачиваетесь'
        '. Чтобы встретить мечом подобие когтей, сотканных из тьмы. Перед вами'
        ' едва заметные в полумраке комнаты виднеются очертания темноты, '
        'напоминающие человека. Но с непропорционально длинными руками и '
        'короткими ногами, а так же со словно неправильной формы головой. Вы'
        ' вступаете в бой с сущностью.'
    )
    enemy = Person(Fore.MAGENTA + 'Демон', 9, 6, 0.2)
    fight = solo_adventure.SoloBattle(adventure, enemy)
    if fight.if_win:
        print('Вы одолеваете демона')
        print(
            Fore.LIGHTRED_EX +
            f'Здоровье: {round(adventure.hero.hp, 1)}/{adventure.hero.max_hp} '
            + Fore.RESET +
            'напишите '
            + Fore.YELLOW +
            'nice'
            + Fore.RESET + ' для продолжения'
            )
        inputs.nice()
        witch_awake(adventure)
    else:
        game_over()


def witch_awake(adventure):
    solo_ui(adventure.hero)
    print(
        'Вы очень тяжело дышите, бой не был из простых. Тварь была очень '
        'изворотлива. Сзади раздается мелодичный женский голос: "Вы убили его.'
        '" Вы оглядываетесь и видите ведьму.  Она каким-то чудом уже успела '
        'надеть платье и теперь светилась юностью и глядела на вас большими '
        'глазами...'
    )
    print(
        Fore.GREEN +
        'Это финал! Спасибо, за игру! Если вам нравятся игры с большим '
        'количеством текста, интересными историями и очень крутой атмосферой'
        ', то я советую sunless sea и sunless skies'
        )
    print(
        'Напишите '
        + Fore.YELLOW +
        'nice'
        + Fore.RESET + ' для выхода в меню'
        )
    inputs.nice()
    main_menu()
