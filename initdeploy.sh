docker cp /www/server/panel/vhost/cert/looparadise.ru/fullchain.pem hotelparadise_back_dj_web_1:/etc/nginx/fullchain.pem
docker cp /www/server/panel/vhost/cert/looparadise.ru/privkey.pem hotelparadise_back_dj_web_1:/etc/nginx/privkey.pem
docker exec hotelparadise_back_dj_web_1 nginx -s reload
docker cp hotelfront:/usr/src/app /www/wwwroot/looparadise.ru/
docker exec hotelparadise_back_dj_web_1 python manage.py makemigrations
docker exec hotelparadise_back_dj_web_1 python manage.py migrate