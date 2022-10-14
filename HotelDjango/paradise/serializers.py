from rest_framework import serializers

from .models import *


class PricesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prices
        fields = ['start_date', 'finish_date', 'price']


class DateStatusesSerializer(serializers.ModelSerializer):
    class Meta:
        model = DateStatuses
        fields = ['status_id', 'status_name']


class LinksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Links
        fields = ['link']


class DateArraySerializer(serializers.ModelSerializer):
    date_status = DateStatusesSerializer(required=False, read_only=True)

    class Meta:
        model = DateArray
        fields = ['arrive_date', 'leave_date', 'date_status']


class RoomSerializer(serializers.ModelSerializer):
    price = PricesSerializer(required=False, read_only=True)
    links = LinksSerializer(many=True, read_only=True)

    class Meta:
        model = Room
        fields = ['room_number', 'title', 'description', 'price', 'links']
