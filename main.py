from models import Battle

if __name__ == "__main__":
    count_heroes = int(input("Сколько войнов должно участвовать в битве?\n>>>"))
    battle = Battle(count_heroes=count_heroes)
    battle.battle_intro()
    battle.start_battle()
