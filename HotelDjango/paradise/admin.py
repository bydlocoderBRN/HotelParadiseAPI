from django.contrib import admin

from .models import Room, Prices, DateArray, Links, DateStatuses


# todo почтовые оповещения, оповещения на телефон.
# todo автопродление сертификата через крон)))
# FSFSDFSDF

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
