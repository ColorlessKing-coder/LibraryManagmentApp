import sqlite3




class UserDatabase:
    def __init__(self) -> None:
        self.database_name = "Database/Database.db"

    #stuff---------------------------------------------------------------------------------------------------------------------
    def create_stuff_table(self)->None:
        with sqlite3.connect(self.database_name) as connection:
            cursor = connection.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS stuff (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT NOT NULL,
                    surname TEXT NOT NULL,
                    password TEXT NOT NULL,
                    email TEXT NOT NULL,
                    date TEXT NOT NULL,
                    role TEXT NOT NULL
                )
            """)
            connection.commit()

    def add_stuff_to_table(self,username:str,surname:str,password:str,email:str,date,role:str)->None:
        with sqlite3.connect(self.database_name) as connection:
            cursor = connection.cursor()
            cursor.execute("INSERT INTO stuff (username,surname,password,email,date,role) VALUES (?, ?, ?, ?, ?, ?)",(username, surname, password, email, date, role))

            connection.commit()

    def delete_users_with_id_for_stuff(self,user_id:int)->None:
        with sqlite3.connect(self.database_name) as connection:
            cursor = connection.cursor()
            cursor.execute(f"DELETE FROM stuff WHERE id = ? ",(user_id,))
            connection.commit()


    def list_users_for_stuff(self)->list:
        with sqlite3.connect(self.database_name) as connection:
            cursor = connection.cursor()
            cursor.execute(f"SELECT * FROM stuff ")
            rows = cursor.fetchall()
            return rows
        
    def update_stuff_table_with_id(self, user_id:int, username:str, surname:str, password:str, email:str, date:str, role:str) -> None:
        with sqlite3.connect(self.database_name) as connection:
            cursor = connection.cursor()
            cursor.execute("""
                UPDATE stuff
                SET username = ?, surname = ?, password = ?, email = ?, date = ?, role = ?
                WHERE id = ?
            """, (username, surname, password, email, date, role, user_id))
            connection.commit()


    
    
    #-Member----------------------------------------------------------------------------------------------
    def create_member_table(self)->None:
        with sqlite3.connect(self.database_name) as connection:
            cursor = connection.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS member (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT NOT NULL,
                    surname TEXT NOT NULL,
                    password TEXT NOT NULL,
                    email TEXT NOT NULL,
                    date TEXT NOT NULL,
                    role TEXT NOT NULL
                )
            """)
            connection.commit()

    def add_member_to_table(self,username:str,surname:str,password:str,email:str,date,role:str)->None:
        with sqlite3.connect(self.database_name) as connection:
            cursor = connection.cursor()
            cursor.execute("INSERT INTO member (username,surname,password,email,date,role) VALUES (?, ?, ?, ?, ?, ?)",(username,surname,password,email,date,role))
            connection.commit()

    def delete_users_with_id_for_member(self,user_id:int)->None:
        with sqlite3.connect(self.database_name) as connection:
            cursor = connection.cursor()
            cursor.execute(f"DELETE FROM member WHERE id = ? ",(user_id,))
            connection.commit()

    def update_member_table_with_id(self, user_id:int, username:str, surname:str, password:str, email:str, date:str, role:str) -> None:
        with sqlite3.connect(self.database_name) as connection:
            cursor = connection.cursor()
            cursor.execute("""
                UPDATE member
                SET username = ?, surname = ?, password = ?, email = ?, date = ?, role = ?
                WHERE id = ?
            """, (username, surname, password, email, date, role, user_id))
            connection.commit()

    def list_users_for_member(self)->list:
        with sqlite3.connect(self.database_name) as connection:
            cursor = connection.cursor()
            cursor.execute(f"SELECT * FROM member ")
            rows = cursor.fetchall()
            return rows


    

    #admin----------------------------------------------------------------------------------------------------------------------------
    def create_admin_table(self) -> None:
        with sqlite3.connect(self.database_name) as connection:
            cursor = connection.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS admin (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT NOT NULL,
                    surname TEXT NOT NULL,
                    password TEXT NOT NULL,
                    email TEXT NOT NULL,
                    date TEXT NOT NULL,
                    role TEXT NOT NULL
                )
            """)
            connection.commit()

    def add_admin_to_table(self, username:str, surname:str, password:str, email:str, date, role:str) -> None:
        with sqlite3.connect(self.database_name) as connection:
            cursor = connection.cursor()
            # 👇 BURADA DİKKAT: VALUES içine parametreler tuple olmalı
            cursor.execute(
                "INSERT INTO admin (username, surname, password, email, date, role) VALUES (?, ?, ?, ?, ?, ?)",
                (username, surname, password, email, date, role)
            )
      
            connection.commit()

    

    def delete_users_with_id_for_admin(self,user_id:int)->None:
        with sqlite3.connect(self.database_name) as connection:
            cursor = connection.cursor()
            cursor.execute(f"DELETE FROM admin WHERE id = ? ",(user_id,))
            connection.commit()


    def list_users_for_admin(self)->list:
        with sqlite3.connect(self.database_name) as connection:
            cursor = connection.cursor()
            cursor.execute(f"SELECT * FROM admin ")
            rows = cursor.fetchall()
            return rows







        # Hepsi İçin Aynı Anda Yapılanlar Yada Genel Olarak Yapılanlar 
   

    def update_admin_table_with_id(self, user_id:int, username:str, surname:str, password:str, email:str, date:str, role:str) -> None:
        with sqlite3.connect(self.database_name) as connection:
            cursor = connection.cursor()
            cursor.execute("""
                UPDATE admin
                SET username = ?, surname = ?, password = ?, email = ?, date = ?, role = ?
                WHERE id = ?
            """, (username, surname, password, email, date, role, user_id))
            connection.commit()

   
   
   
    #-----------------------------------------------------------------------------------------------------------------
    def check_all_auth(self,table_name,username,password)->None:
         with sqlite3.connect(self.database_name) as connection:
            cursor = connection.cursor()
            cursor.execute(f"SELECT * FROM {table_name} WHERE username = ? AND password = ?",(username,password))
            return cursor.fetchone()#("1", "naem", "danis", "1234", "userr@mail.com", "2025-11-13", "noname"))  Döner


    def delete_users_with_id(self,table_name,user_id:int)->None:
        with sqlite3.connect(self.database_name) as connection:
            cursor = connection.cursor()
            cursor.execute(f"DELETE FROM {table_name} WHERE id = ? ",(user_id,))
            connection.commit()

    def list_all_users_with_id(self, table_name, user_id):
        with sqlite3.connect(self.database_name) as connection:
            cursor = connection.cursor()
            cursor.execute(f"SELECT * FROM {table_name} WHERE id=? ", (user_id,))
            row = cursor.fetchone()
            return row
        
    def update_all_users_info_with_id(self, table_name: str, user_id: int, username: str, surname: str, password: str, email: str, date_value: str, role: str):
        with sqlite3.connect(self.database_name) as connection:
            cursor = connection.cursor() 
            cursor.execute(f"""UPDATE {table_name}SET username = ?, surname = ?, password = ?, email = ?, date = ?, role = ?WHERE id = ?""",
            (username, surname, password, email, date_value, role, user_id))
            connection.commit()



    def add_all_user_to_table(self,table_name, username:str, surname:str, password:str, email:str, date, role:str) -> None:
        with sqlite3.connect(self.database_name) as connection:
            cursor = connection.cursor()
            cursor.execute(
                f"INSERT INTO {table_name} (username, surname, password, email, date, role) VALUES (?, ?, ?, ?, ?, ?)",
                (username, surname, password, email, date, role)
            )
      
            connection.commit()


    def check_all_table_with_table_name(self,table_name)->None:
         with sqlite3.connect(self.database_name) as connection:
            cursor = connection.cursor()
            cursor.execute(f"""
                CREATE TABLE IF NOT EXISTS {table_name} (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT NOT NULL,
                    surname TEXT NOT NULL,
                    password TEXT NOT NULL,
                    email TEXT NOT NULL,
                    date TEXT NOT NULL,
                    role TEXT NOT NULL
                )
            """)
            connection.commit()


 

    
        
    
        


            