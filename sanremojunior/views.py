from django.shortcuts import render
from django.http import HttpResponse
from .forms import ZayavkaForm
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from urllib.parse import quote
import os


def index(request):
    title = "Sanremo Junior Kazakhstan | Главная страница"
    form = ZayavkaForm()

    if request.method == "POST":
        form = ZayavkaForm(request.POST, request.FILES)

        if form.is_valid():
            zayavka_instance = form.save(commit=False)
            folder_name = f"{zayavka_instance.surname}_{zayavka_instance.name}"
            file_storage = FileSystemStorage(location="media")

            for field_name, uploaded_file in request.FILES.items():
                if uploaded_file:
                    file_name = f"{zayavka_instance.surname}_{zayavka_instance.name}_{uploaded_file.name}"
                    folder_path = os.path.join(file_storage.location, folder_name)
                    os.makedirs(folder_path, exist_ok=True)
                    file_path = os.path.join(folder_name, file_name)
                    file_storage.save(file_path, uploaded_file)
                    setattr(zayavka_instance, field_name, file_path)

            zayavka_instance.save()

    context = {'title': title, 'form': form}
    return render(request, 'index.html', context=context)


def prices(request):
    title = "Стоимость проживания | Sanremo Junior Kazakhstan"
    return render(request, 'prices.html', context={'title':title})

def rules(request):
    title = "Положение о конкурсе | Sanremo Junior Kazakhstan"
    return render(request, 'rules.html', context={'title':title})

def about_organizators(request):
    title = "Организаторы | Sanremo Junior Kazakhstan"
    return render(request, 'organizators.html', context={'title':title})

def concurs_video(request):
    pass

def kz_index(request):
    title = "San"
    form = ZayavkaForm()

    if request.method == "POST":
        form = ZayavkaForm(request.POST, request.FILES)

        if form.is_valid():
            zayavka_instance = form.save(commit=False)
            folder_name = f"{zayavka_instance.surname}_{zayavka_instance.name}"
            file_storage = FileSystemStorage(location="media")

            for field_name, uploaded_file in request.FILES.items():
                if uploaded_file:
                    file_name = f"{zayavka_instance.surname}_{zayavka_instance.name}_{uploaded_file.name}"
                    folder_path = os.path.join(file_storage.location, folder_name)
                    os.makedirs(folder_path, exist_ok=True)
                    file_path = os.path.join(folder_name, file_name)
                    file_storage.save(file_path, uploaded_file)
                    setattr(zayavka_instance, field_name, file_path)

            zayavka_instance.save()

    context = {'title': title, 'form': form}
    return render(request, 'kz/kzindex.html', context=context)

def kzprice(request):
    return render(request, 'kz/kzprice.html')

def kzorg(request):
    return render(request, 'kz/kzorg.html')

def kzrules(request):
    return render(request, 'kz/kzrules.html')


@login_required
def applications(request):
    return render(request, 'applications_base.html')