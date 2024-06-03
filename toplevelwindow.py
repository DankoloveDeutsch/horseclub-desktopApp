import tkinter
from tkinter import ttk
import tkinter.messagebox
import customtkinter
import datetime

class TopLevelWindow_add_horse(customtkinter.CTkToplevel):
    def __init__(self, app, db):  # Принимаем экземпляр db в качестве аргумента
        super().__init__(app)
        self.db=db
        self.app=app
        self.geometry("400x350")

        self.label_name = customtkinter.CTkLabel(self, text="Имя лошади:",fg_color="transparent")
        self.label_breed = customtkinter.CTkLabel(self, text="Порода:",fg_color="transparent")       
        self.label_birthdate = customtkinter.CTkLabel(self, text="Дата рождения:",fg_color="transparent")
        self.label_gender = customtkinter.CTkLabel(self, text="Пол:",fg_color="transparent")

        self.label_color = customtkinter.CTkLabel(self, text="Масть:",fg_color="transparent")
        self.label_description = customtkinter.CTkLabel(self, text="Описание:",fg_color="transparent")


        self.entry_name = customtkinter.CTkEntry(self)
        self.entry_breed = customtkinter.CTkEntry(self)
        self.entry_birthdate = customtkinter.CTkEntry(self)
        self.entry_color = customtkinter.CTkEntry(self)
        self.entry_description = customtkinter.CTkEntry(self)

        self.optionmenu_gender = customtkinter.CTkOptionMenu(self, values=["женский", "мужской"])

        self.button_add_horse = customtkinter.CTkButton(self, text="Добавить лошадь", command=self.add_horse)
        self.button_close_window = customtkinter.CTkButton(self, text="Отмена", command=self.close_window)

        self.label_name.grid(row=1, column=1, padx=10, pady=10)
        self.label_breed.grid(row=2, column=1, padx=10, pady=10)
        self.label_birthdate.grid(row=3, column=1, padx=10, pady=10)
        self.label_gender.grid(row=4, column=1, padx=10, pady=10)
        self.label_color.grid(row=5, column=1, padx=10, pady=10)
        self.label_description.grid(row=6, column=1, padx=10, pady=10)

        self.entry_name.grid(row=1, column=2, padx=10, pady=10)
        self.entry_breed.grid(row=2, column=2, padx=10, pady=10)
        self.entry_birthdate.grid(row=3, column=2, padx=10, pady=10)
        self.optionmenu_gender.grid(row=4, column=2, padx=10, pady=10)
        self.entry_color.grid(row=5, column=2, padx=10, pady=10)
        self.entry_description.grid(row=6, column=2, padx=10, pady=10)

        self.button_add_horse.grid(row=7, column=1, columnspan=1, pady=10)
        self.button_close_window.grid(row=7, column=2, columnspan=1, pady=10)

    def close_window(self):
        self.destroy()
    def add_horse(self):
        name = self.entry_name.get()
        breed = self.entry_breed.get()
        birthdate = self.entry_birthdate.get()
        gender = self.optionmenu_gender.get()
        color = self.entry_color.get()
        description = self.entry_description.get()
        horses_data = [name,breed,birthdate,gender,color,description, 0,0]

       	self.db.add_horses(horses_data)
        self.destroy()
        self.app.view_data("horses")

class TopLevelWindow_del_horse(customtkinter.CTkToplevel):
    def __init__(self, app, db):  # Принимаем экземпляр db в качестве аргумента
        super().__init__(app)
        self.db=db
        self.app=app
        self.geometry("500x300")
        self.label_number = customtkinter.CTkLabel(self, text="Введите номер лошади, которую хотите удалить:",fg_color="transparent")
        self.entry_number = customtkinter.CTkEntry(self)
        self.button_del_horse = customtkinter.CTkButton(self, text="Удалить лошадь", command=self.del_horse)
        self.button_close_window = customtkinter.CTkButton(self, text="Отмена", command=self.close_window)
        self.button_del_horse.grid(row=6, column=1, columnspan=2, pady=10)
        self.button_close_window.grid(row=6, column=2, columnspan=2, pady=10)
        self.label_number.grid(row=1, column=1, padx=10, pady=10)
        self.entry_number.grid(row=1, column=2, padx=10, pady=10)
    def close_window(self):
        self.destroy()
    def del_horse(self):
        number = self.entry_number.get()
        
        self.db.remove_horses(number)
        self.destroy()
        self.app.view_data("horses")


