from django.test import TestCase
from paradise.models import Room, DateStatuses, DateArray
from rest_framework.response import Response


class ModelsTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        room = Room()
        room.room_number = 1
        room.title = "Тестовая первая комната"
        room.description = "Testtest"
        room.save()
        status_bad = DateStatuses()
        status_bad.status_name = "Занято"
        status_bad.save()
        status_good = DateStatuses()
        status_good.status_name = "Свободно"
        status_good.save()
        status_processing = DateStatuses()
        status_processing.status_name = "В обработке"
        status_processing.save()
        days = 1
        while days < 30:
            date_arr = DateArray()
            date_arr.arrive_date = f"2022-01-{days}"
            days += 4
            date_arr.leave_date = f'2022-01-{days}'
            date_arr.date_status = status_bad
            date_arr.room = room
            date_arr.save()
            days += 4

    def test_check_one_date(self):
        resp = self.check_one_date("2022-01-05")
        date_status = resp.data["date_status"]
        self.assertEqual(date_status.get("status_name"), "Занято")
        resp = self.check_one_date("2022-01-06")
        date_status = resp.data["date_status"]
        self.assertEqual(date_status.get("status_name"), "Свободно")

    def test_check_date_array(self):
        resp = self.check_date_array("2022-01-06", "2022-01-08")
        stat = resp.data.get("date_status").get("status_name")
        self.assertEqual(stat, "Свободно")
        dates_to_check = [("2022-01-03", "2022-01-08"),
                          ("2022-01-06", "2022-01-12"),
                          ("2022-01-18", "2022-01-21"),
                          ("2022-01-06", "2022-01-16")]
        for dates in dates_to_check:
            resp = self.check_date_array(dates[0], dates[1])
            for date_array in resp.data:
                stat = date_array.get("date_status").get("status_name")
                self.assertEqual(stat, "Занято")

    def test_get_dates_array(self):
        resp: Response = self.client.get("/paradise/room/1/dates/array?start_date=2022-01-01&finish_date=2022-01-29")
        dates = list(resp.data)
        print("DATEA!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print(dates)
        self.assertEqual(len(dates), 4)

    def check_one_date(self, date) -> Response:
        resp: Response = self.client.get(f"/paradise/room/1/dates/check?date={date}")
        return resp

    def check_date_array(self, start_date, finish_date) -> Response:
        resp: Response = self.client.get(
            f"/paradise/room/1/dates/check_interval?start_date={start_date}&finish_date={finish_date}")
        return resp
