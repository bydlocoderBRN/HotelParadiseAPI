from django.shortcuts import render

from django.http import HttpResponse
from rest_framework.views import APIView
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework import status
from django.db import models

#todo viewsets


class BookingView(APIView):

    def get(self, request):
        queryset = Booking.objects.all()
        serialized_bookings = BookingSerializer(queryset, many=True)
        return Response(serialized_bookings.data, status=status.HTTP_200_OK)

    def post(self, request):
        booking_raw = request.data
        serialized_booking = BookingSerializer(data=booking_raw)
        if serialized_booking.is_valid(raise_exception=True):
            serialized_booking.create(serialized_booking.validated_data)
            return Response('Book created', status=status.HTTP_200_OK)
        else:
            return Response('Body is not valid', status=status.HTTP_400_BAD_REQUEST)


class RoomViewTemp(APIView):
    def get(self, request):
        raw_rooms = Room.objects.order_by('room_number')
        serialized_rooms = RoomSerializer(raw_rooms, many=True)
        return Response(serialized_rooms.data, status=status.HTTP_200_OK)


class RoomView(APIView):

    def get(self, request, room_number):
        try:
            room = Room.objects.get(room_number=room_number)
        except models.ObjectDoesNotExist:
            return Response("Комнаты с таким номером не существует", status=status.HTTP_400_BAD_REQUEST)
        else:
            serialized_room = RoomSerializer(room)
            return Response(serialized_room.data, status=status.HTTP_200_OK)


class DateArrayView(APIView):

    def get(self, request):
        raw_dates = DateArray.objects.all()
        serialized_dates = DateArraySerializer(raw_dates, many=True)
        return Response(serialized_dates.data, status=status.HTTP_200_OK)