class TopLevelWindow_add_staff(customtkinter.CTkToplevel):
    def __init__(self, app, db):  # Принимаем экземпляр db в качестве аргумента
        super().__init__(app)
        self.db=db
        self.app=app
        self.geometry("400x550")

        self.label_firstname = customtkinter.CTkLabel(self, text="Фамилия:",fg_color="transparent")
        self.label_lastname = customtkinter.CTkLabel(self, text="Имя:",fg_color="transparent")       
        self.label_middlename = customtkinter.CTkLabel(self, text="Отчество:",fg_color="transparent")
        self.label_gender = customtkinter.CTkLabel(self, text="Пол:",fg_color="transparent")
        self.label_birthdate = customtkinter.CTkLabel(self, text="Дата рождения:",fg_color="transparent")
        self.label_inn = customtkinter.CTkLabel(self, text="ИНН:",fg_color="transparent")
        self.label_passport = customtkinter.CTkLabel(self, text="Пасспорт:",fg_color="transparent")
        self.label_phonenumber = customtkinter.CTkLabel(self, text="Номер телефона:",fg_color="transparent")
        self.label_email = customtkinter.CTkLabel(self, text="Почта:",fg_color="transparent")
        self.label_position = customtkinter.CTkLabel(self, text="Должность:",fg_color="transparent")


        self.entry_firstname = customtkinter.CTkEntry(self)
        self.entry_lastname = customtkinter.CTkEntry(self)
        self.entry_middlename = customtkinter.CTkEntry(self)
        self.optionmenu_gender = customtkinter.CTkOptionMenu(self, values=["женский", "мужской"])
        self.entry_birthdate = customtkinter.CTkEntry(self)
        self.entry_inn = customtkinter.CTkEntry(self)
        self.entry_passport = customtkinter.CTkEntry(self)
        self.entry_phonenumber = customtkinter.CTkEntry(self)
        self.entry_email = customtkinter.CTkEntry(self)
        name_pos = self.db.get_name_positions()
        name_pos = [str(name[0]) for name in name_pos]
        name_pos = [name.strip() for name in (*name_pos,)]
        self.optionmenu_position = customtkinter.CTkOptionMenu(self, values=name_pos)

        self.button_add_staff = customtkinter.CTkButton(self, text="Добавить Сотрудника", command=self.add_staff)
        self.button_close_window = customtkinter.CTkButton(self, text="Отмена", command=self.close_window)

        self.label_firstname.grid(row=1, column=1, padx=10, pady=10)
        self.label_lastname.grid(row=2, column=1, padx=10, pady=10)
        self.label_middlename.grid(row=3, column=1, padx=10, pady=10)
        self.label_gender.grid(row=4, column=1, padx=10, pady=10)
        self.label_birthdate.grid(row=5, column=1, padx=10, pady=10)
        self.label_inn.grid(row=6, column=1, padx=10, pady=10)
        self.label_passport.grid(row=7, column=1, padx=10, pady=10)
        self.label_phonenumber.grid(row=8, column=1, padx=10, pady=10)
        self.label_email.grid(row=9, column=1, padx=10, pady=10)
        self.label_position.grid(row=10, column=1, padx=10, pady=10)

        self.entry_firstname.grid(row=1, column=2, padx=10, pady=10)
        self.entry_lastname.grid(row=2, column=2, padx=10, pady=10)
        self.entry_middlename.grid(row=3, column=2, padx=10, pady=10)
        self.optionmenu_gender.grid(row=4, column=2, padx=10, pady=10)
        self.entry_birthdate.grid(row=5, column=2, padx=10, pady=10)
        self.entry_inn.grid(row=6, column=2, padx=10, pady=10)
        self.entry_passport.grid(row=7, column=2, padx=10, pady=10)
        self.entry_phonenumber.grid(row=8, column=2, padx=10, pady=10)
        self.entry_email.grid(row=9, column=2, padx=10, pady=10)
        self.optionmenu_position.grid(row=10, column=2, padx=10, pady=10)

        self.button_add_staff.grid(row=11, column=1, columnspan=1, pady=10)
        self.button_close_window.grid(row=11, column=2, columnspan=1, pady=10)

    def close_window(self):
        self.destroy()

    def add_staff(self):
        firstname = self.entry_firstname.get()
        lastname = self.entry_lastname.get()
        middlename = self.entry_middlename.get()
        gender = self.optionmenu_gender.get()
        birthdate = self.entry_birthdate.get()
        inn = self.entry_inn.get()
        passport = self.entry_passport.get()
        phonenumber = self.entry_phonenumber.get()
        email=self.entry_email.get()
        positions = self.db.get_positions_by_name(self.optionmenu_position.get())

        positions = [str(pos[0]) for pos in positions]
        positions = [pos.strip() for pos in (*positions,)]
        print(positions)
        positions= positions[0]
        data = [firstname,lastname,middlename,gender,birthdate,inn,passport,phonenumber,email,positions]

       	self.db.add_staff(data)
        self.destroy()
        self.app.view_data("staff")

