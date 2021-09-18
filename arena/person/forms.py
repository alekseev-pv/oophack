from django import forms
from django.forms.widgets import Textarea
from .models import Paladin, Warrior


class PaladinForm(forms.ModelForm):
    class Meta():
        model = Paladin
        fields = ('name', 'helmet', 'chest', 'helmet', 'first_weapon',
                  'second_weapon', 'leg_armor',)
        widgets = {
            'name': Textarea,
        }


class WarriorForm(forms.ModelForm):
    class Meta():
        model = Warrior
        fields = ('name', 'helmet', 'chest', 'helmet', 'first_weapon',
                  'second_weapon', 'leg_armor',)
        widgets = {
            'name': Textarea,
        }
