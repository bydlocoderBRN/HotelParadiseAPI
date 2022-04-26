from django.urls import path
from . import views

urlpatterns = [
    path('get_person', views.BookingView.as_view()),
]

