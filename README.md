# Запускаем статический сайт с помощью bottle + heroku

**Статический сайт** — [сайт](https://ru.wikipedia.org/wiki/%D0%A1%D0%B0%D0%B9%D1%82), состоящий из статичных html страниц, составляющих единое целое. Содержит в себе (в виде HTML-размеченных) текст, изображения, мультимедиа содержимое (аудио, видео) и HTML-теги.

Наш сайт будет состоять из двух вещей : логики  и представления

Логика - это то как сервер  будет реагировать на наши действий.

Представление - html страницы с текстом, изображением и тд.

### Представление

Заходим на [replit.com](https://replit.com/)

Создаем проект по шаблону html, css, js

<img width="704" alt="Снимок экрана 2022-03-27 в 10 36 20" src="https://user-images.githubusercontent.com/56774342/160271716-d649f757-2d13-4306-ac2b-2e55a2040a8b.png">

Создаем несколько страниц 

<img width="704" alt="Снимок экрана 2022-03-27 в 10 37 23" src="https://user-images.githubusercontent.com/56774342/160271783-bd3b2a5b-608f-4648-a645-6b5248ed9935.png">


Нажимаем старт и запускается прототип нашего сайт. Можно посмотреть как будет выглядеть наше приложение.

Домашнюю страницу принято называть  index.html

### Логика

Мы будем использовать веб-фреймворк bottle . В нем содержится минимум вещей необходимых для написания сайта. [Подробнее](https://github.com/bottlepy/bottle) 

Здесь я буду использовать ide replit , но вы можете использовать любую другую.

Заходим на replit.com

Создаем проект для языка Python

<img width="704" alt="Снимок экрана 2022-03-27 в 10 38 41" src="https://user-images.githubusercontent.com/56774342/160271803-6a6926df-edf2-4935-a049-e7b4bf1a40ea.png">


Устанавливаем библиотеку bottle

<img width="704" alt="Снимок экрана 2022-03-27 в 10 39 03" src="https://user-images.githubusercontent.com/56774342/160271808-4b4009cb-6e2c-4897-89f7-c8ba43134121.png">

Пишем логику

<img width="704" alt="Снимок экрана 2022-03-27 в 10 39 27" src="https://user-images.githubusercontent.com/56774342/160271823-b457dc17-0ec8-4388-b7fc-e603fad7444f.png">


```python
#импортируем из библиотеки bottle нужные методы
from bottle import route, run, static_file

#когда вводим в адресную строку имя-домена/hello
#возвращает "Hello World!"
@route('/hello')
def hello():
    return "Hello World!"

#когда вводим в адресную строку имя-домена/static/название-html-страницы.html
#отрисовывает название-html-страницы.html
@route('/static/<filename>')
def server_static(filename):
    return static_file(filename, 'static/')

#запускаем локальный сервер 
run(host='localhost', port=8080, debug=True)
```

Переносим представление в отдельную папку  static

<img width="704" alt="Снимок экрана 2022-03-27 в 10 39 56" src="https://user-images.githubusercontent.com/56774342/160271837-b1ad065f-3e55-4f89-8024-1738deb058d4.png">

Коммитим и закидываем на гитхаб
Для этого надо создать новый репозиторий 

<img width="693" alt="Снимок экрана 2022-03-27 в 10 41 07" src="https://user-images.githubusercontent.com/56774342/160271870-d8db50ea-89f0-40a1-bbfa-2af44e84b325.png">


Пишем конфигурационные файлы

- добавим библиотеку os

```python
import os
```

- изменим запуск сервера

```python
if os.environ.get('APP_LOCATION') == 'heroku':
	run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
else:
	run(host='localhost', port=8080, debug=True)
```

<img width="710" alt="Снимок экрана 2022-03-27 в 10 46 30" src="https://user-images.githubusercontent.com/56774342/160272030-c708faf1-91b3-4142-8aa6-515f06b8b78b.png">

- добавим файл Procfile

В этом файлы мы явно припишем команду запуска нашего приложения для сервера

<img width="710" alt="Снимок экрана 2022-03-27 в 10 46 57" src="https://user-images.githubusercontent.com/56774342/160272054-1daadfad-eca1-489d-ab99-a2519f3add0f.png">
```python
web: python maib.py
```

- добавим файл requirements.txt

Здесь мы определяем версии используемых библиотек (сторонних)

Узнать версию библиотеки можно в разделе packages слева

<img width="710" alt="Снимок экрана 2022-03-27 в 10 48 00" src="https://user-images.githubusercontent.com/56774342/160272107-017d4d05-f4f0-4655-a744-24f11715db5f.png">

- добавим файл runtime.txt

Здесь указываем версию Python .  Узнать ее можно в терминале справа

<img width="710" alt="Снимок экрана 2022-03-27 в 10 48 52" src="https://user-images.githubusercontent.com/56774342/160272135-ce0a2032-f6dc-41e4-ac8a-c8c26edf9548.png">

Коммитим

<img width="710" alt="Снимок экрана 2022-03-27 в 10 49 10" src="https://user-images.githubusercontent.com/56774342/160272147-de9dd4d4-a2ea-434e-bcfe-047f0eec2dd5.png">


### Деплой на heroku

Заходим на [heroku]( https://www.heroku.com)

Создаем новый проект

<img width="710" alt="Снимок экрана 2022-03-27 в 10 52 50" src="https://user-images.githubusercontent.com/56774342/160272289-1167c806-f5fd-4c12-a861-0d8995f89f9d.png">

<img width="710" alt="Снимок экрана 2022-03-27 в 10 53 32" src="https://user-images.githubusercontent.com/56774342/160272313-2a4837e9-704c-4b0b-9fc0-10b56a0a2926.png">


Привязываем репозиторий с github

Имя репозитория можно посмотреть либо на сайте [github.com](http://github.com) либо в replit

<img width="535" alt="Снимок экрана 2022-03-27 в 10 54 34" src="https://user-images.githubusercontent.com/56774342/160272349-f150fbe1-b8f7-4891-830d-9fd590df8aca.png">

<img width="710" alt="Снимок экрана 2022-03-27 в 10 53 58" src="https://user-images.githubusercontent.com/56774342/160272333-b8a94d49-1c2a-4424-81e0-09cd3294cafe.png">

здесь указываем выбираем github и выбираем наш репозиторий

<img width="1367" alt="Снимок экрана 2022-03-27 в 10 56 34" src="https://user-images.githubusercontent.com/56774342/160272410-c367b2cb-9d4d-4b9d-bced-a9656d04849c.png">

Нажимаем Deploy Branch

<img width="1367" alt="Снимок экрана 2022-03-27 в 10 57 28" src="https://user-images.githubusercontent.com/56774342/160272437-7add4aae-5aff-4e87-954d-2c65312bf20d.png">

Создаем локальную переменную

<img width="716" alt="Снимок экрана 2022-03-27 в 10 58 31" src="https://user-images.githubusercontent.com/56774342/160272461-a6516301-4ec9-4e1e-a5a1-3dea56bca306.png">

выбираем Reveal Config Vars

<img width="1355" alt="Снимок экрана 2022-03-27 в 10 59 37" src="https://user-images.githubusercontent.com/56774342/160272492-312cb752-5aef-48e5-a57d-00046095d8ab.png">

Проверяем worker

(если worker не появился, заходим в настройки и перезагружаем страницу - это типичный баг хероку)

<img width="1311" alt="Снимок экрана 2022-03-27 в 11 00 40" src="https://user-images.githubusercontent.com/56774342/160272534-00ca38b9-fb34-464f-a9f5-051e3ecc5cf5.png">

Открываем проект - и запоминаем url готово

<img width="543" alt="Снимок экрана 2022-03-27 в 11 01 34" src="https://user-images.githubusercontent.com/56774342/160272555-eb8f7949-d8e6-44d8-90a3-f0597b73f6ea.png">


вводим url нашего ресурса

url можно узнать из кода

```python
@route('/hello')
@route('/static/<filename>')
```

<img width="695" alt="Снимок экрана 2022-03-27 в 11 01 56" src="https://user-images.githubusercontent.com/56774342/160272571-49711a36-03a9-4451-a3ac-fab38cb6b16c.png">

<img width="798" alt="Снимок экрана 2022-03-27 в 11 02 25" src="https://user-images.githubusercontent.com/56774342/160272581-7f08fe51-318e-4a9b-997c-1b71316f6e6d.png">

<img width="798" alt="Снимок экрана 2022-03-27 в 11 02 41" src="https://user-images.githubusercontent.com/56774342/160272588-75e0fd42-c727-427d-8773-9e8888e0759a.png">


### Изменения проекта

Если вы захотите дополнить свой проект страницами или как то изменить код

То вам нужно будет зайти в ide , внести необходимые правки или дополнения

Затем закоммитить+запушить ваши изменения

<img width="1219" alt="Снимок экрана 2022-03-27 в 11 03 04" src="https://user-images.githubusercontent.com/56774342/160272602-7f44ee29-6f64-4091-a9c3-3f7b3b14bdf8.png">

И на странице проекта в heroku перезалить ветку (новый проект создавать не надо !!!)

<img width="1344" alt="Снимок экрана 2022-03-27 в 11 03 44" src="https://user-images.githubusercontent.com/56774342/160272618-06d43cc1-df7d-4d9a-85b6-0b643fae3b7b.png">

### Полезные материалы

[Статья которую я адаптировал](https://github.com/chucknado/bottle_heroku_tutorial)
