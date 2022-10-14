from django.urls import path
from . import views

urlpatterns = [
    path('room/all', views.get_all_rooms),
    path('room/<int:room_number>', views.get_room),
    path('room/<int:room_number>/dates/all', views.get_all_dates),
    path('room/<int:room_number>/dates/array', views.get_date_array),
    path('room/<int:room_number>/dates/check', views.check_date),
    path('room/<int:room_number>/dates/check_interval', views.check_date_array)

]
