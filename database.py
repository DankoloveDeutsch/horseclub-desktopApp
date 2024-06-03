from config import host, user, db_password, dbname
import psycopg2

class DataBase():
    def __init__(self):
        self.flag = False
        try:
            self.connection = psycopg2.connect(
                host = host,
                user = user,
                password = db_password,
                dbname = dbname
            )
            
        except Exception as _ez:
            print("[INFO] Error while working with PostgreSQL")
        finally:
            if self.connection and self.flag:
                self.connection.close()
                self.cursor.close()
                print("[INFO] PostgreSQL connection close")
    def get_horses(self):
        try:
            self.cursor = self.connection.cursor()
            sql_query = "SELECT * FROM horses"
            self.cursor.execute(sql_query)
            horses = self.cursor.fetchall()
            print('[INFO] База данных вернула список лошадей')
            return horses
        except psycopg2.Error as e:
            print("[ERROR] Ошибка при получении списка лошадей", e)
    def get_horses_by_clientid(self, clientid):
        try:
            self.cursor = self.connection.cursor()
            sql_query = """
                SELECT h.horseid, h.name, h.breed, h.birthdate, h.gender, h.color, h.description, h.active_services_cost, h.services_cost_month
                FROM Horses h
                JOIN Client_Horses ch ON h.horseid = ch.horseid
                WHERE ch.ownerid = %s
            """
            self.cursor.execute(sql_query, (clientid,))
            horses = self.cursor.fetchall()
            print('[INFO] База данных вернула список лошадей клиента')
            return horses
        except psycopg2.Error as e:
            print("[ERROR] Ошибка при получении списка лошадей клиента", e)

    def get_horses_by_staffid(self, staffid):
        try:
            self.cursor = self.connection.cursor()
            sql_query = """
                SELECT h.horseid, h.name, h.breed, h.birthdate, h.gender, h.color, h.description, h.active_services_cost, h.services_cost_month
                FROM Horses h
                JOIN Staff_Horses sh ON h.horseid = sh.horseid
                WHERE sh.staffid = %s
            """
            self.cursor.execute(sql_query, (staffid,))
            horses = self.cursor.fetchall()
            print('[INFO] База данных вернула список лошадей сотрудника')
            return horses
        except psycopg2.Error as e:
            print("[ERROR] Ошибка при получении списка лошадей сотрудника", e)


    def add_horses(self, horses):
        print('[INFO] Подготовка к загрузке в бд!')
        try:
            self.cursor = self.connection.cursor()
            sql_query = f"""
                INSERT INTO Horses (name, breed, birthdate, gender, color, description, active_services_cost,services_cost_month)
                VALUES (%s, %s, %s, %s, %s, %s, %s,%s)
            """
            self.cursor.execute(sql_query, horses)
            self.connection.commit()
            print("[INFO] База данных добавила новых лошадей")
        except psycopg2.Error as e:
            print("[ERROR] Ошибка при добавлении новых лошадей", e)

    def remove_horses(self, horseid):
        print('[INFO] Подготовка к удалению из бд!')
        try:
            self.cursor = self.connection.cursor()
            sql_query = "DELETE FROM horses WHERE horseid = %s"  # только строка запроса
            self.cursor.execute(sql_query, (horseid,))  # значение horseid передается отдельно
            self.connection.commit()
            print('[INFO] Лошадь удалена')
        except psycopg2.Error as e:
            print("[ERROR] Ошибка при удалении", e)


    def get_horses_by_client_id(self, client_id):
        try:
            self.cursor = self.connection.cursor()
            sql_query = """
                SELECT Horses.horseid, Horses.name, Horses.breed, Horses.birthdate,
                       Horses.gender, Horses.color, Horses.description, Horses.active_services_cost
                FROM Horses
                JOIN Client_Horses ON Horses.horseid = Client_Horses.horseid
                WHERE Client_Horses.ownerid = %s
            """
            self.cursor.execute(sql_query, (client_id,))
            horses = self.cursor.fetchall()
            print('[INFO] База данных вернула список лошадей для клиента с ID', client_id)
            return horses
        except psycopg2.Error as e:
            print("[ERROR] Ошибка при получении списка лошадей для клиента с ID", client_id, e)

    def get_clients(self):
        try:
            self.cursor = self.connection.cursor()
            sql_query = "SELECT * FROM client"
            self.cursor.execute(sql_query)
            data = self.cursor.fetchall()
            print('[INFO] База данных вернула список клиентов')
            return data
        except psycopg2.Error as e:
            print("[ERROR] Ошибка при получении списка клиентов", e)

    def get_staff(self):
        try:
            self.cursor = self.connection.cursor()
            sql_query = "SELECT staff.staffid, staff.firstname,staff.lastname,staff.middlename,staff.gender,staff.birthdate,staff.inn,staff.passport,staff.phonenumber,staff.email,staff.position FROM staff"
            self.cursor.execute(sql_query)
            data = self.cursor.fetchall()
            print('[INFO] База данных вернула список сотрудников')
            return data
        except psycopg2.Error as e:
            print("[ERROR] Ошибка при получении списка сотрудников", e)

    def get_services(self):
        try:
            self.cursor = self.connection.cursor()
            sql_query = "SELECT * FROM services"
            self.cursor.execute(sql_query)
            data = self.cursor.fetchall()
            print('[INFO] База данных вернула список услуг')
            return data
        except psycopg2.Error as e:
            print("[ERROR] Ошибка при получении списка услуг", e)
    def get_orders(self):
        try:
            self.cursor = self.connection.cursor()
            sql_query = """
            SELECT o.orderid,o.orderdate,s.servicename ,c.lastname FROM orders AS o
            JOIN client c ON o.clientid=c.clientid
            JOIN services s ON o.serviceid=s.serviceid
            """
            self.cursor.execute(sql_query)
            data = self.cursor.fetchall()
            print('[INFO] База данных вернула список заказов')
            return data
        except psycopg2.Error as e:
            print("[ERROR] Ошибка при получении списка заказов", e)

    def get_name_positions(self):
        try:
            self.cursor = self.connection.cursor()
            sql_query = "SELECT nameposition FROM positions"

            self.cursor.execute(sql_query)
            staff = self.cursor.fetchall()
            print('[INFO] База данных вернула названия должносетй')

            return staff
        except psycopg2.Error as e:
            print("[ERROR] Ошибка при получении названий должностей", e)

    def get_positions_by_name(self,name):
        try:
            self.cursor = self.connection.cursor()
            sql_query = "SELECT id FROM positions WHERE nameposition = %s"
            self.cursor.execute(sql_query,(name,))
            pos = self.cursor.fetchall()
            print('[INFO] База данных вернула id должности ')
            return pos
        except psycopg2.Error as e:
            print("[ERROR] Ошибка при получении id должности", e)

    def add_staff(self, staff):
        print('[INFO] Подготовка к загрузке в бд!')
        try:
            self.cursor = self.connection.cursor()
            sql_query = f"""
                INSERT INTO Staff (firstname,lastname,middlename,gender,birthdate,inn,passport,phonenumber,email,position)
                VALUES (%s, %s, %s, %s, %s, %s, %s,%s, %s,%s)
            """
            self.cursor.execute(sql_query, staff)
            self.connection.commit()
            print("[INFO] База данных добавила нового сотрудника")
        except psycopg2.Error as e:
            print("[ERROR] Ошибка при добавлении нового сотрудника", e)
    def remove_staff(self, staff):
        print('[INFO] Подготовка к удалению из бд!')
        try:
            self.cursor = self.connection.cursor()
            sql_query = "DELETE FROM Staff WHERE staffid = %s"  # только строка запроса
            self.cursor.execute(sql_query, (staff,))  # значение horseid передается отдельно
            self.connection.commit()
            print('[INFO] Сотрудник удален')
        except psycopg2.Error as e:
            print("[ERROR] Ошибка при удалении", e)
    def add_services(self, services):
        print('[INFO] Подготовка к загрузке в бд!')
        try:
            self.cursor = self.connection.cursor()
            sql_query = f"""
                INSERT INTO Services (servicename, cost, description)
                VALUES (%s, %s, %s)
            """
            self.cursor.execute(sql_query, services)
            self.connection.commit()
            print("[INFO] База данных добавила новую услугу")
        except psycopg2.Error as e:
            print("[ERROR] Ошибка при добавлении новой услуги", e)
    def remove_services(self, serviceid):
        print('[INFO] Подготовка к удалению из бд!')
        try:
            self.cursor = self.connection.cursor()
            sql_query = "DELETE FROM services WHERE serviceid = %s"  # только строка запроса
            self.cursor.execute(sql_query, (serviceid,))  # значение horseid передается отдельно
            self.connection.commit()
            print('[INFO] Услуга удалена')
        except psycopg2.Error as e:
            print("[ERROR] Ошибка при удалении", e)
    def get_service_id_by_name(self, name):
        """Возвращает id услуги по ее названию"""
        try:
            self.cursor = self.connection.cursor()
            sql_query = "SELECT serviceid FROM services WHERE servicename = %s"
            self.cursor.execute(sql_query, (name,))
            result = self.cursor.fetchone()
            if result:
                return result[0]
            else:
                return None
        except psycopg2.Error as e:
            print("[ERROR] Ошибка при получении id услуги по ее названию", e)

    def get_client_id_by_name(self, name):
        """Возвращает id клиента по его имени"""
        try:
            self.cursor = self.connection.cursor()
            sql_query = "SELECT clientid FROM client WHERE lastname = %s"
            self.cursor.execute(sql_query, (name,))
            result = self.cursor.fetchone()
            if result:
                return result[0]
            else:
                return None
        except psycopg2.Error as e:
            print("[ERROR] Ошибка при получении id клиента по его имени", e)

    def add_order(self, order):
        """Добавляет заказ в таблицу Orders"""
        try:
            self.cursor = self.connection.cursor()
            sql_query = "INSERT INTO orders (orderdate, serviceid, clientid) VALUES (%s, %s, %s) RETURNING orderid"
            self.cursor.execute(sql_query, order)
            order_id = self.cursor.fetchone()[0]
            self.connection.commit()
            print("[INFO] База данных добавила новый заказ")
            return order_id
        except psycopg2.Error as e:
            print("[ERROR] Ошибка при добавлении нового заказа", e)

    def add_order_horse(self, order_horse):
        """Добавляет запись в таблицу Orders_Horses"""
        try:
            self.cursor = self.connection.cursor()
            sql_query = "INSERT INTO Orders_Horses (orderid, horseid) VALUES (%s, %s)"
            self.cursor.execute(sql_query, order_horse)
            self.connection.commit()
            print("[INFO] База данных добавила новую запись в таблицу Orders_Horses")
        except psycopg2.Error as e:
            print("[ERROR] Ошибка при добавлении новой записи в таблицу Orders_Horses", e)

    def remove_orders(self, orderid):
        """Удаляет заказ из таблицы Orders и все связанные с ним записи из таблицы Orders_Horses"""
        try:
            self.cursor = self.connection.cursor()

            # удаляем записи из таблицы Orders_Horses
            sql_query = "DELETE FROM Orders_Horses WHERE orderid = %s"
            self.cursor.execute(sql_query, (orderid,))

            # удаляем заказ из таблицы Orders
            sql_query = "DELETE FROM Orders WHERE orderid = %s"
            self.cursor.execute(sql_query, (orderid,))

            self.connection.commit()
            print("[INFO] База данных удалила заказ и все связанные с ним записи")
        except psycopg2.Error as e:
            print("[ERROR] Ошибка при удалении заказа и всех связанных с ним записей", e)
    def get_orders_by_clientid(self, clientid):
        try:
            self.cursor = self.connection.cursor()
            sql_query = """
                SELECT o.orderid, o.orderdate, s.servicename, s.cost
                FROM Orders o
                JOIN Services s ON o.serviceid = s.serviceid
                WHERE o.clientid = %s
            """
            self.cursor.execute(sql_query, (clientid,))
            orders = self.cursor.fetchall()
            print('[INFO] База данных вернула список заказов клиента')
            return orders
        except psycopg2.Error as e:
            print("[ERROR] Ошибка при получении списка заказов клиента", e)
    def get_orders_by_staffid(self, staffid):
        try:
            self.cursor = self.connection.cursor()
            sql_query = """
                SELECT o.orderid, o.orderdate, s.servicename, s.cost
                FROM Orders o
                JOIN Services s ON o.serviceid = s.serviceid
                JOIN Orders_Staff os ON o.orderid = os.orderid
                WHERE os.staffid = %s
            """
            self.cursor.execute(sql_query, (staffid,))
            orders = self.cursor.fetchall()
            print('[INFO] База данных вернула список заказов сотрудника')
            return orders
        except psycopg2.Error as e:
            print("[ERROR] Ошибка при получении списка заказов сотрудника", e)

    def get_user_by_login_and_password(self, login, password):
        try:
            self.cursor = self.connection.cursor()
            sql_query = "SELECT * FROM users WHERE login = %s AND password = %s"
            self.cursor.execute(sql_query, (login, password))
            user = self.cursor.fetchone()
            return user
        except psycopg2.Error as e:
            print("[ERROR] Ошибка при получении пользователя по логину и паролю", e)
            return None

    def get_client_by_user_id(self, user_id):
        try:
            self.cursor = self.connection.cursor()
            sql_query = "SELECT * FROM Client WHERE userid = %s"
            self.cursor.execute(sql_query, (user_id,))
            client = self.cursor.fetchone()
            return client
        except psycopg2.Error as e:
            print("[ERROR] Ошибка при получении клиента по user_id", e)
            return None

    def get_staff_by_user_id(self, user_id):
        try:
            self.cursor = self.connection.cursor()
            sql_query = "SELECT * FROM Staff WHERE userid = %s"
            self.cursor.execute(sql_query, (user_id,))
            staff = self.cursor.fetchone()
            return staff
        except psycopg2.Error as e:
            print("[ERROR] Ошибка при получении сотрудника по user_id", e)
            return None