from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator
from django.core.validators import MinValueValidator


User = get_user_model()


class Thing(models.Model):
    item_name = models.CharField(
        max_length=45,
        help_text="Имя предмета"
    )
    def_ammount = models.IntegerField(
        default=10,
        validators=[MinValueValidator(1), MaxValueValidator(10)],
        help_text="Защита в %. Максимум 10",
    )
    damage_amount = models.PositiveIntegerField(
        default=5,
        validators=[MinValueValidator(1), MaxValueValidator(10)],
        help_text="Урон. Максимум 10",
    )

    class Meta:
        verbose_name = 'item'

    def __str__(self):
        return self.item_name


class Helmet(Thing):
    class Meta:
        verbose_name = 'helmet'


class Chest(Thing):
    class Meta:
        verbose_name = 'chest'


class FirstWeapon(Thing):
    class Meta:
        verbose_name = 'first_weapon'


class SecondWeapon(Thing):
    class Meta:
        verbose_name = 'second_weapon'


class LegArmor(Thing):
    class Meta:
        verbose_name = 'leg_armor'


class Person(models.Model):
    account = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='champions',
        help_text='Аккаунт воина'
    )
    name = models.CharField(
        max_length=40,
        help_text="Имя персонажа"
    )
    helmet = models.ForeignKey(
        Helmet,
        on_delete=models.CASCADE,
        related_name='person',
        blank=False,
        null=False,
        help_text='Шлем'
    )
    chest = models.ForeignKey(
        Chest,
        on_delete=models.CASCADE,
        related_name='person',
        blank=False,
        null=False,
        help_text='Нагрудник'
    )
    first_weapon = models.ForeignKey(
        FirstWeapon,
        on_delete=models.CASCADE,
        related_name='person',
        blank=False,
        null=False,
        help_text='Первое оружие'
    )
    second_weapon = models.ForeignKey(
        SecondWeapon,
        on_delete=models.CASCADE,
        related_name='person',
        blank=False,
        null=False,
        help_text='Второй оружиеы'
    )
    leg_armor = models.ForeignKey(
        LegArmor,
        on_delete=models.CASCADE,
        related_name='person',
        blank=False,
        null=False,
        help_text='Поножи'
    )


class Paladin(Person):
    base_def = models.PositiveIntegerField(
        default=30,
        help_text="Базовая защита",
    )
    base_health = models.PositiveIntegerField(
        default=300,
        help_text="Базовое хп",
    )
    base_attack = models.PositiveIntegerField(
        default=15,
        help_text="Базовый урон",
    )


class Warrior(Person):
    base_attack = models.PositiveIntegerField(
        default=30,
        help_text="Базовый урон",
    )
    base_def = models.PositiveIntegerField(
        default=15,
        help_text="Базовая защита",
    )
    base_health = models.PositiveIntegerField(
        default=150,
        help_text="Базовое хп",
    )
