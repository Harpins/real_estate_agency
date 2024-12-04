from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from phonenumber_field import modelfields


class Flat(models.Model):
    created_at = models.DateTimeField(
        'Когда создано объявление',
        default=timezone.now,
        db_index=True)

    description = models.TextField('Текст объявления', blank=True)
    price = models.IntegerField('Цена квартиры', db_index=True)

    town = models.CharField(
        'Город, где находится квартира',
        max_length=50,
        db_index=True)
    town_district = models.CharField(
        'Район города, где находится квартира',
        max_length=50,
        blank=True,
        help_text='Чертаново Южное')
    address = models.TextField(
        'Адрес квартиры',
        help_text='ул. Подольских курсантов д.5 кв.4')
    floor = models.CharField(
        'Этаж',
        max_length=3,
        help_text='Первый этаж, последний этаж, пятый этаж')

    rooms_number = models.IntegerField(
        'Количество комнат в квартире',
        db_index=True)
    living_area = models.IntegerField(
        'количество жилых кв.метров',
        null=True,
        blank=True,
        db_index=True)

    has_balcony = models.NullBooleanField('Наличие балкона', db_index=True)
    active = models.BooleanField('Активно-ли объявление', db_index=True)
    construction_year = models.IntegerField(
        'Год постройки здания',
        null=True,
        blank=True,
        db_index=True)

    new_building = models.BooleanField(
        'Новостройка', db_index=True, default=False)

    liked_by = models.ManyToManyField(
        User, blank=True, related_name='liked_flats', verbose_name='Кто лайкнул')

    def __str__(self):
        return f'{self.town}, {self.address} ({self.price}р.)'


class Feedback(models.Model):
    author = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL,
                               related_name='feedbacks', verbose_name='Автор жалобы')
    flat = models.ForeignKey(Flat, null=True, blank=True, on_delete=models.SET_NULL,
                                related_name='complaints', verbose_name='Квартира, на которую пожаловались')
    message = models.TextField('Текст жалобы', blank=True)

    def __str__(self):
        return f'{self.author} | {self.flat} | {self.message[:30]}'


class Owner(models.Model):
    name = models.CharField('ФИО владельца', max_length=200, db_index=True)
    phonenumber = models.CharField('Номер владельца', max_length=20)
    pure_phonenumber = modelfields.PhoneNumberField(
        'Нормализованный номер владельца', max_length=20, null=True, blank=True)
    flats = models.ManyToManyField(
        Flat, blank=True, related_name='owners', verbose_name='Квартиры в собственности')

    def __str__(self):
        return f'{self.name}'
