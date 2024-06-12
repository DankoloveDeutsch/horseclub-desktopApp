# horseclub-desktopApp
Десктопное приложение для конного клуба(Курсовой проект в рамках курса "Базы данных")


## Установка

1. Клонируйте репозиторий
'''git clone https://github.com/DankoloveDeutsch/horseclub-desktopApp.git'''

2. Перейдите в директорию horseclub-desktopApp
'''cd horseclub-desktopApp'''

3. Создайте виртуальное окружение
'''python 3 -m venv venv'''

4. Активируйте виртуальное окружение
'''Scripts\activate.bat'''

5. Установите необходимые библиотеки (tkinter, customtkinter, psycopg2)
'''pip install customtkinter psycopg2'''

6. Создаете базу данных (в работе использовалась postgreSQL). Схема представлена в файле ERD-db.pgerd

7. Создайте файл config.py и внесите следующие данные.
'''
host = "ip адрес вашего сервера с базой данных"
user = "Имя пользователя для обращения к базе данных"
db_password = "Пароль для доступа к базе данных"
dbname = "Имя базы данных"
''' 
