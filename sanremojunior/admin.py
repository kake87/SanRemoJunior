from django.contrib import admin
from .models import Zayavka


@admin.register(Zayavka)
class ZayavkaAdmin(admin.ModelAdmin):
    list_display = ('surname', 'name', 'birthdate', 'nomination', 'age_category', 'application_date')
    search_fields = ('surname', 'name', 'birthdate', 'nomination', 'age_category')
    list_filter = ('nomination', 'age_category', 'application_date')