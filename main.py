#импортируем из библиотеки bottle нужные методы
from bottle import route, run, static_file
import os
import sqlite3
#когда вводим в адресную строку имя-домена/hello
#возвращает "Hello World!"
@route('/hello')
def hello():
    return "Hello World!"

@route('/bye')
def bye():
    return "Bye World!"

@route('/')
def root():
    return static_file('root.html', 'static/')
#когда вводим в адресную строку имя-домена/static/название-html-страницы.html
#отрисовывает название-html-страницы.html
@route('/static/<filename>')
def server_static(filename):
    return static_file(filename, 'static/')
@route('/users')
def all_users():
    conn = sqlite3.connect('test1.db')
    c = conn.cursor()
    c.execute("SELECT * FROM users")
    result = c.fetchall()
    conn.close()
    return str(result)

@route('/users/<id>')
def show_user(id):
    conn = sqlite3.connect('test1.db')
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE id={value}".format(value=int(id)))
    result = c.fetchall()
    conn.close()
    return str(result)

#добавляем условие для запуска на сервисе heroku
#если  переменная окружения APP_LOCATION равна 'heroku'
#тогда выставляем адрес 0.0.0.0 
if os.environ.get('APP_LOCATION') == 'heroku':
    run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
else:
    run(host='localhost', port=8080, debug=True)
