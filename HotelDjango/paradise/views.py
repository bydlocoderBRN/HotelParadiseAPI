from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from .models import Room, DateArray, DateStatuses
from .serializers import DateArraySerializer, RoomSerializer


@api_view(["GET"])
def get_all_rooms(request: Request):
    raw_rooms = Room.objects.all().order_by('room_number')
    serialized_rooms = RoomSerializer(raw_rooms, many=True)
    return Response(serialized_rooms.data, status=status.HTTP_200_OK)


@api_view(["GET"])
def get_room(request: Request, room_number):
    raw_room = Room.objects.all().filter(room_number__exact=room_number)
    if raw_room.exists():
        serialized_rooms = RoomSerializer(list(raw_room).pop())
        print(str(serialized_rooms.data))
        return Response(serialized_rooms.data, status=status.HTTP_200_OK)
    else:
        return Response("Комнаты не существует", status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def get_all_dates(request: Request, room_number):
    room = Room.objects.filter(room_number__exact=room_number)
    if room.exists():
        room = list(room).pop()
        raw_dates = DateArray.objects.filter(room=room)
        serialized_dates = DateArraySerializer(list(raw_dates), many=True)
        return Response(serialized_dates.data, status=status.HTTP_200_OK)
    else:
        return Response("Комнаты не существует", status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def get_date_array(request: Request, room_number):
    start_date = request.query_params["start_date"]
    finish_date = request.query_params["finish_date"]
    room = Room.objects.filter(room_number__exact=room_number)
    if room.exists():
        room = list(room).pop()
        raw_dates = DateArray.objects.filter(room=room).filter(arrive_date__gte=start_date, leave_date__lte=finish_date)
        serialized_dates = DateArraySerializer(raw_dates, many=True)
        return Response(serialized_dates.data, status=status.HTTP_200_OK)
    else:
        return Response("Комнаты не существует", status=status.HTTP_400_BAD_REQUEST)


# todo предлагать другие даты, если искомые заняты
# todo очистка дат, которые уже прошли
# ['Значение “05-24-2022” имеет неверный формат даты. Оно должно быть в формате YYYY-MM-DD.']

@api_view(["GET"])
def check_date(request: Request, room_number):
    date = request.query_params.get("date")
    print("DATA!!!!!!!!!!!!!!!!!!")
    print(type(date))
    room = Room.objects.filter(room_number__exact=room_number)
    if not room.exists():
        return Response("Комнаты не существует", status=status.HTTP_400_BAD_REQUEST)
    room = list(room).pop()
    checked_date = DateArray.objects.filter(room=room).filter(arrive_date__lte=date, leave_date__gte=date)
    if checked_date.exists():
        date = DateArraySerializer(list(checked_date).pop())
        return Response(date.data, status.HTTP_200_OK)
    else:
        date_array_obj = DateArray()
        date_array_obj.room = room
        date_array_obj.arrive_date = date
        date_array_obj.leave_date = date
        date_array_obj.date_status = list(DateStatuses.objects.filter(status_name="Свободно")).pop()
        date_array_ser = DateArraySerializer(date_array_obj)
        return Response(date_array_ser.data, status.HTTP_200_OK)


@api_view(["GET"])
def check_date_array(request: Request, room_number):
    sdate = request.query_params.get("start_date")
    fdate = request.query_params.get("finish_date")
    room = Room.objects.filter(room_number__exact=room_number)
    if not room.exists():
        return Response("Комнаты не существует", status=status.HTTP_400_BAD_REQUEST)
    room = list(room).pop()
    checked_dates = DateArray.objects.all(). \
        exclude(arrive_date__lt=sdate, leave_date__lt=sdate). \
        exclude(arrive_date__gt=fdate, leave_date__gt=fdate).filter(room=room)
    if checked_dates.exists():
        date_list = list(checked_dates)
        response_dates = DateArraySerializer(date_list, many=True)
        return Response(response_dates.data, status.HTTP_200_OK)
    else:
        date_array_obj = DateArray()
        date_array_obj.room = room
        date_array_obj.arrive_date = sdate
        date_array_obj.leave_date = fdate
        date_array_obj.date_status = list(DateStatuses.objects.filter(status_name="Свободно")).pop()
        date_array_ser = DateArraySerializer(date_array_obj)
        return Response(date_array_ser.data, status.HTTP_200_OK)
