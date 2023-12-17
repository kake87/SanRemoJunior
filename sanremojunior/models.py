from django.db import models
from django.core.validators import EmailValidator
from django.utils.translation import gettext_lazy as _

class Zayavka(models.Model):
    NOMINATIONS = [
        ('pop', 'Поп-музыка'),
        ('rock', 'Рок'),
        ('jazz', 'Джаз'),
        ('classical', 'Академический вокал'),
        ('folk', 'Фолк'),
        ('rap', 'Рэп'),
    ]
    
    AGE_CATEGORY = [
        ('A1', 'A1 (6-9)'),
        ('A2', 'A2 (10-12)'),
        ('A3', 'A3 (13-15)'),
    ]

    surname = models.CharField(verbose_name="Фамилия", max_length=50)
    name = models.CharField(verbose_name="Имя", max_length=50)
    country_city = models.CharField(verbose_name="Страна и город рождения", max_length=100)
    address = models.CharField(verbose_name="Адрес", max_length=75, null=True, blank=True)
    birthdate = models.DateField(verbose_name="Дата рождения")
    nomination = models.CharField(verbose_name="Номинация", choices=NOMINATIONS, max_length=20)
    age_category = models.CharField(verbose_name="Возрастная группа", choices=AGE_CATEGORY, max_length=20)
    phone = models.CharField(verbose_name="Номер телефона", max_length=20, null=True, blank=True)
    email = models.EmailField(verbose_name="Электронная почта", validators=[EmailValidator(message=_("Введите корректный адрес электронной почты"))])
    study_place = models.CharField(verbose_name="Учебное заведение", max_length=50, null=True, blank=True)
    teacher_fio = models.CharField(verbose_name="ФИО преподавателя(руководителя)", max_length=100, null=True, blank=True)
    concertmaster_fio = models.CharField(verbose_name="ФИО концертмейстера", max_length=100, null=True, blank=True)
    application_date = models.DateTimeField(verbose_name="Время и дата заявки", auto_now_add=True)
    identity_document = models.FileField(verbose_name="Удостоверение личности", upload_to="identity_documents/", null=True, blank=True)
    payment_receipt = models.FileField(verbose_name="Квитанция об оплате", upload_to="payment_receipts/", null=True, blank=True)
    participant_photo = models.ImageField(verbose_name="Фотография участника", upload_to="participant_photos/", null=True, blank=True)
    audio_record = models.FileField(verbose_name="Прикрепленная аудиозапись", upload_to="audio_records/", null=True, blank=True)
    song_name = models.CharField(verbose_name="Название произведения", null=True, blank=True, max_length=50)
    song_author = models.CharField(verbose_name="Автор произведения", null=True, blank=True, max_length=20)
    duration_of_song = models.DurationField(verbose_name="Длительность песни", null=True, blank=True)


    def __str__(self):
        return f"{self.surname} {self.name}"
    

