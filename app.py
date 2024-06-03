import tkinter
from tkinter import ttk
import tkinter.messagebox
import customtkinter
from database import DataBase
from datetime import datetime
from toplevelwindow import *


customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"



class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.pros_button =False
        self.title("Приложение для конного клуба")
        self.geometry(f"{self.width_ret()}x{self.hight_ret()}")

        self.standart_color = '#1F6AA5'
        self.activate_color = 'green'
        # Окно авторизации
        self.login_window()
        self.toplevel_window = None
        self.adminlevel=0
    def width_ret(self):
        return 1500
    def hight_ret(self):
        return 580
    def login_window(self):

        self.login_frame = customtkinter.CTkFrame(self, width = self.width_ret()*0.15,height=self.hight_ret()/2, corner_radius=0)
        self.login_frame.pack(padx=20, pady=20)
        self.pros_frame = self.login_frame

        customtkinter.CTkLabel(self.login_frame, text="Логин:").grid(row=0, column=0, sticky=customtkinter.E)
        customtkinter.CTkLabel(self.login_frame, text="Пароль:").grid(row=1, column=0, sticky=customtkinter.E)

        self.login_entry = customtkinter.CTkEntry(self.login_frame)
        self.password_entry = customtkinter.CTkEntry(self.login_frame, show="*")

        self.login_entry.grid(row=0, column=1)
        self.password_entry.grid(row=1, column=1)

        login_button = customtkinter.CTkButton(self.login_frame, text="Войти", command=self.authenticate_user)
        login_button.grid(row=2, column=1, pady=10)

    def authenticate_user(self):
        entered_login = self.login_entry.get()
        entered_password = self.password_entry.get()

        user = db.get_user_by_login_and_password(entered_login, entered_password)

        if user:
            user_id = user[0]
            client = db.get_client_by_user_id(user_id)
            staff = db.get_staff_by_user_id(user_id)
            if client:
                self.clientid = client[0]
                self.adminlevel = user[3]
                self.show_main()
            elif staff:
                self.staffid = staff[0]
                self.adminlevel = user[3]
                self.show_main()
            elif user[3]==2:
                self.adminlevel = 2
                self.show_main()
            else:
                tkinter.messagebox.showerror("Ошибка", "Ошибка при получении данных пользователя.")

            #tkinter.messagebox.showinfo("Успех", "Авторизация успешна!")
            
        else:
            tkinter.messagebox.showerror("Ошибка", "Неверный логин или пароль. Повторите попытку.")

    def show_main(self):
        # Закрыть окно авторизации
        self.pros_frame.destroy()

        # Отобразить боковое меню навигации
        self.sidebar()
        # Отобразить главное окно (дашборд)

        if (self.adminlevel==0):
            self.profile_user()
        elif(self.adminlevel==1):
            self.profile_user()
        else:
            self.dashboard()

    def sidebar(self):

        self.sidebar_frame = customtkinter.CTkFrame(self, width=self.width_ret()*0.15, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)

        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))

        if (self.adminlevel==0):
            self.sidebar_button_1 = customtkinter.CTkButton(self.sidebar_frame, command=self.profile_user,text ="Профиль")
            self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)

            self.sidebar_button_5 = customtkinter.CTkButton(self.sidebar_frame, command=self.list_orders,text = "Мои заказы")
            self.sidebar_button_5.grid(row=2, column=0, padx=20, pady=10)
            
            self.sidebar_button_3 = customtkinter.CTkButton(self.sidebar_frame, command=self.list_horses,text ="Мои лошади")
            self.sidebar_button_3.grid(row=3, column=0, padx=20, pady=10)

            self.sidebar_button_4 = customtkinter.CTkButton(self.sidebar_frame, command=self.list_services,text ="Услуги в КСК")
            self.sidebar_button_4.grid(row=4, column=0, padx=20, pady=10)
            
        elif(self.adminlevel==1):
            self.sidebar_button_1 = customtkinter.CTkButton(self.sidebar_frame, command=self.profile_user,text ="Профиль")
            self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)

            self.sidebar_button_5 = customtkinter.CTkButton(self.sidebar_frame, command=self.list_orders,text = "Заказы на исполнение")
            self.sidebar_button_5.grid(row=2, column=0, padx=20, pady=10)
            
            self.sidebar_button_3 = customtkinter.CTkButton(self.sidebar_frame, command=self.list_horses,text ="Обслуживаемые лошади")
            self.sidebar_button_3.grid(row=3, column=0, padx=20, pady=10)

        else:
            self.sidebar_button_1 = customtkinter.CTkButton(self.sidebar_frame, command=self.dashboard,text ="Дашбоард")
            self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)

            self.sidebar_button_2 = customtkinter.CTkButton(self.sidebar_frame, command=self.list_staff,text = "Сотрудники")
            self.sidebar_button_2.grid(row=2, column=0, padx=20, pady=10)
            
            self.sidebar_button_3 = customtkinter.CTkButton(self.sidebar_frame, command=self.list_horses,text ="Лошади")
            self.sidebar_button_3.grid(row=3, column=0, padx=20, pady=10)
            
            self.sidebar_button_4 = customtkinter.CTkButton(self.sidebar_frame, command=self.list_services,text ="Услуги")
            self.sidebar_button_4.grid(row=4, column=0, padx=20, pady=10)
            
            self.sidebar_button_5 = customtkinter.CTkButton(self.sidebar_frame, command=self.list_orders,text ="Заказы")
            self.sidebar_button_5.grid(row=5, column=0, padx=20, pady=10)

        

        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=6, column=0, padx=20, pady=(10, 0))

        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark", "System"],command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=7, column=0, padx=20, pady=(10, 10))
        self.scaling_label = customtkinter.CTkLabel(self.sidebar_frame, text="UI Scaling:", anchor="w")
        self.scaling_label.grid(row=8, column=0, padx=20, pady=(10, 0))
        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["80%", "90%", "100%", "110%", "120%"],
                                                               command=self.change_scaling_event)
        self.scaling_optionemenu.grid(row=9, column=0, padx=20, pady=(10, 20))

    def dashboard(self):
        self.pros_frame.destroy()
        if(self.pros_button):
            self.pros_button.configure(state ="enable",fg_color = self.standart_color)
        self.sidebar_button_1.configure(state="disabled", fg_color = self.activate_color)
        self.pros_button = self.sidebar_button_1

        self.dashboard_frame = customtkinter.CTkFrame(self,width=self.width_ret()*0.75, corner_radius=0)
        self.dashboard_frame.grid(row=0,column=1,rowspan=4,padx=(20, 0), pady=(20, 0),sticky="nsew")
        self.pros_frame = self.dashboard_frame

        self.dashboard_text = customtkinter.CTkTextbox(self.dashboard_frame,width=self.width_ret()*0.75)
        self.dashboard_text.insert("0.0", "Здравствуйте\n\n" +"Для вас доступен широкие возможности для редактирования!\nВыберите нужный пункт в боковом меню слева!!\n")
        self.dashboard_text.grid(row=0, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")

    def profile_user(self):
        self.pros_frame.destroy()
        if(self.pros_button):
            self.pros_button.configure(state ="enable",fg_color = self.standart_color)
        self.sidebar_button_1.configure(state="disabled", fg_color = self.activate_color)
        self.pros_button = self.sidebar_button_1

        self.profile_frame = customtkinter.CTkFrame(self,width=self.width_ret()*0.75, corner_radius=0)
        self.profile_frame.grid(row=0,column=1,rowspan=4,padx=(20, 0), pady=(20, 0),sticky="nsew")
        self.pros_frame = self.profile_frame

        data =['Приветсвуем','Уважаемый','1','2','3']
        print(data)
        self.label_name = customtkinter.CTkLabel(self.profile_frame, text="Ваше имя:",fg_color="transparent")
        self.label_email = customtkinter.CTkLabel(self.profile_frame, text="Ваша почта:",fg_color="transparent")
        self.label_phone = customtkinter.CTkLabel(self.profile_frame, text="Ваш телефон:",fg_color="transparent")
        self.label_memberstatus = customtkinter.CTkLabel(self.profile_frame, text="Ваш статус системы лояльности:",fg_color="transparent")

        self.label_name_ot = customtkinter.CTkLabel(self.profile_frame, text=data[1],fg_color="transparent")
        self.label_email_ot = customtkinter.CTkLabel(self.profile_frame, text=data[2],fg_color="transparent")
        self.label_phone_ot = customtkinter.CTkLabel(self.profile_frame, text=data[3],fg_color="transparent")
        self.label_memberstatus_ot = customtkinter.CTkLabel(self.profile_frame, text=data[4],fg_color="transparent")
        

        self.label_name.grid(row=0, column=0, padx=10, pady=10)
        self.label_email.grid(row=1, column=0, padx=10, pady=10)
        self.label_phone.grid(row=2, column=0, padx=10, pady=10)
        self.label_memberstatus.grid(row=3, column=0, padx=10, pady=10)

        self.label_name_ot.grid(row=0, column=1, padx=10, pady=10)
        self.label_email_ot.grid(row=1, column=1, padx=10, pady=10)
        self.label_phone_ot.grid(row=2, column=1, padx=10, pady=10)
        self.label_memberstatus_ot.grid(row=3, column=1, padx=10, pady=10)

    def list_staff(self):

        self.pros_frame.destroy()
        self.pros_button.configure(state ="enable", fg_color = self.standart_color)
        self.sidebar_button_2.configure(state="disabled", fg_color = self.activate_color)
        self.pros_button = self.sidebar_button_2

        self.staff_frame = customtkinter.CTkFrame(self,width=self.width_ret()*0.75, corner_radius=0)
        self.staff_frame.grid(row=0,column=1,rowspan=4,padx=(20, 0), pady=(20, 0),sticky="nsew")
        self.pros_frame = self.staff_frame
      
        # Список лошадей, таблица
        self.tree = ttk.Treeview(self.staff_frame,columns=("Number","firstname", "lastname", "middlename", "gender", "birthdate", "inn", "passport","phonenumber","email","position"), show="headings")
        self.tree.heading("Number", text="Номер",anchor=tkinter.CENTER)
        self.tree.heading("firstname", text="Фамилия",anchor=tkinter.CENTER)
        self.tree.heading("lastname", text="Имя",anchor=tkinter.CENTER)
        self.tree.heading("middlename", text="Отчество",anchor=tkinter.CENTER)
        self.tree.heading("gender", text="Пол",anchor=tkinter.CENTER)
        self.tree.heading("birthdate", text="Дата рождения",anchor=tkinter.CENTER)
        self.tree.heading("inn", text="ИНН",anchor=tkinter.CENTER)
        self.tree.heading("passport", text="Паспорт",anchor=tkinter.CENTER)
        self.tree.heading("phonenumber", text="Номер телефона",anchor=tkinter.CENTER)
        self.tree.heading("email", text="Почта",anchor=tkinter.CENTER)
        self.tree.heading("position", text="Должность",anchor=tkinter.CENTER)

        self.tree.column("Number", width=20, stretch=tkinter.NO)
        self.tree.column("firstname", width=100, stretch=tkinter.NO)
        self.tree.column("lastname", width=100, stretch=tkinter.NO)
        self.tree.column("middlename", width=50, stretch=tkinter.NO)
        self.tree.column("gender", width=75, stretch=tkinter.NO)
        self.tree.column("birthdate", width=100, stretch=tkinter.NO)
        self.tree.column("inn", width=100, stretch=tkinter.NO)
        self.tree.column("passport", width=100, stretch=tkinter.NO)
        self.tree.column("phonenumber", width=100, stretch=tkinter.NO)
        self.tree.column("email", width=100, stretch=tkinter.NO)
        self.tree.column("position", width=100, stretch=tkinter.NO)

        self.tree.grid(row=0, column=0, rowspan=6, padx=10, pady=10)
        self.view_data("staff")

        #Управляющие кнопки
        if(self.adminlevel==0):
            pass
        else:
            self.button_add_staff = customtkinter.CTkButton(self.staff_frame, text="Добавить сотрудника", command=self.open_toplevel_staff_add)
            self.button_del_staff = customtkinter.CTkButton(self.staff_frame, text="Удалить сотрудника", command=self.open_toplevel_staff_del)

            # размещение интерфейса
            self.button_add_staff.grid(row=0, column=1, pady=10)
            self.button_del_staff.grid(row=1, column=1, pady=10)

    def open_toplevel_staff_add(self):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = TopLevelWindow_add_staff(self,db)  # create window if its None or destroyed
            self.toplevel_window.focus()
        else:
            self.toplevel_window.focus()

    def open_toplevel_staff_del(self):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = TopLevelWindow_del_staff(self,db)  # create window if its None or destroyed
            self.toplevel_window.focus()
        else:
            self.toplevel_window.focus()

    def list_services(self):

        self.pros_frame.destroy()
        self.pros_button.configure(state ="enable", fg_color = self.standart_color)
        self.sidebar_button_4.configure(state="disabled", fg_color = self.activate_color)
        self.pros_button = self.sidebar_button_4

        self.services_frame = customtkinter.CTkFrame(self,width=self.width_ret()*0.75, corner_radius=0)
        self.services_frame.grid(row=0,column=1,rowspan=4,padx=(20, 0), pady=(20, 0),sticky="nsew")
        self.pros_frame = self.services_frame
      
        # Список лошадей, таблица
        self.tree = ttk.Treeview(self.services_frame,columns=("Number","Name", "cost", "description"), show="headings")
        self.tree.heading("Number", text="Номер",anchor=tkinter.CENTER)
        self.tree.heading("Name", text="Имя",anchor=tkinter.CENTER)
        self.tree.heading("cost", text="Цена",anchor=tkinter.CENTER)
        self.tree.heading("description", text="Описание",anchor=tkinter.CENTER)

        self.tree.column("Number", width=20, stretch=tkinter.NO)
        self.tree.column("Name", width=200, stretch=tkinter.NO)
        self.tree.column("cost", width=100, stretch=tkinter.NO)
        self.tree.column("description", width=500, stretch=tkinter.NO)

        self.tree.grid(row=0, column=0, rowspan=6, padx=10, pady=10)
        self.view_data("services")
        #Управляющие кнопки
        if(self.adminlevel==0 or self.adminlevel==1):
            pass
        else:
            self.button_add_services = customtkinter.CTkButton(self.services_frame, text="Добавить услугу", command=self.open_toplevel_services_add)
            self.button_del_services = customtkinter.CTkButton(self.services_frame, text="Удалить услугу", command=self.open_toplevel_services_del  )

            # размещение интерфейса
            self.button_add_services.grid(row=0, column=1, pady=10)
            self.button_del_services.grid(row=1, column=1, pady=10)
    def open_toplevel_services_add(self):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = TopLevelWindow_add_services(self,db)  # create window if its None or destroyed
            self.toplevel_window.focus()
        else:
            self.toplevel_window.focus()

    def open_toplevel_services_del(self):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = TopLevelWindow_del_services(self,db)  # create window if its None or destroyed
            self.toplevel_window.focus()
        else:
            self.toplevel_window.focus()
    def list_orders(self):

        self.pros_frame.destroy()
        self.pros_button.configure(state ="enable", fg_color = self.standart_color)
        self.sidebar_button_5.configure(state="disabled", fg_color = self.activate_color)
        self.pros_button = self.sidebar_button_5

        self.orders_frame = customtkinter.CTkFrame(self,width=self.width_ret()*0.75, corner_radius=0)
        self.orders_frame.grid(row=0,column=1,rowspan=4,padx=(20, 0), pady=(20, 0),sticky="nsew")
        self.pros_frame = self.orders_frame
      
        # Список лошадей, таблица
        self.tree = ttk.Treeview(self.orders_frame,columns=("Number","Date", "services", "client"), show="headings")
        self.tree.heading("Number", text="Номер",anchor=tkinter.CENTER)
        self.tree.heading("Date", text="Дата",anchor=tkinter.CENTER)
        self.tree.heading("services", text="Услуга",anchor=tkinter.CENTER)
        self.tree.heading("client", text="Клиент",anchor=tkinter.CENTER)

        self.tree.column("Number", width=20, stretch=tkinter.NO)
        self.tree.column("Date", width=200, stretch=tkinter.NO)
        self.tree.column("services", width=200, stretch=tkinter.NO)
        self.tree.column("client", width=200, stretch=tkinter.NO)
       
        self.tree.grid(row=0, column=0, rowspan=6, padx=10, pady=10)
        
        #Управляющие кнопки
        if(self.adminlevel==0):
            self.button_add_orders = customtkinter.CTkButton(self.orders_frame, text="Заказать услугу", command=self.open_toplevel_orders_add)
            self.button_add_orders.grid(row=0, column=1, pady=10)
            self.view_data("orders_client")
        elif(self.adminlevel==1):
            pass
            self.view_data("orders_staff")
        else:
            self.button_add_orders = customtkinter.CTkButton(self.orders_frame, text="Добавить заказ", command=self.open_toplevel_orders_add)
            self.button_del_orders = customtkinter.CTkButton(self.orders_frame, text="Удалить заказ", command=self.open_toplevel_orders_del)

            # размещение интерфейса
            self.button_add_orders.grid(row=0, column=1, pady=10)
            self.button_del_orders.grid(row=1, column=1, pady=10)
            self.view_data("orders")

    def open_toplevel_orders_add(self):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = TopLevelWindow_add_orders(self,db)  # create window if its None or destroyed
            self.toplevel_window.focus()
        else:
            self.toplevel_window.focus()

    def open_toplevel_orders_del(self):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = TopLevelWindow_del_orders(self,db)  # create window if its None or destroyed
            self.toplevel_window.focus()
        else:
            self.toplevel_window.focus()
    def list_horses(self):

        self.pros_frame.destroy()
        self.pros_button.configure(state ="enable", fg_color = self.standart_color)
        self.sidebar_button_3.configure(state="disabled", fg_color = self.activate_color)
        self.pros_button = self.sidebar_button_3

        self.horses_frame = customtkinter.CTkFrame(self,width=self.width_ret()*0.75, corner_radius=0)
        self.horses_frame.grid(row=0,column=1,rowspan=4,padx=(20, 0), pady=(20, 0),sticky="nsew")
        self.pros_frame = self.horses_frame
      
        # Список лошадей, таблица
        self.tree = ttk.Treeview(self.horses_frame,columns=("Number","Name", "Breed", "birthdate", "gender", "color", "description", "active_services_cost","services_cost_mounth"), show="headings")
        self.tree.heading("Number", text="Номер",anchor=tkinter.CENTER)
        self.tree.heading("Name", text="Имя",anchor=tkinter.CENTER)
        self.tree.heading("Breed", text="Порода",anchor=tkinter.CENTER)
        self.tree.heading("birthdate", text="Дата рождения",anchor=tkinter.CENTER)
        self.tree.heading("gender", text="Пол",anchor=tkinter.CENTER)
        self.tree.heading("color", text="Масть",anchor=tkinter.CENTER)
        self.tree.heading("description", text="Описание",anchor=tkinter.CENTER)
        self.tree.heading("active_services_cost", text="Общая стоимость услуг",anchor=tkinter.CENTER)
        self.tree.heading("services_cost_mounth", text="Стоимость услуг за последний месяц",anchor=tkinter.CENTER)

        self.tree.column("Number", width=20, stretch=tkinter.NO)
        self.tree.column("Name", width=100, stretch=tkinter.NO)
        self.tree.column("Breed", width=100, stretch=tkinter.NO)
        self.tree.column("birthdate", width=50, stretch=tkinter.NO)
        self.tree.column("gender", width=75, stretch=tkinter.NO)
        self.tree.column("color", width=90, stretch=tkinter.NO)
        self.tree.column("description", width=200, stretch=tkinter.NO)
        self.tree.column("active_services_cost", width=80, stretch=tkinter.NO)
        self.tree.column("services_cost_mounth", width=200, stretch=tkinter.NO)
        self.tree.grid(row=0, column=0, rowspan=6, padx=10, pady=10)
        
        #Управляющие кнопки
        if(self.adminlevel==0):
            self.view_data("horse_client")
        elif(self.adminlevel==1):
            self.view_data("horse_staff")
        else:
            self.button_add_horse = customtkinter.CTkButton(self.horses_frame, text="Добавить лошадь", command=self.open_toplevel_horse_add)
            self.button_del_horse = customtkinter.CTkButton(self.horses_frame, text="Удалить лошадь", command=self.open_toplevel_horse_del)

            # размещение интерфейса
            self.button_add_horse.grid(row=0, column=1, pady=10)
            self.button_del_horse.grid(row=1, column=1, pady=10)
            self.view_data("horses")
        

    def open_toplevel_horse_add(self):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = TopLevelWindow_add_horse(self,db)  # create window if its None or destroyed
            self.toplevel_window.focus()
        else:
            self.toplevel_window.focus()
    def open_toplevel_horse_del(self):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = TopLevelWindow_del_horse(self,db)  # create window if its None or destroyed
            self.toplevel_window.focus()
        else:
            self.toplevel_window.focus()

    def view_data(self, data):
        if data=="horses":
            from_db = db.get_horses()
        elif data=="staff":
            from_db = db.get_staff()
        elif data=="services":
            from_db=db.get_services()
        elif data=="orders":
            from_db=db.get_orders()
        elif data=="orders_client":
            from_db=db.get_orders_by_clientid(self.clientid)
        elif data=="orders_staff":
            from_db=db.get_orders_by_staffid(self.staffid)
        elif data=="horse_client":
            from_db=db.get_horses_by_clientid(self.clientid)
        elif data=="horse_staff":
            from_db=db.get_horses_by_staffid(self.staffid)

        for row in self.tree.get_children():
                self.tree.delete(row)

            # Добавляем данные о лошадях в Treeview
        for data_db in from_db:
            self.tree.insert("", tkinter.END, values=data_db)



    def clear_entries(self):
        self.entry_name.delete(0, tkinter.END)
        self.entry_breed.delete(0, tkinter.END)
        self.entry_age.delete(0, tkinter.END)
        self.entry_health_status.delete(0, tkinter.END)
        self.entry_availability.delete(0,tkinter.END)

    def open_input_dialog_event(self):
        dialog = customtkinter.CTkInputDialog(text="Type in a number:", title="CTkInputDialog")
        print("CTkInputDialog:", dialog.get_input())

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

    def sidebar_button_event(self):
        print("sidebar_button click")
    
    

if __name__ == "__main__":
    db = DataBase()
    db.flag = True
    app = App()
    app.mainloop()