from django.shortcuts import render

from django.http import HttpResponse
from rest_framework.views import APIView
from .models import Person
from .serializers import PersonSerializer
from rest_framework.response import Response
from rest_framework import status


class PersonView(APIView):

    def get(self, request, format=None):
        persons = Person.objects.all()
        serializer = PersonSerializer(persons)
        return Response(serializer.data, status=status.HTTP_200_OK)
