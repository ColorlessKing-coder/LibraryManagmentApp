import sqlite3




class BookDb:


    def __init__(self) -> None:
        self.database_name = "Database/Database.db"
        self.pragma = "PRAGMA foreign_keys = ON;"



    
    
    
    
    def create_indexes(self):
        with sqlite3.connect(self.database_name) as connection:
            cursor = connection.cursor()

            cursor.execute("CREATE INDEX IF NOT EXISTS idx_books_author_book ON books_author(book_id);")
            cursor.execute("CREATE INDEX IF NOT EXISTS idx_books_author_author ON books_author(author_id);")

            cursor.execute("CREATE INDEX IF NOT EXISTS idx_book_publisher_book ON book_publisher(book_id);")
            cursor.execute("CREATE INDEX IF NOT EXISTS idx_book_publisher_pub ON book_publisher(publisher_id);")


            cursor.execute("CREATE INDEX IF NOT EXISTS idx_book_language_book ON book_language(book_id);")
            cursor.execute("CREATE INDEX IF NOT EXISTS idx_book_language_lang ON book_language(language_id);")

            cursor.execute("CREATE INDEX IF NOT EXISTS idx_book_category_book ON book_category(book_id);")
            cursor.execute("CREATE INDEX IF NOT EXISTS idx_book_category_cat ON book_category(category_id);")

            connection.commit()

    

    def main_library(self):
        with sqlite3.connect(self.database_name) as connection:
            cursor = connection.cursor()
            cursor.execute(self.pragma)
            cursor.execute(f"""
                CREATE TABLE IF NOT EXISTS main_library (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    book_name TEXT,cover_image BLOB,
                    isbn TEXT,original_title TEXT,
                    place_of_publication TEXT,
                    publication_year INTEGER,
                    copyright_year INTEGER,edition TEXT,
                    translator TEXT,editor TEXT,binding_type TEXT,
                    size_cm TEXT,page_count INTEGER,
                    illustrations TEXT,condition TEXT,
                    series TEXT,series_issn TEXT,
                    acquisition_date TEXT,number_of_copies INTEGER,
                    available_copies INTEGER,loan_type TEXT,
                    ebook_link TEXT,audio_link TEXT,
                    donor TEXT,notes TEXT);""")
             
            connection.commit()
        
    
    #Bu Tamamen Kitap ekleme Ksımıq
    def add_book_to_table(self, data, cover_image):
        with sqlite3.connect(self.database_name) as conn:
            cursor = conn.cursor()

            cursor.execute("""
                INSERT OR IGNORE INTO main_library (
                    book_name, isbn, original_title, place_of_publication,
                    publication_year, copyright_year, edition, translator,
                    editor, binding_type, size_cm, page_count, illustrations,
                    condition, series, series_issn, acquisition_date,
                    number_of_copies, available_copies, loan_type, ebook_link,
                    audio_link, donor, notes, cover_image
                )
                VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
            """, (
                data["book_name"],
                data["isbn"],
                data["original_title"],
                data["place_of_publication"],
                data["publication_year"],
                data["copyright_year"],
                data["edition"],
                data["translator"],
                data["editor"],
                data["binding_type"],
                data["size_cm"],
                data["page_count"],
                data["illustrations"],
                data["condition"],
                data["series"],
                data["series_issn"],
                data["acquisition_date"],
                data["number_of_copies"],
                data["available_copies"],
                data["loan_type"],
                data["ebook_link"],
                data["audio_link"],
                data["donor"],
                data["notes"],
                cover_image  # <<< BLOB BURAYA GELİYOR
            ))
            book_id = cursor.lastrowid#Tabloya Eklenen Bilgide Oluşan İdyi Döndürür Bu İd İlişkili Tüm Tablolarda Kullanlacak
            conn.commit()
            return book_id






        # ----------------- INDEX CREATION ----------------- Hızlandırma İçin Kullaılır 
    
  
    def delete_books_with_id(self,book_id)->None:
        with sqlite3.connect(self.database_name) as connection:
            cursor = connection.cursor()
            cursor.execute("DELETE FROM main_library WHERE id = ?",(book_id,))
            connection.commit()

    def list_books(self) -> list:
        with sqlite3.connect(self.database_name) as connection:
            cursor = connection.cursor()
            cursor.execute("SELECT  id ,book_name, cover_image FROM main_library ")  
            data = cursor.fetchall()
            return data

    def cover_image_with_id(self, book_id):
        with sqlite3.connect(self.database_name) as connection:
            cursor = connection.cursor()
            cursor.execute(
                "SELECT cover_image FROM main_library WHERE id = ?", (book_id,)
            )
            result = cursor.fetchone()

            if result:
                return result[0]      
            else:
                return None


    def cover_image_update(self, book_id: int, image_bytes: bytes) -> None:
        with sqlite3.connect(self.database_name) as connection: 
            cursor = connection.cursor()
            cursor.execute("UPDATE main_library SET cover_image = ? WHERE id = ?",(image_bytes, book_id))
            connection.commit()





    def list_books_and_update(self,books_id):
        with sqlite3.connect(self.database_name) as connection:
            cursor = connection.cursor()
            cursor.execute("""
            SELECT ml.id,ml.book_name,ml.isbn,ml.original_title, ml.place_of_publication,ml.publication_year, ml.editor,
            ml.binding_type,ml.size_cm, ml.page_count,ml.illustrations,ml.condition,ml.series,ml.series_issn,ml.acquisition_date,
            ml.number_of_copies, ml.available_copies,ml.loan_type,ml.ebook_link, ml.audio_link,ml.donor, ml.notes,
            GROUP_CONCAT(DISTINCT author.author_name) AS authors,          GROUP_CONCAT(DISTINCT category.category_name) AS categories,
            GROUP_CONCAT(DISTINCT language.language_name) AS languages,    GROUP_CONCAT(DISTINCT publisher.publisher_name) AS publishers,ml.cover_image
            FROM main_library ml

            LEFT JOIN books_author ba ON ba.book_id = ml.id
            LEFT JOIN author ON author.id = ba.author_id

            LEFT JOIN book_category bc ON bc.book_id = ml.id
            LEFT JOIN category ON category.id = bc.category_id

            LEFT JOIN book_language bl ON bl.book_id = ml.id
            LEFT JOIN language ON language.id = bl.language_id

            LEFT JOIN book_publisher bp ON bp.book_id = ml.id
            LEFT JOIN publisher ON publisher.id = bp.publisher_id

            WHERE ml.id = ?
            GROUP BY ml.id;""",(books_id,))  
            data = cursor.fetchone()
            return data

    def update_main_table(self, book_id, data):
        with sqlite3.connect(self.database_name) as connection:
            cursor = connection.cursor()

            cursor.execute("""
                UPDATE main_library SET book_name = ? ,isbn = ?,original_title = ?,place_of_publication = ?,publication_year = ?,
                copyright_year = ?,edition = ?,translator = ?,editor = ?,binding_type = ?,size_cm = ?,page_count = ?,illustrations = ?,
                condition = ?,series = ?,series_issn = ?,acquisition_date = ?,number_of_copies = ?,available_copies = ?,loan_type = ?,
                ebook_link = ?,audio_link = ?,donor = ?,notes = ? WHERE id = ?""", (
                data["book_name"],data["isbn"], data["original_title"],data["place_of_publication"],data["publication_year"], data["copyright_year"],
                data["edition"],data["translator"], data["editor"],  data["binding_type"], data["size_cm"],
                data["page_count"], data["illustrations"], data["condition"],data["series"], data["series_issn"], data["acquisition_date"],data["number_of_copies"],
                data["available_copies"],data["loan_type"], data["ebook_link"],data["audio_link"],data["donor"],data["notes"],book_id))

            connection.commit()

    def book_exists(self, book_id):
        with sqlite3.connect(self.database_name) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT 1 FROM main_library WHERE id = ?", (book_id,))
            return cursor.fetchone() is not None




    # ----------------- Authors Create Table   -----------------
    def author(self) -> None:
        with sqlite3.connect(self.database_name) as connection:
            cursor = connection.cursor()
            cursor.execute(self.pragma)
            cursor.execute(f"""
                CREATE TABLE IF NOT EXISTS author (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    author_name TEXT NOT NULL UNIQUE
                );
            """)
            connection.commit()

    #-------------------- Add authors To Authors Table     
    def add_author_to_table(self, author_name):
        if not author_name:
            return None

        clean_name = author_name.strip().title()

        with sqlite3.connect(self.database_name) as conn:
            cur = conn.cursor()
            try:
                cur.execute("INSERT INTO author (author_name) VALUES (?)", (clean_name,))
                conn.commit()
                return cur.lastrowid
            except sqlite3.IntegrityError:
                # Zaten varsa ID'yi al
                cur.execute("SELECT id FROM author WHERE author_name = ?", (clean_name,))
                row = cur.fetchone()
                if row:
                    return row[0]
                return None

        
    
    # ----------------- Books-Authors N-N Table -----------------
    def books_author_table(self) -> None:
        with sqlite3.connect(self.database_name) as connection:
            cursor = connection.cursor()
            cursor.execute(self.pragma)
            cursor.execute(f"""
                CREATE TABLE IF NOT EXISTS books_author (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    book_id INTEGER NOT NULL,
                    author_id INTEGER NOT NULL,
                    FOREIGN KEY(book_id) REFERENCES main_library(id),
                    FOREIGN KEY(author_id) REFERENCES author(id),
                    UNIQUE(book_id, author_id)
                );
            """)
            connection.commit()

    #Add Authors Info Releatde Table---------------------------------- 
    
    
    def add_data_to_related_table_that_books_author_table(self,book_id,author_id):
        with sqlite3.connect(self.database_name) as connection:
            cursor = connection.cursor()
            cursor.execute(self.pragma)
            cursor.execute(""" INSERT OR IGNORE INTO books_author (book_id,author_id) VALUES (?,?)""",(book_id,author_id))
            connection.commit()
            
    

        # ------------------- 1️⃣ Yazarları Güncelle -------------------
       
    def update_book_authors(self, book_id, author_ids: list):
        with sqlite3.connect(self.database_name) as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM books_author WHERE book_id = ?", (book_id,))  #dediğimizde, sadece o kitabın mevcut yazar ilişkilerini temizliyoruz, kitabın kendisi main_library tablosundan silinmiyor.
            for a_id in author_ids:
                cursor.execute("INSERT INTO books_author (book_id, author_id) VALUES (?, ?)", (book_id, a_id))
            conn.commit()

    # ------------------- 2️⃣ Kategorileri Güncelle -------------------
    def update_book_categories(self, book_id, category_ids: list):
        with sqlite3.connect(self.database_name) as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM book_category WHERE book_id = ?", (book_id,))
            for c_id in category_ids:
                cursor.execute("INSERT INTO book_category (book_id, category_id) VALUES (?, ?)", (book_id, c_id))
            conn.commit()

    # ------------------- 3️⃣ Dilleri Güncelle -------------------
    def update_book_languages(self, book_id, language_ids: list):
        with sqlite3.connect(self.database_name) as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM book_language WHERE book_id = ?", (book_id,))
            for l_id in language_ids:
                cursor.execute("INSERT INTO book_language (book_id, language_id) VALUES (?, ?)", (book_id, l_id))
            conn.commit()

    # ------------------- 4️⃣ Yayınevlerini Güncelle -------------------
    def update_book_publishers(self, book_id, publisher_ids: list):
        with sqlite3.connect(self.database_name) as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM book_publisher WHERE book_id = ?", (book_id,))
            for p_id in publisher_ids:
                cursor.execute("INSERT INTO book_publisher (book_id, publisher_id) VALUES (?, ?)", (book_id, p_id))
            conn.commit()

    
 

        
            

    # ---
    # 
    # 
    # 
    # -------------- Publisher Table -----------------

    def add_publisher_to_table(self,publisher_name):
        with sqlite3.connect(self.database_name) as conn:
            cur = conn.cursor()
            cur.execute("SELECT id FROM publisher WHERE publisher_name = ?", (publisher_name,))
            row = cur.fetchone()
            if row:
                return row[0]
            cur.execute("INSERT   INTO publisher (publisher_name) VALUES (?)", (publisher_name,))
            conn.commit()
            return cur.lastrowid
            
   

    def publisher(self) -> None:
        with sqlite3.connect(self.database_name) as connection:
            cursor = connection.cursor()
            cursor.execute(self.pragma)
            cursor.execute(f"""
                CREATE TABLE IF NOT EXISTS publisher (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    publisher_name TEXT NOT NULL UNIQUE
                );
            """)
            connection.commit()

    # ----------------- Books-Publisher N-N Table -----------------
    def book_publisher_table(self) -> None:
        with sqlite3.connect(self.database_name) as connection:
            cursor = connection.cursor()
            cursor.execute(self.pragma)
            cursor.execute(f"""
                CREATE TABLE IF NOT EXISTS book_publisher (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                book_id INTEGER NOT NULL,
                publisher_id INTEGER NOT NULL,
                FOREIGN KEY(book_id) REFERENCES main_library(id),
                FOREIGN KEY(publisher_id) REFERENCES publisher(id),
                UNIQUE(book_id, publisher_id));
            """)
            connection.commit()



    def add_data_related_table_to_book_publisher_table(self,book_id,publisher_id)->None:
        with sqlite3.connect(self.database_name) as connection:
            cursor = connection.cursor()
            cursor.execute(self.pragma)
            cursor.execute("INSERT OR IGNORE INTO book_publisher (book_id, publisher_id) VALUES (?, ?)",(book_id,publisher_id))


            connection.commit()








    def add_language_to_table(self,language_name):
         with sqlite3.connect(self.database_name) as conn:
            cur = conn.cursor()
            cur.execute("SELECT id FROM language WHERE language_name = ?", (language_name,))
            row = cur.fetchone()
            if row:
                return row[0]
            cur.execute("INSERT   INTO language (language_name) VALUES (?)", (language_name,))
            conn.commit()
            return cur.lastrowid

    def language(self)->None:
        with sqlite3.connect(self.database_name) as connect:
            cursor = connect.cursor()
            cursor.execute(self.pragma)
            cursor.execute(f"""
            CREATE TABLE IF NOT EXISTS language 
            (id INTEGER PRIMARY KEY AUTOINCREMENT,language_name TEXT NOT NULL UNIQUE);""")
            connect.commit()

    def book_language_table(self)->None:
          with sqlite3.connect(self.database_name) as connect:
            cursor = connect.cursor()
            cursor.execute(self.pragma)
            cursor.execute(f"""
           CREATE TABLE IF NOT EXISTS book_language (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            book_id INTEGER NOT NULL,
            language_id INTEGER NOT NULL,
            FOREIGN KEY (book_id) REFERENCES main_library(id),
            FOREIGN KEY (language_id) REFERENCES language(id),
            UNIQUE (book_id, language_id));""")
            connect.commit()

    def add_data_related_table_to_book_language_table(self,book_id,language_id):
        with sqlite3.connect(self.database_name) as connection:
            cursor = connection.cursor()
            cursor.execute(self.pragma)
            cursor.execute("INSERT OR IGNORE INTO book_language (book_id,language_id) VALUES (?,?)",(book_id,language_id))
            connection.commit()





    def add_category_to_table(self,category_name):
        with sqlite3.connect(self.database_name) as conn:
            cur = conn.cursor()
            cur.execute("SELECT id FROM category WHERE category_name = ?", (category_name,))
            row = cur.fetchone()
            if row:
                return row[0]
            cur.execute("INSERT  INTO category (category_name) VALUES (?)", (category_name,))
            conn.commit()
            return cur.lastrowid
        
   
    def category(self)->None:
        with sqlite3.connect(self.database_name) as connect:
            cursor = connect.cursor()
            cursor.execute(self.pragma)
            cursor.execute(f"""
            CREATE TABLE IF NOT EXISTS category 
            (id INTEGER PRIMARY KEY AUTOINCREMENT,category_name TEXT NOT NULL UNIQUE);""")
            connect.commit()

    def book_category_table(self)->None:
        with sqlite3.connect(self.database_name) as connect:
            cursor = connect.cursor()
            cursor.execute(self.pragma)
            cursor.execute(f"""
           CREATE TABLE IF NOT EXISTS book_category (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            book_id INTEGER NOT NULL,
            category_id INTEGER NOT NULL,
            FOREIGN KEY (book_id) REFERENCES main_library(id),
            FOREIGN KEY (category_id) REFERENCES category(id),
            UNIQUE (book_id, category_id));""")
            connect.commit()

    def add_data_related_table_to_book_category_table(self,book_id,category_id):
        with sqlite3.connect(self.database_name) as connection:
            cursor = connection.cursor()
            cursor.execute(self.pragma)
            cursor.execute(""" INSERT OR IGNORE INTO book_category (book_id,category_id) VALUES (?,?)""",(book_id,category_id))
            connection.commit()
               
       



    


