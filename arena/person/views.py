from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from .models import Paladin, Person, Warrior
from .forms import PaladinForm, WarriorForm
import random

User = get_user_model()


def battle_log(username):
    user = get_object_or_404(User, username=username)
    user_champions = user.champions.all()
    user_champ = user_champions[0]

    all_persons = Person.objects.all()
    person_count = all_persons.count()
    random_id = random.randint(1, person_count)
    enemy_champ = all_persons[random_id - 1]

    battle_log = []

    enemy_def: str = (enemy_champ.helmet.def_ammount
                      + enemy_champ.chest.def_ammount
                      + enemy_champ.first_weapon.def_ammount
                      + enemy_champ.second_weapon.def_ammount
                      + enemy_champ.leg_armor.def_ammount + 15
                      )
    user_def = (user_champ.helmet.def_ammount +
                user_champ.chest.def_ammount +
                user_champ.first_weapon.def_ammount +
                user_champ.second_weapon.def_ammount +
                user_champ.leg_armor.def_ammount + 15
                )
    enemy_damage = (enemy_champ.helmet.damage_amount +
                    enemy_champ.chest.damage_amount +
                    enemy_champ.first_weapon.damage_amount +
                    enemy_champ.second_weapon.damage_amount +
                    enemy_champ.leg_armor.damage_amount + 15
                    )
    user_damage = (user_champ.helmet.damage_amount +
                   user_champ.chest.damage_amount +
                   user_champ.first_weapon.damage_amount +
                   user_champ.second_weapon.damage_amount +
                   user_champ.leg_armor.damage_amount + 15
                   )
    final_enemy_damage = enemy_damage - enemy_damage*(user_def/100)
    final_user_damage = user_damage - user_damage*(enemy_def/100)
    enemy_hp = 150
    user_hp = 150
    TURNES = 20

    def introduce():
        battle_log.append(
            f'В этой схватке участвуют {user_champ.name}'
            f'и {enemy_champ.name}'
        )

    def fighting():
        battle_user_hp = user_hp
        battle_enemy_hp = enemy_hp
        for turn in range(TURNES):
            if battle_enemy_hp > 0:
                battle_user_hp = battle_user_hp - final_enemy_damage
                battle_log.append(
                    f'{enemy_champ.name} наносит удар - '
                    f'{user_champ.name} получает урон '
                    f'{final_enemy_damage}.'
                    f'У него остается {battle_user_hp} здоровья'
                )
            else:
                battle_log.append(f'{enemy_champ.name} повержен.')
                break

            if battle_user_hp > 0:
                battle_enemy_hp = battle_enemy_hp - final_user_damage
                battle_log.append(
                    f'{user_champ.name} наносит удар - '
                    f'{enemy_champ.name} получает урон '
                    f'{final_user_damage}.'
                    f'У него остается {battle_enemy_hp} здоровья'
                )
            else:
                battle_log.append(f'{user_champ.name} повержен.')
                break

    introduce()
    fighting()
    return battle_log


def fight_vs_someone(request, username):
    loggs = battle_log(username)
    context = {
        'loggs': loggs,
    }
    return render(request, 'battles/fight_vs_someone.html', context)


def fight_vs_u_want(request, username, enemy_id):
    loggs = battle_log(username, enemy_id)

    context = {
        'loggs': loggs,
    }
    return render(request, 'battles/fight_vs_u_want.html', context)


def index(request):
    paladins_list = Paladin.objects.all()
    warriors_list = Warrior.objects.all()

    context = {
        'paladins_list': paladins_list,
        'warriors_list': warriors_list,
    }

    return render(request, 'info/index.html', context)


def profile(request, username):
    user = get_object_or_404(User, username=username)
    user_champion = user.person.all()
    context = {
        'user_champion': user_champion,
    }

    return render(request, 'info/profile.html', context)


@login_required
def paladin_create(request):
    if request.method != 'POST':
        form = PaladinForm()
        return render(request, 'create/paladin.html', {'form': form})
    form = PaladinForm(request.POST or None)
    if form.is_valid():
        if Paladin.objects.filter(account=request.user).exists():
            Paladin.objects.filter(account=request.user).delete()
        if Warrior.objects.filter(account=request.user).exists():
            Warrior.objects.filter(account=request.user).delete()   
        champion = form.save(commit=False)
        champion.account = request.user
        champion.save()
        return redirect('person:index')
    return render(request, 'create/paladin.html', {'form': form})


@login_required
def warrior_create(request):
    if request.method != 'POST':
        form = WarriorForm()
        return render(request, 'create/warrior.html', {'form': form})
    form = WarriorForm(request.POST or None)
    if form.is_valid():
        if Paladin.objects.filter(account=request.user).exists():
            Paladin.objects.filter(account=request.user).delete()
        if Warrior.objects.filter(account=request.user).exists():
            Warrior.objects.filter(account=request.user).delete()
        champion = form.save(commit=False)
        champion.author = request.user
        champion.save()
        return redirect('person:profile', username=request.user.username)
    return render(request, 'create/warrior.html', {'form': form})
