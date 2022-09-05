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
        fields = ['status_id', 'status_name']


class DateStatusesSerializer(serializers.ModelSerializer):
    class Meta:
        model = DateStatuses
        fields = ['status_id', 'status_name']


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
        fields = ['room_number', 'description', 'price', 'links']


class BookingSerializer(serializers.ModelSerializer):
    person = PersonSerializer(required=False)
    room = serializers.PrimaryKeyRelatedField(required=False, queryset=Room.objects.all())
    dates = DateArraySerializer(required=True)
    book_status = BookStatusesSerializer(required=False)

    class Meta:
        model = Booking
        fields = ['person', 'room', 'dates', 'book_status']



    def create(self, validated_data):
        room = None
        person = Person(**validated_data['person'])  #передаем все поля гостя
        person.save()                                #апдейтим или создаем нового
        if 'room' in validated_data:
            room = validated_data['room']   #поскольку отношение с комнатой у нас по pk, то сериалайзер сразу возвращает объект комнаты
        dates = DateArray(**validated_data['dates'])
        dates.date_status = DateStatuses.objects.get(status_name='В обработке')
        dates.save()  #Создаем новый объект дат
        book_status = BookStatuses.objects.get(status_name='В обработке') # присваиваем статус букингу
        book = Booking(person=person, room=room, dates=dates, book_status=book_status)
        book.save() #создаем и сохраняем новую бронь

    def update(self, instance, validated_data):
        for field in validated_data.keys():
            instance[field] = validated_data[field]
        instance.save()

