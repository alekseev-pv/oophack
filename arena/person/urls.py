from django.urls import path
from . import views

app_name = 'person'

urlpatterns = [
    path('', views.index, name='index'),   # Инфа о всей бойцах
    path('profile/<str:username>/',        # Профиль пользователя
         views.profile, name='profile'),
    path('paladin_create/', views.paladin_create, name='paladin_create'),
    path('warrior_create/', views.warrior_create, name='warrior_create'),
    path('fight_vs_someone/<str:username>/fight/',  # Битва против рандома
         views.fight_vs_someone, name='fight_vs_someone'),
    path('fight_vs_u_want/<str:username>/<int:enemy_id>/fight/',
         views.fight_vs_u_want, name='fight_vs_u_want'),  # Против конкретного
]
