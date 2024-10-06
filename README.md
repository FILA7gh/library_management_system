# library_management_system
for Megacom with love from Aftandil)

# Предисловие: 
В общем я постарался написать хороший проект но времени не хватило, из 4 дней свободного времени было всего где то пол дня
из за этого пришлось найти что то среднее между скоростью и качеством, но думаю я построил неплохую архитектуру, 
которая придерживается таких принципов как dry, kiss (но не SOLID), хочу отметить еще то что не хватило времени 
на тесты (не полностью и не совсем рабочие), не успел подключить flower в докере, протестировать селери таски и смс на почту,
хотел подключить ci-cd, nginx и развернуть на сервере (сервера нет)

# how start?
1. Создаете файл с переменными окружение ".env" на примере ".env.Example"
2. запускаете команду docker compose up --build
3. на локал хосте 0.0.0.0:8000/ можете тестить апишки, есть так же swagger http://0.0.0.0:8000/swagger/?format=openapi

# ER diagram
https://miro.com/welcomeonboard/MXBJdDhPU3NHRXRtREVudkE2aXByT1ZaSGpWMjRqeGxEQWNtS002RjN4ZHlMbmE2RkczdFRCVE94YXRjT0FiOHwzNDU4NzY0NTc4MDQyNzgxNDIzfDI=?share_link_id=994071826936