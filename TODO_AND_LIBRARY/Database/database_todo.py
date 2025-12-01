import sqlite3
import pandas 

class Todo_Database:
    def __init__(self) -> None:
        self.todo_database_name = "Database/Database.db"
        

    def todo_table(self) -> None:
        with sqlite3.connect(self.todo_database_name) as connection:
            cursor = connection.cursor()
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS todo (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            title TEXT NOT NULL,
            description TEXT NOT NULL,
            date TEXT NOT NULL)
""")

            connection.commit()



    def insert_todo(self,username,todo_title,todo_description,todo_date)->None:
        connection = sqlite3.connect(self.todo_database_name)
        cursor = connection.cursor()
        cursor.execute("INSERT INTO todo (username , title ,description ,date) VALUES (?,?,?,?)",(username,todo_title,todo_description,str(todo_date)))
        connection.commit()
        connection.close()

    def list_todo(self)-> list :
        with sqlite3.connect(self.todo_database_name) as connection:
            cursor = connection.cursor()
            cursor.execute("SELECT id , username , title ,description,date FROM todo")
            rows = cursor.fetchall()
            return rows
        
    def list_todo_with_id(self,todo_id)->list:
        with sqlite3.connect(self.todo_database_name,) as connection:
            cursor = connection.cursor()
            cursor.execute(f"SELECT * FROM todo WHERE id=? ", (todo_id,))
            rows = cursor.fetchone()
            return rows

            
    def delete_todo(self, todo_id) -> None:
        with sqlite3.connect(self.todo_database_name) as connection:
            cursor = connection.cursor()
            cursor.execute("DELETE FROM todo WHERE id = ?", (todo_id,))
            connection.commit()

    def update_todo(self,todo_id,username,title,description,date)->None:
        with sqlite3.connect(self.todo_database_name) as connection:
            cursor = connection.cursor()
            cursor.execute("""UPDATE todo SET username = ? , title = ? ,description = ? , date = ? WHERE id =?""",(username,title,description,date,todo_id))
            connection.commit()
