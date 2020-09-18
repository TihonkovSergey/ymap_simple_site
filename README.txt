Зависимости: FLASK и python >3.7
-- Запустить init_database.py
-- В файле templates/index.html на 6 строчке вписать
 	свой ключ для "JavaScript API и HTTP Геокодер" от Yandex Map
-- Далее в директории проекта:
	win:
		set FLASK_APP=app
		flask run
	
	unix: 
		export FLASK_APP=app
		flask run
