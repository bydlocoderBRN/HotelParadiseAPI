from django.db import models


class Prices(models.Model):
    price_id = models.AutoField(primary_key=True)
    start_date = models.DateField(verbose_name='Дата начала ценового промежутка')
    finish_date = models.DateField(verbose_name='Дата конца ценового промежутка')
    price = models.IntegerField(verbose_name='Цена в заданный промежуток')

    class Meta:
        verbose_name = 'Цены'
        verbose_name_plural = 'Цены'

    def __str__(self):
        return str(self.price)


class Room(models.Model):
    room_number = models.BigAutoField(primary_key=True, verbose_name='Номер комнаты')
    title = models.CharField(max_length=128, null=True, blank=True)
    price = models.ForeignKey(Prices, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Цена в период')
    description = models.CharField(max_length=512, verbose_name='Описание комнаты', blank=True)

    # dates = []
    # links = []
    class Meta:
        verbose_name = 'Комната'
        verbose_name_plural = 'Комнаты'

    def __str__(self):
        return str(self.room_number)


class Links(models.Model):
    link_id = models.BigAutoField(primary_key=True)
    link = models.CharField(max_length=255, verbose_name='Ссылка')
    title = models.CharField(max_length=64, blank=True, null=True)
    room = models.ForeignKey(Room, related_name='links', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Ссылки на фото'
        verbose_name_plural = 'Ссылки на фото'

    def __str__(self):
        return str(self.link)


class DateStatuses(models.Model):
    status_id = models.AutoField(primary_key=True)
    status_name = models.CharField(max_length=16, verbose_name='Состояние промежутка дат')

    def __str__(self):
        return self.status_name


class DateArray(models.Model):
    array_id = models.BigAutoField(primary_key=True, blank=True)
    arrive_date = models.DateField(verbose_name='Начало промежутка дат')
    leave_date = models.DateField(verbose_name='Конец промежутка дат')
    date_status = models.ForeignKey(DateStatuses,
                                    on_delete=models.SET_NULL,
                                    null=True, blank=True,
                                    verbose_name='Статус дат')
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='dates')

    class Meta:
        verbose_name = 'Состояние дат'
        verbose_name_plural = 'Состояние дат'

    def __str__(self):
        return "C " + str(self.arrive_date) + " до " + str(self.leave_date)
