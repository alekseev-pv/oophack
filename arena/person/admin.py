from django.contrib import admin
from .models import Paladin, Warrior, LegArmor, Person
from .models import Helmet, Chest, FirstWeapon, SecondWeapon


class PersonAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'helmet', 'chest', 'first_weapon',
                    'second_weapon', 'leg_armor')
    list_editable = ('name', 'helmet', 'chest', 'first_weapon',
                     'second_weapon', 'leg_armor')
    search_fields = ('name',)
    list_filter = ('name',)
    empty_value_display = '-пусто-'


class PaladinAdmin(admin.ModelAdmin):
    list_display = ('account', 'name', 'base_health', 'base_attack',
                    'base_def', 'helmet', 'chest', 'first_weapon',
                    'second_weapon', 'leg_armor')
    list_editable = ('name', 'base_health', 'base_attack',
                     'base_def', 'helmet', 'chest', 'first_weapon',
                     'second_weapon', 'leg_armor')
    search_fields = ('name',)
    list_filter = ('name',)
    empty_value_display = '-пусто-'


class WarriorAdmin(admin.ModelAdmin):
    list_display = ('account', 'name', 'base_health', 'base_attack',
                    'base_def', 'helmet', 'chest', 'first_weapon',
                    'second_weapon', 'leg_armor')
    list_editable = ('name', 'base_health', 'base_attack',
                     'base_def', 'helmet', 'chest', 'first_weapon',
                     'second_weapon', 'leg_armor')
    search_fields = ('name',)
    list_filter = ('name',)
    empty_value_display = '-пусто-'


class HelmetAdmin(admin.ModelAdmin):
    list_display = ('pk', 'item_name', 'def_ammount', 'damage_amount')
    list_editable = ('item_name', 'def_ammount', 'damage_amount')
    search_fields = ('item_name',)
    list_filter = ('item_name',)
    empty_value_display = '-пусто-'


class ChestAdmin(admin.ModelAdmin):
    list_display = ('pk', 'item_name', 'def_ammount', 'damage_amount')
    list_editable = ('item_name', 'def_ammount', 'damage_amount')
    search_fields = ('item_name',)
    list_filter = ('item_name',)
    empty_value_display = '-пусто-'


class FirstWeaponAdmin(admin.ModelAdmin):
    list_display = ('pk', 'item_name', 'def_ammount', 'damage_amount')
    list_editable = ('item_name', 'def_ammount', 'damage_amount')
    search_fields = ('item_name',)
    list_filter = ('item_name',)
    empty_value_display = '-пусто-'


class SecondWeaponAdmin(admin.ModelAdmin):
    list_display = ('pk', 'item_name', 'def_ammount', 'damage_amount')
    list_editable = ('item_name', 'def_ammount', 'damage_amount')
    search_fields = ('item_name',)
    list_filter = ('item_name',)
    empty_value_display = '-пусто-'


class LegArmorAdmin(admin.ModelAdmin):
    list_display = ('pk', 'item_name', 'def_ammount', 'damage_amount')
    list_editable = ('item_name', 'def_ammount', 'damage_amount')
    search_fields = ('item_name',)
    list_filter = ('item_name',)
    empty_value_display = '-пусто-'


admin.site.register(Person, PersonAdmin)
admin.site.register(Paladin, PaladinAdmin)
admin.site.register(Warrior, WarriorAdmin)
admin.site.register(Helmet, HelmetAdmin)
admin.site.register(Chest, ChestAdmin)
admin.site.register(FirstWeapon, FirstWeaponAdmin)
admin.site.register(SecondWeapon, SecondWeaponAdmin)
admin.site.register(LegArmor, LegArmorAdmin)
