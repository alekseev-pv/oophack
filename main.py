from heroes import in_game
import random

while len(in_game) > 1:
    para = random.choices(in_game, k=2)
    if para[0]!=para[1]:
        para[0].attacks(para[1])
        if para[1].health <= 0:
            in_game.remove(para[1])
        else:
            para[1].attacks(para[0])
        if para[0].health <= 0:
            in_game.remove(para[0])
print(len(f'*Победитель Арены - {in_game[0].name}*')*'*')
print (f'*Победитель Арены - {in_game[0].name}*')
print(len(f'*Победитель Арены - {in_game[0].name}*')*'*')