class TopLevelWindow_del_staff(customtkinter.CTkToplevel):
    def __init__(self, app, db):  # Принимаем экземпляр db в качестве аргумента
        super().__init__(app)
        self.db=db
        self.app=app
        self.geometry("500x300")
        self.label_number = customtkinter.CTkLabel(self, text="Введите id Сотрудника, которого хотите удалить:",fg_color="transparent")
        self.entry_number = customtkinter.CTkEntry(self)
        self.button_del_staff = customtkinter.CTkButton(self, text="Удалить сотрудника", command=self.del_staff)
        self.button_close_window = customtkinter.CTkButton(self, text="Отмена", command=self.close_window)
        self.button_del_staff.grid(row=6, column=1, columnspan=2, pady=10)
        self.button_close_window.grid(row=6, column=2, columnspan=2, pady=10)
        self.label_number.grid(row=1, column=1, padx=10, pady=10)
        self.entry_number.grid(row=1, column=2, padx=10, pady=10)
    def close_window(self):
        self.destroy()
    def del_staff(self):
        number = self.entry_number.get()
        
        self.db.remove_staff(number)
        self.destroy()
        self.app.view_data("staff")

class TopLevelWindow_add_services(customtkinter.CTkToplevel):
    def __init__(self, app, db):  # Принимаем экземпляр db в качестве аргумента
        super().__init__(app)
        self.db = db
        self.app = app
        self.geometry("400x350")

        self.label_name = customtkinter.CTkLabel(self, text="Название услуги:",fg_color="transparent")
        self.label_cost = customtkinter.CTkLabel(self, text="Стоимость:",fg_color="transparent")
        self.label_description = customtkinter.CTkLabel(self, text="Описание:",fg_color="transparent")

        self.entry_name = customtkinter.CTkEntry(self)
        self.entry_cost = customtkinter.CTkEntry(self)
        self.entry_description = customtkinter.CTkEntry(self)

        self.button_add_service = customtkinter.CTkButton(self, text="Добавить услугу", command=self.add_service)
        self.button_close_window = customtkinter.CTkButton(self, text="Отмена", command=self.close_window)

        self.label_name.grid(row=1, column=1, padx=10, pady=10)
        self.label_cost.grid(row=2, column=1, padx=10, pady=10)
        self.label_description.grid(row=3, column=1, padx=10, pady=10)

        self.entry_name.grid(row=1, column=2, padx=10, pady=10)
        self.entry_cost.grid(row=2, column=2, padx=10, pady=10)
        self.entry_description.grid(row=3, column=2, padx=10, pady=10)

        self.button_add_service.grid(row=4, column=1, columnspan=1, pady=10)
        self.button_close_window.grid(row=4, column=2, columnspan=1, pady=10)

    def close_window(self):
        self.destroy()

    def add_service(self):
        name = self.entry_name.get()
        cost = self.entry_cost.get()
        description = self.entry_description.get()

        data = [name, cost, description]

        self.db.add_services(data)
        self.destroy()
        self.app.view_data("services")

class TopLevelWindow_del_services(customtkinter.CTkToplevel):
    def __init__(self, app, db):  # Принимаем экземпляр db в качестве аргумента
        super().__init__(app)
        self.db = db
        self.app = app
        self.geometry("500x300")
        self.label_number = customtkinter.CTkLabel(self, text="Введите id услуги, которую хотите удалить:",fg_color="transparent")
        self.entry_number = customtkinter.CTkEntry(self)
        self.button_del_service = customtkinter.CTkButton(self, text="Удалить услугу", command=self.del_service)
        self.button_close_window = customtkinter.CTkButton(self, text="Отмена", command=self.close_window)
        self.button_del_service.grid(row=6, column=1, columnspan=2, pady=10)
        self.button_close_window.grid(row=6, column=2, columnspan=2, pady=10)
        self.label_number.grid(row=1, column=1, padx=10, pady=10)
        self.entry_number.grid(row=1, column=2, padx=10, pady=10)

    def close_window(self):
        self.destroy()

    def del_service(self):
        number = self.entry_number.get()

        self.db.remove_services(number)
        self.destroy()
        self.app.view_data("services")

