from django.db import models


class Booking(models.Model):
    person = models.ForeignKey('Person', on_delete=models.SET_NULL, null=True)
    room = models.ForeignKey('Room', on_delete=models.SET_NULL, null=True)
    dates = models.ForeignKey('DateArray', on_delete=models.CASCADE)
    book_status = models.ForeignKey('BookStatuses', on_delete=models.SET_NULL, null=True)


class Person(models.Model):
    phone_number = models.CharField(max_length=20)
    first_name = models.CharField(max_length=32, unique=True)
    last_name = models.CharField(max_length=32)
    father_name = models.CharField(max_length=32)
    description = models.CharField(max_length=255, null=True)


class Room(models.Model):
    price = models.IntegerField()
    description = models.CharField(max_length=512)
    links = models.ManyToManyField('Links')


class Links(models.Model):
    link = models.CharField(max_length=255)


class DateArray(models.Model):
    arrive_date = models.DateField()
    leave_date = models.DateField()
    date_status = models.ForeignKey('DateStatuses', on_delete=models.SET_NULL, null=True)


class DateStatuses(models.Model):
    status = models.CharField(max_length=16)


class BookStatuses(models.Model):
    status = models.CharField(max_length=16)





# создаем тут модель
# если надо добавляем в админку
# потом делаем миграции (makemigrations а потом migrate)
# разобраться почему хост это имя контейнера