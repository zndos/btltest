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