class TopLevelWindow_add_orders(customtkinter.CTkToplevel):
    def __init__(self, app, db):  # Принимаем экземпляр db в качестве аргумента
        super().__init__(app)
        self.db = db
        self.app = app
        self.geometry("500x350")

        self.label_date = customtkinter.CTkLabel(self, text="Дата заказа:",fg_color="transparent")
        self.label_service = customtkinter.CTkLabel(self, text="Услуга:",fg_color="transparent")
        self.label_client = customtkinter.CTkLabel(self, text="Клиент:",fg_color="transparent")
        self.label_horses = customtkinter.CTkLabel(self, text="перечислите id лошадей для этой услуги:",fg_color="transparent")

        self.entry_date = customtkinter.CTkEntry(self)
        self.entry_date.insert(0,datetime.date.today())
        self.optionmenu_service = customtkinter.CTkOptionMenu(self, values=[])
        self.optionmenu_client = customtkinter.CTkOptionMenu(self, values=[])
        self.entry_horses = customtkinter.CTkEntry(self)

        self.button_add_order = customtkinter.CTkButton(self, text="Добавить заказ", command=self.add_order)
        self.button_close_window = customtkinter.CTkButton(self, text="Отмена", command=self.close_window)

        self.label_date.grid(row=1, column=1, padx=10, pady=10)
        self.label_service.grid(row=2, column=1, padx=10, pady=10)
        self.label_client.grid(row=3, column=1, padx=10, pady=10)
        self.label_horses.grid(row=4, column=1, padx=10, pady=10)

        self.entry_date.grid(row=1, column=2, padx=10, pady=10)
        self.optionmenu_service.grid(row=2, column=2, padx=10, pady=10)
        self.optionmenu_client.grid(row=3, column=2, padx=10, pady=10)
        self.entry_horses.grid(row=4, column=2, padx=10, pady=10)

        self.button_add_order.grid(row=5, column=1, columnspan=1, pady=10)
        self.button_close_window.grid(row=5, column=2, columnspan=1, pady=10)

        # Получаем список услуг и клиентов из базы данных
        services = db.get_services()
        clients = db.get_clients()

        # Заполняем optionmenu услугами и клиентами
        self.optionmenu_service.configure(values=[service[1] for service in services])
        self.optionmenu_client.configure(values=[client[2] for client in clients])

    def close_window(self):
        self.destroy()

    def add_order(self):
        date = self.entry_date.get()
        service = self.optionmenu_service.get()
        client = self.optionmenu_client.get()
        horses = self.entry_horses.get()

        # Получаем id услуги и клиента из базы данных
        service_id = self.db.get_service_id_by_name(service)
        client_id = self.db.get_client_id_by_name(client)

        # Добавляем заказ в базу данных
        order_id = self.db.add_order([date, service_id, client_id])

        # Разбиваем строку с номерами лошадей на список
        horses_list = [int(x.strip()) for x in horses.split(',')]
        print(horses_list)
        # Добавляем записи в таблицу Orders_Horses
        for horse_id in horses_list:
	        order_horse_data = (order_id, horse_id)
	        print(order_id,horse_id)
	        self.db.add_order_horse(order_horse_data)

        self.destroy()
        self.app.view_data("orders")


class TopLevelWindow_del_orders(customtkinter.CTkToplevel):
    def __init__(self, app, db):  # Принимаем экземпляр db в качестве аргумента
        super().__init__(app)
        self.db = db
        self.app = app
        self.geometry("500x300")
        self.label_number = customtkinter.CTkLabel(self, text="Введите id заказа, которого хотите удалить:",fg_color="transparent")
        self.entry_number = customtkinter.CTkEntry(self)
        self.button_del_order = customtkinter.CTkButton(self, text="Удалить заказ", command=self.del_order)
        self.button_close_window = customtkinter.CTkButton(self, text="Отмена", command=self.close_window)
        self.button_del_order.grid(row=6, column=1, columnspan=2, pady=10)
        self.button_close_window.grid(row=6, column=2, columnspan=2, pady=10)
        self.label_number.grid(row=1, column=1, padx=10, pady=10)
        self.entry_number.grid(row=1, column=2, padx=10, pady=10)

    def close_window(self):
        self.destroy()

    def del_order(self):
        number = self.entry_number.get()

        self.db.remove_orders(number)
        self.destroy()
        self.app.view_data("orders")
