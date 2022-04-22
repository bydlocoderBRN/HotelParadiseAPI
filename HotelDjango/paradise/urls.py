from django.urls import path
from .views import PersonView
from . import views

urlpatterns = [
    path('get_person', PersonView.as_view()),
]

