from django.contrib import admin
from .models import *

#todo почтовые оповещения, оповещения на телефон.
#todo вьюсеты и роутеры разобраться
#todo автопродление сертификата через крон)))

class BookingAdmin(admin.ModelAdmin):
    list_display = ('room', 'person', 'dates', 'book_status', 'book_creation_date')
admin.site.register(Booking, BookingAdmin)


class PersonAdmin(admin.ModelAdmin):
    list_display = ('phone_number', 'last_name', 'first_name', 'father_name')
admin.site.register(Person, PersonAdmin)


class RoomAdmin(admin.ModelAdmin):
    list_display = ('room_number', 'price')
admin.site.register(Room, RoomAdmin)


class PricesAdmin(admin.ModelAdmin):
    list_display = ('price', 'start_date', 'finish_date')
admin.site.register(Prices, PricesAdmin)


class DateArrayAdmin(admin.ModelAdmin):
    list_display = ('date_status', 'arrive_date', 'leave_date')
admin.site.register(DateArray, DateArrayAdmin)


class LinksAdmin(admin.ModelAdmin):
    list_display = ('link',)
admin.site.register(Links, LinksAdmin)


admin.site.register(DateStatuses)
admin.site.register(BookStatuses)


# Register your models here.
