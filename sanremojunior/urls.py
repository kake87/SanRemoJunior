from django.urls import path
from .views import index, prices, rules, about_organizators, concurs_video, kz_index, kzorg, kzrules, applications, kzprice
from django.contrib.auth.decorators import login_required
from django.contrib.admin import site


site.login = login_required(site.login)

urlpatterns = [
    path('', index, name='Главная'),
    path('prices', prices, name="Проживание"),
    path('rules', rules, name="Правила"),
    path('organizators', about_organizators, name='Организаторы'),
    path('concurs_video', concurs_video, name='Concurs Video'),
    path('kzindex', kz_index, name='Бас бет'),
    path('kzorg', kzorg, name='Ұйымдастырушылар'),
    path('kzrules', kzrules, name='Конкурс шарттары'),
    path('kzprice', kzprice, name='Тұру бағасы'),
    path('applications', applications, name="APPLICATIONS")
]

