from django.db import models


class Booking(models.Model):
    booking_id = models.BigAutoField(primary_key=True, verbose_name='Номер брони', blank=True)
    person = models.ForeignKey('Person', on_delete=models.CASCADE, verbose_name='Гость')
    room = models.ForeignKey('Room', on_delete=models.SET_NULL, null=True, verbose_name='Комната')
    dates = models.ForeignKey('DateArray', on_delete=models.CASCADE, verbose_name='Даты брони')
    book_status = models.ForeignKey('BookStatuses', on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Статус брони')
    book_creation_date = models.DateField(auto_now_add=True, verbose_name='Дата создания брони', blank=True)

    class Meta:
        verbose_name = 'Брони'
        verbose_name_plural = 'Брони'


class Person(models.Model):
    phone_number = models.CharField(max_length=20, unique=True, primary_key=True, verbose_name='Номер телефона')
    first_name = models.CharField(max_length=32, verbose_name='Имя')
    last_name = models.CharField(max_length=32, verbose_name='Фамилия')
    father_name = models.CharField(max_length=32, verbose_name='Отчество')
    description = models.CharField(max_length=255, null=True, blank=True, verbose_name='Заметки, описание')

    class Meta:
        verbose_name = 'Гости'
        verbose_name_plural = 'Гости'


class Room(models.Model):
    room_number = models.BigAutoField(primary_key=True, verbose_name='Номер комнаты')
    price = models.ForeignKey('Prices', on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Цена в период')
    description = models.CharField(max_length=512, verbose_name='Описание комнаты', blank=True)
    links = models.ManyToManyField('Links', blank=True, verbose_name='Ссылки на фотографии комнаты')

    class Meta:
        verbose_name = 'Комната'
        verbose_name_plural = 'Комнаты'


class Links(models.Model):
    link_id = models.BigAutoField(primary_key=True)
    link = models.CharField(max_length=255, verbose_name='Ссылка')

    class Meta:
        verbose_name = 'Ссылки на фото'
        verbose_name_plural = 'Ссылки на фото'


class DateArray(models.Model):
    array_id = models.BigAutoField(primary_key=True, blank=True)
    arrive_date = models.DateField(verbose_name='Начало промежутка дат')
    leave_date = models.DateField(verbose_name='Конец промежутка дат')
    date_status = models.ForeignKey('DateStatuses', on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Статус промежутка дат')

    class Meta:
        verbose_name = 'Состояние дат'
        verbose_name_plural = 'Состояние дат'


class DateStatuses(models.Model):
    status_id = models.AutoField(primary_key=True)
    status_name = models.CharField(max_length=16, verbose_name='Состояние промежутка дат')


class BookStatuses(models.Model):
    status_id = models.AutoField(primary_key=True)
    status_name = models.CharField(max_length=16, verbose_name='Статус брони')


class Prices(models.Model):
    price_id = models.AutoField(primary_key=True)
    start_date = models.DateField(verbose_name='Дата начала ценового промежутка')
    finish_date = models.DateField(verbose_name='Дата конца ценового промежутка')
    price = models.IntegerField(verbose_name='Цена в заданный промежуток')

    class Meta:
        verbose_name = 'Цены'
        verbose_name_plural = 'Цены'


# создаем тут модель
# если надо добавляем в админку
# потом делаем миграции (makemigrations а потом migrate)
# разобраться почему хост это имя контейнера