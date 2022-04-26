from django.shortcuts import render

from django.http import HttpResponse
from rest_framework.views import APIView
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework import status


class BookingView(APIView):

    def get(self, request, format=None):
        rawBookings = Booking.objects.all()
        serializedBookings = BookingSerializer(rawBookings, many=True)
        return Response(serializedBookings.data, status=status.HTTP_200_OK)
