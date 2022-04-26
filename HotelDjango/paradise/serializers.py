from rest_framework import serializers

from .models import *


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ['phone_number', 'first_name', 'last_name', 'father_name', 'description']


class PricesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prices
        fields = ['start_date', 'finish_date', 'price']


class BookStatusesSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookStatuses
        fields = ['status']


class DateStatusesSerializer(serializers.ModelSerializer):
    class Meta:
        model = DateStatuses
        fields = ['status']


class LinksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Links
        fields = ['link']


class DateArraySerializer(serializers.ModelSerializer):
    date_status = DateStatusesSerializer(required=False)

    class Meta:
        model = DateArray
        fields = ['arrive_date', 'leave_date', 'date_status']


class RoomSerializer(serializers.ModelSerializer):
    price = PricesSerializer(required=False)
    links = LinksSerializer(many=True)

    class Meta:
        model = Room
        fields = ['description', 'price', 'links']


class BookingSerializer(serializers.ModelSerializer):
    person = PersonSerializer(required=False)
    room = serializers.PrimaryKeyRelatedField(required=False, queryset=Room.objects.all())
    dates = DateArraySerializer(required=True)
    book_status = BookStatusesSerializer(required=False)

    class Meta:
        model = Booking
        fields = ['person', 'room', 'dates', 'book_status']

    def create(self, validated_data):
        person = None
        room = None

        if 'person' in validated_data:
            person = validated_data['person']
            person.save()
        if 'room' in validated_data:
            roomPK = validated_data['room']
            room = Room.objects.get(pk=roomPK)
        dates = validated_data['dates']
        dates['date_status'] = DateStatuses(status='processing')
        book_status = BookStatuses(status='free')
        book = Booking(person=person, room=room, dates=dates, book_status=book_status)
        book.save()

    def update(self, instance, validated_data):
        for field in validated_data.keys():
            instance[field] = validated_data['field']

        instance.save()