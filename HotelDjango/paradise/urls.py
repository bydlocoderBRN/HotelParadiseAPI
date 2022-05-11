from django.urls import path
from . import views

#todo router

urlpatterns = [
    path('booking/all', views.BookingView.as_view()),
    path('booking/add', views.BookingView.as_view()),
    path('room/all', views.RoomViewTemp.as_view()),
    path('room/<int:room_number>', views.RoomView.as_view()),
    path('dates/all', views.DateArrayView.as_view())
]

