import streamlit as st
from Database.users_database import UserDatabase
from Database.database_todo import Todo_Database
from Database.book_database import BookDb
import re
import time
import datetime



class Index:
    def __init__(self) -> None:
        st.set_page_config(page_title=" Next Generation Library APP",page_icon="images/app.ico",layout="wide")
        self.book_db = BookDb()
        self.database =UserDatabase()
        self.todo_database = Todo_Database()
        
       
        self.table_name = ""
        
        self.book_id = None
        self.author_id = None
        self.language_id = None
        self.category_id = None
        self.publisher_id = None



        
        if "error" not in st.session_state:
            st.session_state.error = f""

        if "error_status" not in st.session_state:
            st.session_state.error_status = False

        #---member-------------------------------------------------------------------------------------
        if "add_member_user" not in st.session_state:
                        st.session_state["add_member_user"] = False

        if "update_member" not in st.session_state:
            st.session_state["update_member"] = False


        #---stuff-------------------------------------------------------------------------------------
        if "add_stuff_user" not in st.session_state:
                        st.session_state["add_stuff_user"] = False

        if "update_stuff" not in st.session_state:
            st.session_state["update_stuff"] = False
        #---admin------------------------------------------------------------------------------
        if "add_admin_user" not in st.session_state:
                        st.session_state["add_admin_user"] = False

        if "update_admin" not in st.session_state:
            st.session_state["update_admin"] = False
        #-----------------------------------------------------------------------------
      
      
        if "list_user" not in st.session_state: # Bu Ekrana Basması İçin True İse Ekranda Göstericek Diğer Türlü Sidebar İçinde Klaıyot 
             st.session_state["list_user"] = False

        if "list_user_values" not in st.session_state:
             st.session_state["list_user_values"] = ()#Veri Tabanından Dönen Verileri Tutuyoruz

        if "book_list" not in st.session_state:
            st.session_state["book_list"] = ""




        #Todo*----------------------------------------------------------------------------------------------
        if "list_todo" not in st.session_state:
            st.session_state["list_todo"] = ""

        if "todo_add" not in st.session_state:
            st.session_state["todo_add"] = False

        if "update_todo" not in st.session_state:
            st.session_state["update_todo"] = False

        
        #BookAdd----------------------------------------------------------------------------------------------------
        if "book_add" not in st.session_state:
            st.session_state["book_add"] = False

        if "book_list_and_delete" not in st.session_state:
            st.session_state["book_list_and_delete"] = ""   

        if "book_update" not in st.session_state:
            st.session_state["book_update"] = ""

        



        #-------------------------------------------------------------------------------------------Bu Ksımda Güncellemede İdye göre Bilgilein Gelmesi İçin
        if "user_name_update" not in st.session_state:
            st.session_state.user_name_update = ""

        if "surname_update" not in st.session_state:
            st.session_state.surname_update = ""

        if "password_update" not in st.session_state:
            st.session_state.password_update = ""

        if "email_update" not in st.session_state:
            st.session_state.email_update = ""

        if "date_update" not in st.session_state:
            st.session_state.date_update = None

        if "id_number_update" not in st.session_state:#İd Nummber Session Verixe Bunu Göre Çağırıcaz
            st.session_state.id_number_update = ""
        
        if "role_update" not in st.session_state:#İd Nummber Session Verixe Bunu Göre Çağırıcaz
            st.session_state.role_update = ""

        if "description_update" not in st.session_state:#İd Nummber Session Verixe Bunu Göre Çağırıcaz
            st.session_state.description_update = ""
        
        if "title_update" not in st.session_state:#İd Nummber Session Verixe Bunu Göre Çağırıcaz
            st.session_state.title_update = ""

        #-----------------------------------------------------------------------------------------------------------------

        # ------------------ Main Library Fields ------------------
        if "book_name_update" not in st.session_state:
            st.session_state.book_name_update = ""

        if "isbn_update" not in st.session_state:
            st.session_state.isbn_update = ""

        if "original_title_update" not in st.session_state:
            st.session_state.original_title_update = ""

        if "place_of_publication_update" not in st.session_state:
            st.session_state.place_of_publication_update = ""

        if "publication_year_update" not in st.session_state:
            st.session_state.publication_year_update = ""

        if "copyright_year_update" not in st.session_state:
            st.session_state.copyright_year_update = 0

        if "edition_update" not in st.session_state:
            st.session_state.edition_update = ""

        if "translator_update" not in st.session_state:
            st.session_state.translator_update = ""

        if "editor_update" not in st.session_state:
            st.session_state.editor_update = ""

        if "binding_type_update" not in st.session_state:
            st.session_state.binding_type_update = ""

        if "size_cm_update" not in st.session_state:
            st.session_state.size_cm_update = ""

        if "page_count_update" not in st.session_state:
            st.session_state.page_count_update = ""

        if "illustrations_update" not in st.session_state:
            st.session_state.illustrations_update = ""

        if "condition_update" not in st.session_state:
            st.session_state.condition_update = ""

        if "series_update" not in st.session_state:
            st.session_state.series_update = ""

        if "series_issn_update" not in st.session_state:
            st.session_state.series_issn_update = ""

        if "acquisition_date_update" not in st.session_state:
            st.session_state.acquisition_date_update = ""

        if "number_of_copies_update" not in st.session_state:
            st.session_state.number_of_copies_update = ""

        if "available_copies_update" not in st.session_state:
            st.session_state.available_copies_update = ""

        if "loan_type_update" not in st.session_state:
            st.session_state.loan_type_update = ""

        if "ebook_link_update" not in st.session_state:
            st.session_state.ebook_link_update = ""

        if "audio_link_update" not in st.session_state:
            st.session_state.audio_link_update = ""

        if "donor_update" not in st.session_state:
            st.session_state.donor_update = ""

        if "notes_update" not in st.session_state:
            st.session_state.notes_update = ""

        if "cover_image_update" not in st.session_state:
            st.session_state.cover_image_update = None  # BLOB için

        # ------------------ Many-to-Many Fields ------------------
        if "authors_update" not in st.session_state:
            st.session_state.authors_update = ""

        if "categories_update" not in st.session_state:
            st.session_state.categories_update = ""

        if "languages_update" not in st.session_state:
            st.session_state.languages_update = ""

        if "publishers_update" not in st.session_state:
            st.session_state.publishers_update = ""



    def Books_Add(self)->None:
      
        st.markdown("<br>" * 5,unsafe_allow_html=True) #Böyle Daha Mantıklı 
            
        st.header("📔 Books Add", divider=True)
        with st.container(border=True):
            cols = st.columns([1,3])

        # Kapak resmi
        with cols[0]:
            with st.container(border=True,height=600):
                st.subheader("📷 Book Cover")
                uploaded_file = st.file_uploader("", type=["jpg","png"], accept_multiple_files=False)
                if uploaded_file is not None:
                    st.image(uploaded_file, use_container_width=True)

        # Form alanları
        with cols[1]:

            with st.form("book_add_form", border=True, width="stretch",enter_to_submit=False):
                cols = st.columns(4)

                
                with cols[0]:
                    with st.container(border=True,height=500):
                        st.subheader("📖 Book Info")
                        book_name = st.text_input("📘 Book Name", key="books_name")
                        books_writer = st.text_input("✍️ Author", key="books_writer")
                        
                            
                        isbn = st.text_input("🔢 ISBN", key="isbn")
                        original_title = st.text_input("📝 Original Title (if translated)", key="original_title")
                        language = st.selectbox("🌐 Language", ["Turkish", "English", "Spanish", "French"], key="language")
                        category = st.selectbox(
                            "🏷️ Category",
                            ["Fiction","Non-Fiction","Science","Technology","Children / Young Adult","Fantasy / Sci-Fi","Art / Design",
                            "History","Biography / Memoir","Education / Textbook","Self-Help / Personal Development","Philosophy / Religion",
                            "Health / Medicine","Travel / Geography","Cooking / Food","Sports / Recreation","Business / Economics","Law / Politics",
                            "Language / Linguistics","Comics / Graphic Novels","Poetry / Literature","Reference / Encyclopedias","Other"],
                            key="category"
                        )

                    # ------------------- COL 1: Publication Details -------------------
                with cols[1]:
                    with st.container(border=True,height=500):
                        st.subheader("🏢 Publication Details")
                        publisher = st.text_input("🏛️ Publisher", key="publisher")
                        place_of_publication = st.text_input("📍 Place of Publication", key="place_of_publication")
                        publication_year = st.number_input("📅 Publication Year", min_value=1000, max_value=2100, value=2025, step=1, key="publication_year")
                        copyright_year = st.number_input("© Copyright Year", min_value=1000, max_value=2100, value=2025, step=1, key="copyright_year")
                        edition = st.text_input("📚 Edition", key="edition")
                        translator = st.text_input("🌐 Translator (if any)", key="translator")
                        editor = st.text_input("🖊️ Editor (if any)", key="editor")

                # ------------------- COL 2: Physical Details -------------------
                with cols[2]:
                    with st.container(border=True,height=500):
                        st.subheader("📦 Physical Details")
                        binding_type = st.selectbox("📖 Binding Type", ["Paperback", "Hardcover"], key="binding_type")
                        size_cm = st.text_input("📐 Dimensions (cm)", key="size_cm")
                        page_count = st.number_input("📄 Page Count", min_value=1, max_value=10000, key="page_count")
                        illustrations = st.text_input("🖼️ Illustrations / Images", key="illustrations")
                        condition = st.selectbox("🔧 Condition", ["New", "Good", "Fair", "Damaged"], key="condition")

                # ------------------- COL 3: Library Management -------------------
                with cols[3]:
                    with st.container(border=True,height=500):
                        st.subheader("🏛️ Library Management")
                        series = st.text_input("📚 Series Name (if any)", key="series")
                        series_issn = st.text_input("🔢 Series ISSN / ISBN", key="series_issn")
                        acquisition_date = st.date_input("📅 Acquisition Date", key="acquisition_date")
                        number_of_copies = st.number_input("📦 Number of Copies", min_value=1, key="number_of_copies")
                        available_copies = st.number_input("✅ Available Copies", min_value=0, key="available_copies")
                        loan_type = st.selectbox("🔄 Loan Type", ["Normal", "Short Loan", "Reference Only"], key="loan_type")
                        ebook_link = st.text_input("💻 E-book Link", key="ebook_link")
                        audio_link = st.text_input("🎧 Audio Book Link", key="audio_link")
                        donor = st.text_input("🎁 Donor (if any)", key="donor")
                        notes = st.text_area("📝 Notes / Library Notes", key="library_notes")


                

                
                button = st.form_submit_button("➕ Add Book", type="primary", width="stretch")
                if button:
                    self.book_db.main_library()

                    try:
                        if books_writer:
                            self.book_db.author()#Normal Tablo Oluşturuldu
                            self.author_id = self.book_db.add_author_to_table(books_writer)#Yazzar Tabloya eklendi 
                            
                        else:
                            self.author_id = None
                    except Exception as e:
                        st.error(f"Error adding author: {e}")
                        self.author_id = None

                    try:
                        if language:
                            self.book_db.language()
                            self.language_id = self.book_db.add_language_to_table(language)
                        else:
                            self.language_id = None
                    except Exception as e:
                        st.error(f"Error adding language: {e}")
                        self.language_id = None

                    try:
                        if category:
                            self.book_db.category()
                            self.category_id = self.book_db.add_category_to_table(category)
                        else:
                            self.category_id = None
                    except Exception as e:
                        st.error(f"Error adding category: {e}")
                        self.category_id = None

                    try:
                        if publisher:
                            self.book_db.publisher()
                            self.publisher_id = self.book_db.add_publisher_to_table(publisher)
                        else:
                            self.publisher_id = None
                    except Exception as e:
                        st.error(f"Error adding publisher: {e}")
                        self.publisher_id = None


                    data = {
                        "book_name": book_name,
                        "isbn": isbn,
                        "original_title": original_title,
                        "place_of_publication": place_of_publication,
                        "publication_year": publication_year,
                        "copyright_year": copyright_year,
                        "edition": edition,
                        "translator": translator,
                        "editor": editor,
                        "binding_type": binding_type,
                        "size_cm": size_cm,
                        "page_count": page_count,
                        "illustrations": illustrations,
                        "condition": condition,
                        "series": series,
                        "series_issn": series_issn,
                        "acquisition_date": acquisition_date,
                        "number_of_copies": number_of_copies,
                        "available_copies": available_copies,
                        "loan_type": loan_type,
                        "ebook_link": ebook_link,
                        "audio_link": audio_link,
                        "donor": donor,
                        "notes": notes
                    }


                    cover = uploaded_file.getvalue() if uploaded_file else None

                    book_id = self.book_db.add_book_to_table(data, cover)
                    self.book_id = book_id

                    if self.author_id:
                        self.book_db.books_author_table()
                        self.book_db.add_data_to_related_table_that_books_author_table(book_id, self.author_id)

                    if self.language_id:
                        self.book_db.book_language_table()
                        self.book_db.add_data_related_table_to_book_language_table(book_id, self.language_id)

                    if self.publisher_id:
                        self.book_db.book_publisher_table()
                        self.book_db.add_data_related_table_to_book_publisher_table(book_id, self.publisher_id)

                    if self.category_id:
                        self.book_db.book_category_table()
                        self.book_db.add_data_related_table_to_book_category_table(book_id, self.category_id)

                    st.success("Book added successfully!")


    def list_and_delete_books(self)->None:

        def delete_books(books_id):
            self.book_db.delete_books_with_id(books_id)
            st.session_state["book_list_and_delete"] = [t for t in st.session_state["book_list_and_delete"] if t[0] != books_id]



        st.markdown("<br>" * 5,unsafe_allow_html=True) #Böyle Daha Mantıklı 
            
        st.header("📔 Books List And Delete", divider="red")


        books_image = self.book_db.list_books()
        st.session_state["book_list_and_delete"] = books_image

        cols  = st.columns(5)
        for i , info in enumerate(st.session_state["book_list_and_delete"]):
            books_id = info[0]
            books_name = info[1]
            cover_image = info[2]
            cols_index = i % 5
            with cols[cols_index]:
                with st.container(border=True,horizontal_alignment="center",width=1080,height=600):
                    st.image(cover_image,use_container_width=True)  
                with st.expander("Book Info"):
                        st.markdown(f"[{books_id}] : {books_name}")
                        button = st.button(" Delete Book",key=f"delete_book_with_{books_id}",type="primary",width="stretch",on_click=delete_books,args=(books_id,))
                        
    def update_books_info(self)->None:
        
        st.markdown("<br>" * 5,unsafe_allow_html=True) #Böyle Daha Mantıklı 
            
        st.header("📔 Books Update", divider=True)
        with st.container(border=True):
            outside_cols = st.columns([1,3,1])

        # Kapak resmi
        with outside_cols[0]:
            with st.container(border=True, height=600):
                st.subheader("📷 Book Cover")

                
                if st.session_state.get("id_number_update"):#İd Seçildi mi 

                    
                    if st.session_state.get("cover_image_update"):
                        st.image(st.session_state.cover_image_update, use_container_width=True)
                    else:
                        st.info("No cover image available for this book.")

                else:
                    st.info("Please enter a Book ID to load cover image.")



        # Form alanları
        with outside_cols[1]:

            with st.form("book_update_form", border=True, width="stretch",enter_to_submit=False):
                cols = st.columns(4)

                
                with cols[0]:
                    with st.container(border=True,height=500):
                        st.subheader("📖 Book Info")
                        book_name = st.text_input("📘 Book Name", key="book_name_update")
                        books_writer = st.text_input("✍️ Author", key="authors_update")
                        
                            
                        isbn = st.text_input("🔢 ISBN", key="isbn_update")
                        original_title = st.text_input("📝 Original Title (if translated)", key="original_title_update")
                        language = st.selectbox("🌐 Language", ["Turkish", "English", "Spanish", "French"], key="languages_update")
                        category = st.selectbox(
                            "🏷️ Category",
                            ["Fiction","Non-Fiction","Science","Technology","Children / Young Adult","Fantasy / Sci-Fi","Art / Design",
                            "History","Biography / Memoir","Education / Textbook","Self-Help / Personal Development","Philosophy / Religion",
                            "Health / Medicine","Travel / Geography","Cooking / Food","Sports / Recreation","Business / Economics","Law / Politics",
                            "Language / Linguistics","Comics / Graphic Novels","Poetry / Literature","Reference / Encyclopedias","Other"],
                            key="categories_update"
                        )

                    # ------------------- COL 1: Publication Details -------------------
                
                with cols[1]:
                    with st.container(border=True,height=500):
                        st.subheader("🏢 Publication Details")
                        publisher = st.text_input("🏛️ Publisher", key="publishers_update")
                        place_of_publication = st.text_input("📍 Place of Publication", key="place_of_publication_update")
                        publication_year = st.number_input("📅 Publication Year", min_value=1000, max_value=2100, value=2025, step=1, key="publication_year_update")
                        copyright_year = st.number_input("© Copyright Year", min_value=1000, max_value=2100, value=2025, step=1, key="copyright_year_update")
                        edition = st.text_input("📚 Edition", key="edition_update")
                        translator = st.text_input("🌐 Translator (if any)", key="translator_update")
                        editor = st.text_input("🖊️ Editor (if any)", key="editor_update")

                # ------------------- COL 2: Physical Details -------------------
                with cols[2]:
                    with st.container(border=True,height=500):
                        st.subheader("📦 Physical Details")
                        binding_type = st.selectbox("📖 Binding Type", ["Paperback", "Hardcover"], key="binding_type_update")
                        size_cm = st.text_input("📐 Dimensions (cm)", key="size_cm_update")
                        page_count = st.number_input("📄 Page Count", min_value=1, max_value=10000, key="page_count_update")
                        illustrations = st.text_input("🖼️ Illustrations / Images", key="illustrations_update")
                        condition = st.selectbox("🔧 Condition", ["New", "Good", "Fair", "Damaged"], key="condition_update")

                # ------------------- COL 3: Library Management -------------------
                with cols[3]:
                    with st.container(border=True,height=500):
                        st.subheader("🏛️ Library Management")
                        series = st.text_input("📚 Series Name (if any)", key="series_update")
                        series_issn = st.text_input("🔢 Series ISSN / ISBN", key="series_issn_update")
                        acquisition_date = st.date_input("📅 Acquisition Date", key="acquisition_date_update",value=datetime.date.today())
                        number_of_copies = st.number_input("📦 Number of Copies", min_value=1, key="number_of_copies_update")
                        available_copies = st.number_input("✅ Available Copies", min_value=0, key="available_copies_update")
                        loan_type = st.selectbox("🔄 Loan Type", ["Normal", "Short Loan", "Reference Only"], key="loan_type_update")
                        ebook_link = st.text_input("💻 E-book Link", key="ebook_link_update")
                        audio_link = st.text_input("🎧 Audio Book Link", key="audio_link_update")
                        donor = st.text_input("🎁 Donor (if any)", key="donor_update")
                        notes = st.text_area("📝 Notes / Library Notes", key="notes_update")

                
                button = st.form_submit_button("➕ Update ", type="primary", width="stretch")
                if button:
                    data = {
                        "book_name": book_name,
                        "isbn": isbn,
                        "original_title": original_title,
                        "place_of_publication": place_of_publication,
                        "publication_year": publication_year,
                        "copyright_year": copyright_year,
                        "edition": edition,
                        "translator":translator,
                        "editor": editor,
                        "binding_type": binding_type,
                        "size_cm": size_cm,
                        "page_count": page_count,
                        "illustrations": illustrations,
                        "condition": condition,
                        "series": series,
                        "series_issn": series_issn,
                        "acquisition_date": acquisition_date,
                        "number_of_copies": number_of_copies,
                        "available_copies": available_copies,
                        "loan_type": loan_type,
                        "ebook_link": ebook_link,
                        "audio_link": audio_link,
                        "donor": donor,
                        "notes": notes,
                    }

                        
                    
                    self.book_db.update_main_table(st.session_state.id_number_update, data)

                    
                    if books_writer:
                        self.book_db.author()
                        author_id = self.book_db.add_author_to_table(books_writer)
                        if author_id:
                            self.book_db.update_book_authors(st.session_state.id_number_update, [author_id])

                    
                    if language:
                        self.book_db.language()
                        language_id = self.book_db.add_language_to_table(language)
                        if language_id:
                            self.book_db.update_book_languages(st.session_state.id_number_update, [language_id])

                    
                    if category:
                        self.book_db.category()
                        category_id = self.book_db.add_category_to_table(category)
                        if category_id:
                            self.book_db.update_book_categories(st.session_state.id_number_update, [category_id])

                    
                    if publisher:
                        self.book_db.publisher()
                        publisher_id = self.book_db.add_publisher_to_table(publisher)
                        if publisher_id:
                            self.book_db.update_book_publishers(st.session_state.id_number_update, [publisher_id])

                    st.success("Book updated successfully!")




        with outside_cols[2]:
            with st.form("id_form",border=True):
                book_id = st.number_input("Enter Book ID",step=1,key="id_number_update")
                
                st.form_submit_button("Get Books Info",type="secondary",width="stretch",key="get_info",on_click=self.load_books_info)

            st.subheader("📷 UpdatePhoto Photo")
            uploaded_file = st.file_uploader("", type=["jpg","png"], accept_multiple_files=False)
            if uploaded_file is not None:
                if st.session_state.get("id_number_update"):#Seçili Bir anahtar Var mı Kontrol Et 
                    image_bytes = uploaded_file.read()#byte çevrildi blob olarak kayıt edilecek veri tabanına
                    st.session_state.cover_image_update = image_bytes
                    self.book_db.cover_image_update(st.session_state.id_number_update, image_bytes)
                    st.success("Cover image updated!")#Fotoraf Update Edildi Sessiona Gönderildi Sessiondaki Değer Değişiyor
                else:
                    st.warning("Please select a Book ID first!")
                            
   

            




                           

              

                    


                
            
         




    def todo(self)->None:
        st.markdown(" <br> " * 5,unsafe_allow_html=True)
        st.header(" 🗂️ Todo Add",divider=True)
        cols = st.columns([1,2,1])
        with cols[0]:
            pass

        with cols[2]:
            pass
        
        with cols[1]:
            st.image("images/todo.png", width=300)
            with st.container(border=True):
                with st.form("admin_form",border=False):
                    
                    username = st.text_input("Username : ")
                    todo_title = st.text_input("Title :")
                    todo_desc = st.text_area("Description : ")
                    todo_date = st.date_input("Date:")
                    submit_button =   st.form_submit_button(label="ADD TODO")

                    if submit_button:
                        try:
                            self.todo_database.todo_table()
                            self.todo_database.insert_todo(username,todo_title,todo_desc,todo_date)

                            st.success("Todo Added Successfully")
                            st.info(f"**Todo INFO:!**\n\n **Username:** {username}\n\n💬 📝 **Title:** {todo_title}\n\n💬 **Description:** {todo_desc}\n\n📅 **Date:** {todo_date}")
                            time.sleep(1)
                        except Exception as e:
                            st.warning(f"Failed To Add Todo: {st.exception(e)}")
                            st.session_state.todo_add = False 

    def todo_list(self)->None:
        st.markdown(" <br> " * 5,unsafe_allow_html=True)
        st.header("🗂️ Todo List",divider=True)
        
        def delete_todo_from_session(todo_id):
            self.todo_database.delete_todo(todo_id)  # veritabanından sil
            st.session_state["list_todo"] = [t for t in st.session_state["list_todo"] if t[0] != todo_id]

        
        todos_data = self.todo_database.list_todo()
        st.session_state.list_todo = todos_data

        if not st.session_state["list_todo"]:
            st.info("NO TODO")
            return
    
        cols = st.columns(3)
        for i, todo in enumerate(st.session_state["list_todo"]):
            username = f"👤 **Username:** {todo[1]}"
            _id = f"🆔 **ID:** {todo[0]}"
            title = f"📝 **Title:** {todo[2]}"
            description = f"💬 **Description:** {todo[3]}"
            date = f"📅 **Date:** {todo[4]}"

             # Hangi sütuna düşeceğini belirle
            with cols[i]:
                with st.container(key=f"{_id}",border=True,horizontal=True):
                    st.markdown(f"{username}<br>{_id}<br>{title}<br>{date}", unsafe_allow_html=True)
                    st.button("DELETE", key=f"Delete{_id}", on_click=lambda id=todo[0]: delete_todo_from_session(id))

                with st.expander("Description:"):
                    st.info(description)

    def todo_update(self)->None:
        st.markdown(" <br> " * 5,unsafe_allow_html=True)
        st.header(" 🗂️ Todo Update ",divider=True)
        cols = st.columns([1,2,1])
        with cols[0]:
            pass

        with cols[2]:
            pass
        
        with cols[1]:
            st.image("images/todo_update.png", width=300)
            with st.container(border=True):
                cols = st.columns(2)
                    
                with cols[0]:
                    with st.form("todo_updated_form", border=False):
                        user_name = st.text_input("Username:", key="user_name_update")
                        title = st.text_input("Title",key="title_update")
                        description = st.text_area("Description :",key="description_update")
                        date = st.date_input("Date:", key="date_update")
                        submit_update = st.form_submit_button("Update Todo", type="secondary", width="stretch")
                        if submit_update:
                            try: 
                                
                                user_id = st.session_state.id_number_update
                                self.todo_database.todo_table()
                                self.todo_database.update_todo(int(user_id),username=user_name,title=title,description=description,date=date.strftime("%Y-%m-%d"))  # BURASI DÜZELTİLDİ


                                st.success("Updated successfully")
                                time.sleep(1)
                                

                            except Exception as e:
                                st.error(f"Error: Something went wrong while updating the user.")
                                st.session_state.update_todo = False 

                with cols[1]:
                    with st.form("todo_id_form",border=False):
                        st.markdown("Before Update Select User ID : ")
                        user_id = st.text_input("Enter User ID", key="id_number_update")#Buraya Giriş Yapınca Nuber Değeri Değişecek
                        button =st.form_submit_button("Get Todo Info",on_click=self.load_todo_info)#Key İçindeki Değerleri Değişmek İçin On_click İçine Yazmamız gerek
                        if st.session_state.error_status:
                            #st.error(st.session_state.error)#Bu Direk Hatayı Söylüyor Ama Bu Uygun Olmaz 
                            st.error("Error : ( There is no such user and user id ) ")
                            st.session_state.error_status = False #Error Ekranı Rerun Yapsak Bile Kalıcak Çünkü Trueda False Yapmam Gerek 

        
                                     


    def admin_added(self)->None:
        st.markdown(" <br> " * 5,unsafe_allow_html=True)
        st.header("👨‍💻 Admin User Add",divider=True)
        
        cols = st.columns([1,2,1])
        with cols[0]:
            pass

        with cols[2]:
            pass
        
        with cols[1]:
             st.image("images/sign_up.png", width=300)
             with st.container(border=True):
                    with st.form("admin_form",border=False):
                    
                        
                        user_name_add = st.text_input("Username:")
                        surname_add = st.text_input("Surname:")
                        password_add = st.text_input("Password:", type="password")
                        email_add = st.text_input("Email:")
                        date_add = st.date_input("Date:")
                        role_add = st.selectbox("Role", ["Admin"])

                        submit_add = st.form_submit_button("Sign Up",type="secondary",width="stretch")


                        if submit_add:
                            if len(password_add) < 8:
                                st.error("Password too short")
                                return
                            
                            if not re.match(r"[^@]+@[^@]+\.[^@]+", email_add):
                                st.error("Please Enter Valid Email Address")
                                return
                            
                            try:
                                self.database.create_admin_table()
                                self.database.add_admin_to_table(user_name_add,surname_add,password_add,email_add,date_add,role_add)
                                
                                st.success("Stuff Added successfully")
                                time.sleep(1)
                                st.session_state.add_admin_user = False 

                                
                            except Exception as e:
                                st.error(f"Error : Something went wrong while creating the account. ")
                                st.session_state.add_admin_user = False 

    def update_admin(self)->None:
        st.markdown(" <br> " * 5,unsafe_allow_html=True)
        st.header("👨‍💻 Admin User Update ",divider="rainbow")
        
        cols = st.columns([1,2,1])
        with cols[0]:
            pass

        with cols[2]:
            pass
        
        with cols[1]:
            st.image("images/update.png", width=300)
            with st.container(border=True):
                cols = st.columns(2)
                    
                with cols[0]:
                    with st.form("admin_updated_form", border=False):
                        user_name = st.text_input("Username:", key="user_name_update")
                        surname = st.text_input("Surname:", key="surname_update")
                        password = st.text_input("Password:", type="password", key="password_update")
                        email = st.text_input("Email:", key="email_update")
                        date = st.date_input("Date:", key="date_update")
                        role = st.selectbox("Role", ["Admin"], key="role_update")

                        submit_update = st.form_submit_button("Update", type="secondary", width="stretch")

                        if submit_update:
                            if len(password) < 8:
                                st.error("Error : ( Password too short )")
                                return

                            if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
                                st.error("Error : ( Please Enter Valid Email Address )")
                                return

                            try: 
                                
                                user_id = st.session_state.id_number_update
                                self.database.create_admin_table()
                                self.database.update_admin_table_with_id(
                                int(user_id),
                                username=user_name,
                                surname=surname,
                                password=password,
                                email=email,
                                date=date.strftime("%Y-%m-%d"),  # BURASI DÜZELTİLDİ
                                role=role)


                                st.success("Updated successfully")
                                time.sleep(1)
                                

                            except Exception as e:
                                st.error(f"Error: Something went wrong while updating the user.")
                                st.session_state.update_admin = False 

                with cols[1]:
                    with st.form("admin_id_form",border=False):
                        st.markdown("Before Update Select User ID : ")
                        role_str = st.selectbox("Role Select" , ["Admin"],key="role_type")
                        user_id = st.text_input("Enter User ID", key="id_number_update")#Buraya Giriş Yapınca Nuber Değeri Değişecek
                        button =st.form_submit_button("Get User Info",on_click=self.load_users_info)#Key İçindeki Değerleri Değişmek İçin On_click İçine Yazmamız gerek
                        if st.session_state.error_status:
                            #st.error(st.session_state.error)#Bu Direk Hatayı Söylüyor Ama Bu Uygun Olmaz 
                            st.error("Error : ( There is no such user and user id ) ")
                            st.session_state.error_status = False #Error Ekranı Rerun Yapsak Bile Kalıcak Çünkü Trueda False Yapmam Gerek 


    def load_users_info(self)->None:
        users_info = self.database.list_all_users_with_id(st.session_state.role_type,st.session_state.id_number_update)  
        try:
            st.session_state.user_name_update = users_info[1]
            st.session_state.surname_update = users_info[2]
            st.session_state.password_update = users_info[3]
            st.session_state.email_update = users_info[4]
            try:
                st.session_state.date_update = datetime.datetime.strftime(users_info[5],"%Y-%m-%d")
            except:
                st.session_state.date_update = datetime.datetime.today()
                
            st.session_state.role_update = users_info[6]  
            
        except Exception as e:
            st.session_state.error_status = True
            st.session_state.error = f"Error:{e}"
 
    def load_todo_info(self) -> None:
        todo_info = self.todo_database.list_todo_with_id(st.session_state.id_number_update)
        try:
            st.session_state.user_name_update = todo_info[4]
            st.session_state.title_update = todo_info[1]
            st.session_state.description_update = todo_info[2]

            
            try:
                st.session_state.date_update = datetime.datetime.strftime(todo_info[5],"%Y-%m-%d")
            except:
                st.session_state.date_update = datetime.datetime.today()

        except Exception as e:
            st.session_state.error_status = True
            st.session_state.error = f"Error:{e}"

    def load_books_info(self)->None:

        book_id = st.session_state.get("id_number_update")
        if not book_id:
            st.warning("Please enter a Book ID!")
            return

        # DB’de ID var mı kontrol et
        if not self.book_db.book_exists(book_id):
            st.error(f"No book found with ID {book_id}")
            return

        # Eğer var ise bilgileri yükle
        books_info = self.book_db.list_books_and_update(book_id)
        if not books_info:
            st.error("No data found for this book!")
            return
       
        books = self.book_db.list_books_and_update(st.session_state.id_number_update)

        st.session_state.book_name_update = books[1]
        st.session_state.isbn_update = books[2]
        st.session_state.original_title_update = books[3]
        st.session_state.place_of_publication_update = books[4]
        st.session_state.publication_year_update = books[5]

        st.session_state.editor_update = books[6]
        st.session_state.binding_type_update = books[7]
        st.session_state.size_cm_update = books[8]
        st.session_state.page_count_update = books[9]
        st.session_state.illustrations_update = books[10]
        st.session_state.condition_update = books[11]

        st.session_state.series_update = books[12]
        st.session_state.series_issn_update = books[13]
        try:
                st.session_state.acquisition_date_update = datetime.datetime.strftime(books[14],"%Y-%m-%d")
        except:
                st.session_state.acquisition_date_update = datetime.datetime.today()
        st.session_state.number_of_copies_update = books[15]
        st.session_state.available_copies_update = books[16]
        st.session_state.loan_type_update = books[17]

        st.session_state.ebook_link_update = books[18]
        st.session_state.audio_link_update = books[19]
        st.session_state.donor_update = books[20]
        st.session_state.notes_update = books[21]

        st.session_state.authors_update = books[22]
        st.session_state.categories_update = books[23]
        st.session_state.languages_update = books[24]
        st.session_state.publishers_update = books[25]

        
        cover_image = self.book_db.cover_image_with_id(st.session_state.id_number_update)
        st.session_state.cover_image_update = cover_image 

        




        


    def stuff_added(self)->None:
        st.markdown(" <br> " * 5,unsafe_allow_html=True)
        st.header("🧑‍🏫 Stuff User Add",divider=True)
        cols = st.columns([1,2,1])
        with cols[0]:
            pass

        with cols[2]:
            pass
        
        with cols[1]:
             st.image("images/sign_up.png", width=300)
             with st.container(border=True):
                    with st.form("stuff_form",border=False):
                    
                        
                        user_name_add = st.text_input("Username:")
                        surname_add = st.text_input("Surname:")
                        password_add = st.text_input("Password:", type="password")
                        email_add = st.text_input("Email:")
                        date_add = st.date_input("Date:")
                        role_add = st.selectbox("Role", ["Stuff"])

                        submit_add = st.form_submit_button("Sign Up",type="secondary",width="stretch")


                        if submit_add:
                            if len(password_add) < 8:
                                st.error("Password too short")
                                return
                            
                            if not re.match(r"[^@]+@[^@]+\.[^@]+", email_add):
                                st.error("Please Enter Valid Email Address")
                                return
                            
                            try:
                                self.database.create_stuff_table()
                                self.database.add_stuff_to_table(user_name_add,surname_add,password_add,email_add,date_add,role_add)
                                
                                st.success("Stuff Added successfully")
                                time.sleep(1)
                                st.session_state.add_stuff_user = False 

                                
                            except Exception as e:
                                st.error(f"Error : Something went wrong while creating the account. ")
                                st.session_state.add_stuff_user = False 

    def update_stuff(self)->None:
        st.markdown(" <br> " * 5,unsafe_allow_html=True)
        st.header("🧑‍🏫 Stuff User Update",divider=True)
        cols = st.columns([1,2,1])
        with cols[0]:
            pass

        with cols[2]:
            pass
        
        with cols[1]:
            st.image("images/update.png", width=300)
            with st.container(border=True):
                cols = st.columns(2)
                    
                with cols[0]:
                    with st.form("stuff_updated_form", border=False):
                        user_name = st.text_input("Username:", key="user_name_update")
                        surname = st.text_input("Surname:", key="surname_update")
                        password = st.text_input("Password:", type="password", key="password_update")
                        email = st.text_input("Email:", key="email_update")
                        date = st.date_input("Date:", key="date_update")
                        role = st.selectbox("Role", ["Stuff"], key="role_update")

                        submit_update = st.form_submit_button("Update", type="secondary", width="stretch")

                        if submit_update:
                            if len(password) < 8:
                                st.error("Error : ( Password too short )")
                                return

                            if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
                                st.error("Error : ( Please Enter Valid Email Address )")
                                return

                            try: 
                                
                                user_id = st.session_state.id_number_update
                                self.database.create_stuff_table()
                                self.database.update_stuff_table_with_id(
                                int(user_id),
                                username=user_name,
                                surname=surname,
                                password=password,
                                email=email,
                                date=date.strftime("%Y-%m-%d"),  # BURASI DÜZELTİLDİ
                                role=role)


                                st.success("Updated successfully")
                                time.sleep(1)
                                

                            except Exception as e:
                                st.error(f"Error: Something went wrong while updating the user.")
                                st.session_state.update_admin = False 

                with cols[1]:
                    with st.form("stuff_id_form",border=False):
                        st.markdown("Before Update Select User ID : ")
                        role_str = st.selectbox("Role Select" , ["Stuff"],key="role_type")
                        user_id = st.text_input("Enter User ID", key="id_number_update")#Buraya Giriş Yapınca Nuber Değeri Değişecek
                        button =st.form_submit_button("Get User Info",on_click=self.load_users_info)#Key İçindeki Değerleri Değişmek İçin On_click İçine Yazmamız gerek
                        if st.session_state.error_status:
                            #st.error(st.session_state.error)#Bu Direk Hatayı Söylüyor Ama Bu Uygun Olmaz 
                            st.error("Error : ( There is no such user and user id ) ")
                            st.session_state.error_status = False #Error Ekranı Rerun Yapsak Bile Kalıcak Çünkü Trueda False Yapmam Gerek 


    def member_added(self)->None:
        st.markdown(" <br> " * 5,unsafe_allow_html=True)
        st.header("👪 Member User Add",divider=True)
        cols = st.columns([1,2,1])
        with cols[0]:
            pass

        with cols[2]:
            pass
        
        with cols[1]:
             st.image("images/sign_up.png", width=300)
             with st.container(border=True):
                    with st.form("member_form",border=False):
                    
                        
                        user_name_add = st.text_input("Username:")
                        surname_add = st.text_input("Surname:")
                        password_add = st.text_input("Password:", type="password")
                        email_add = st.text_input("Email:")
                        date_add = st.date_input("Date:")
                        role_add = st.selectbox("Role", ["Member"])

                        submit_add = st.form_submit_button("Sign Up",type="secondary",width="stretch")


                        if submit_add:
                            if len(password_add) < 8:
                                st.error("Password too short")
                                return
                            
                            if not re.match(r"[^@]+@[^@]+\.[^@]+", email_add):
                                st.error("Please Enter Valid Email Address")
                                return
                            
                            try:
                                self.database.create_member_table()
                                self.database.add_member_to_table(user_name_add,surname_add,password_add,email_add,date_add,role_add)
                                
                                st.success("Member Added successfully")
                                time.sleep(1)
                                st.session_state.add_member_user = False 

                                
                            except Exception as e:
                                st.error(f"Error : Something went wrong while creating the account. ")
                                st.session_state.add_member_user = False 

    def update_member(self)->None:
        st.markdown(" <br> " * 5,unsafe_allow_html=True)
        st.header("👪 Member User Update",divider=True)
        cols = st.columns([1,2,1])
        with cols[0]:
            pass

        with cols[2]:
            pass
        
        with cols[1]:
            st.image("images/update.png", width=300)
            with st.container(border=True):
                cols = st.columns(2)
                    
                with cols[0]:
                    with st.form("updated_form_member", border=False):
                        user_name = st.text_input("Username:", key="user_name_update")
                        surname = st.text_input("Surname:", key="surname_update")
                        password = st.text_input("Password:", type="password", key="password_update")
                        email = st.text_input("Email:", key="email_update")
                        date = st.date_input("Date:", key="date_update")
                        role = st.selectbox("Role", ["Member"], key="role_update")

                        submit_update = st.form_submit_button("Update", type="secondary", width="stretch")

                        if submit_update:
                            if len(password) < 8:
                                st.error("Error : ( Password too short )")
                                return

                            if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
                                st.error("Error : ( Please Enter Valid Email Address )")
                                return

                            try: 
                                
                                user_id = st.session_state.id_number_update
                                self.database.create_member_table()
                                self.database.update_member_table_with_id(
                                int(user_id),
                                username=user_name,
                                surname=surname,
                                password=password,
                                email=email,
                                date=date.strftime("%Y-%m-%d"),  # BURASI DÜZELTİLDİ
                                role=role)


                                st.success("Updated successfully")
                                time.sleep(1)
                                

                            except Exception as e:
                                st.error(f"Error: Something went wrong while updating the user.")
                                st.session_state.update_member = False 

                with cols[1]:
                    with st.form("user_id_form",border=False):
                        st.markdown("Before Update Select User ID : ")
                        role_str = st.selectbox("Role Select" , ["Member"],key="role_type")
                        user_id = st.text_input("Enter User ID", key="id_number_update")#Buraya Giriş Yapınca Nuber Değeri Değişecek
                        button =st.form_submit_button("Get User Info",on_click=self.load_users_info)#Key İçindeki Değerleri Değişmek İçin On_click İçine Yazmamız gerek
                        if st.session_state.error_status:
                            #st.error(st.session_state.error)#Bu Direk Hatayı Söylüyor Ama Bu Uygun Olmaz 
                            st.error("Error : ( There is no such user and user id ) ")
                            st.session_state.error_status = False #Error Ekranı Rerun Yapsak Bile Kalıcak Çünkü Trueda False Yapmam Gerek 




                         
    def list_all_person_and_delete_by_admin(self)->None:
        st.markdown(" <br> " * 5,unsafe_allow_html=True)
        st.header("🧑 List Users ",divider=True)
        
        def delete_users_from_database(user_id):
            self.database.delete_users_with_id(self.table_name,user_id)  # veritabanından sil
            st.session_state["list_user_values"] = [t for t in st.session_state["list_user_values"] if t[0] != user_id]

        st.markdown("")
        st.markdown("")
        st.markdown("")
        st.markdown("")
        st.markdown("")
        cols = st.columns(3)
        for i, user in enumerate(st.session_state["list_user_values"]):
            _id         = f"🆔 **ID:** {user[0]}"
            username    = f"🧑 **Username:** {user[1]}"
            surname     = f"👪 **Surname:** {user[2]}"
            password    = f"🔑 **Password:** {user[3]}"
            email       = f"📧 **Email:** {user[4]}"
            date        = f"📅 **Date:** {user[5]}"
            role        = f"🛡️ **Role:** {user[6]}"
                        


            cols_peace = i % 3

            with cols[cols_peace]: 
                with st.container(border=True,horizontal=True,horizontal_alignment="left"):
                    st.markdown(f"### {_id}<br>{username}<br>{surname}<br>{password}<br>{email}<br>{date}<br>{role}", unsafe_allow_html=True)
                    st.button("DELETE", key=f"Delete_{_id}",on_click=lambda id=user[0]: delete_users_from_database(id) )
                    
              
         
                       
                    
        
    
    def sidebar(self)->None:

       
        with st.sidebar:
            with st.container(horizontal=True,horizontal_alignment="left") as admin_info:
                st.image("images/female.ico")
                st.markdown(f"<b>{st.session_state.USER[1]}<b>",unsafe_allow_html=True)    

            with st.container(horizontal=True,horizontal_alignment="left") as admin_menu_panel:
                with st.expander(label=" Admin Settings",icon=":material/settings_account_box:"):
                    button1 = st.button(label="➕ Admin Info Add",width="stretch",type="secondary",key="add_admin")
                    if button1:
                        st.session_state.update_todo = False  
                        st.session_state.update_member = False
                        st.session_state.todo_add = False
                        st.session_state.list_todo = False
                        st.session_state.add_member_user = False
                        st.session_state.list_user = False
                        st.session_state.update_admin = False   
                        st.session_state.add_admin_user = True
                        st.session_state.add_stuff_user = False 
                        st.session_state.update_stuff = False 
                        st.session_state.book_add = False
                        st.session_state.book_list_and_delete = False
                        st.session_state.book_update = False

                    button2 = st.button(label="⚙️ Admin Info Update",width="stretch",type="secondary",key="update_admin_user")
                    if button2:
                        st.session_state.update_todo = False  
                        st.session_state.list_todo = False
                        st.session_state.update_member = False
                        st.session_state.todo_add = False
                        st.session_state.add_member_user = False
                        st.session_state.list_user = False
                        st.session_state.add_admin_user = False
                        st.session_state.update_admin = True
                        st.session_state.add_stuff_user = False 
                        st.session_state.update_stuff = False  
                        st.session_state.book_add = False  
                        st.session_state.book_list_and_delete = False
                        st.session_state.book_update = False
             

            with st.container(horizontal=True,horizontal_alignment="left") as stuff_menu_panel:
                with st.expander(label=" Stuff Settings",icon=":material/settings_account_box:"):
                    button1 = st.button(label="➕ Stuff Info Add",width="stretch",type="secondary",key="add_stuff")
                    if button1:
                        st.session_state.update_todo = False  
                        st.session_state.list_todo = False
                        st.session_state.update_member = False
                        st.session_state.todo_add = False
                        st.session_state.add_member_user = False
                        st.session_state.list_user = False
                        st.session_state.update_admin = False 
                        st.session_state.update_stuff = False  
                        st.session_state.add_admin_user = False
                        st.session_state.add_stuff_user = True
                        st.session_state.book_add = False
                        st.session_state.book_list_and_delete = False
                        

                    button2 = st.button(label="⚙️ Stuff Info Update",width="stretch",type="secondary",key="update_stuff_user")
                    if button2:
                        st.session_state.update_todo = False  
                        st.session_state.list_todo = False
                        st.session_state.update_member = False
                        st.session_state.todo_add = False
                        st.session_state.add_member_user = False
                        st.session_state.list_user = False
                        st.session_state.add_admin_user = False
                        st.session_state.update_admin = False 
                        st.session_state.add_stuff_user = False 
                        st.session_state.update_stuff = True 
                        st.session_state.book_add = False
                        st.session_state.book_list_and_delete = False

            with st.container(horizontal=True,horizontal_alignment="left") as member_menu_panel:
                with st.expander(label="Member Settings",icon=":material/settings_account_box:"):
                    button = st.button(label="➕Member Info Add",width="stretch",type="secondary",key="member_user")
                    if button:
                        st.session_state.update_todo = False  
                        st.session_state.list_todo = False
                        st.session_state.list_user = False
                        st.session_state.todo_add = False
                        st.session_state.update_admin = False 
                        st.session_state.update_stuff = False  
                        st.session_state.add_admin_user = False
                        st.session_state.add_stuff_user = False
                        st.session_state.update_member = False
                        st.session_state.add_member_user = True
                        st.session_state.book_add = False
                        st.session_state.book_list_and_delete = False
                        st.session_state.book_update = False
                        

                  
                    button= st.button(label="⚙️ Member  Update",width="stretch",type="secondary",key="update_member_user")
                    
                    if button:
                        st.session_state.update_todo = False  
                        st.session_state.list_todo = False
                        st.session_state.list_user = False
                        st.session_state.todo_add = False
                        st.session_state.update_admin = False 
                        st.session_state.update_stuff = False  
                        st.session_state.add_admin_user = False
                        st.session_state.add_stuff_user = False
                        st.session_state.update_member = True
                        st.session_state.add_member_user = False
                        st.session_state.book_add = False
                        st.session_state.book_list_and_delete = False
                        st.session_state.book_update = False


        

            with st.container(horizontal=True,horizontal_alignment="left") as Book_menu_panel:
                with st.expander(label="  Book Settings",icon=":material/bookmarks:"):
                    button = st.button(label="## Book Info Add",icon=":material/bookmark_add:",width="stretch",type="secondary",key="add_book_info")
                    if button:
                        st.session_state.book_add = True
                        st.session_state.update_todo = False  
                        st.session_state.list_todo = False
                        st.session_state.update_member = False
                        st.session_state.todo_add = False
                        st.session_state.add_member_user = False
                        st.session_state.list_user = False
                        st.session_state.update_admin = False 
                        st.session_state.update_stuff = False  
                        st.session_state.add_admin_user = False
                        st.session_state.add_stuff_user = False
                        st.session_state.book_list_and_delete = False
                        st.session_state.book_update = False
                        

                    button = st.button(label="## Book List and Delete",icon=":material/bookmark_remove:",width="stretch",type="secondary",key="delete_book_info")
                    if button:
                        st.session_state.book_list_and_delete = True
                        st.session_state.book_add = False
                        st.session_state.update_todo = False  
                        st.session_state.list_todo = False
                        st.session_state.update_member = False
                        st.session_state.todo_add = False
                        st.session_state.add_member_user = False
                        st.session_state.list_user = False
                        st.session_state.update_admin = False 
                        st.session_state.update_stuff = False  
                        st.session_state.add_admin_user = False
                        st.session_state.add_stuff_user = False
                        st.session_state.book_update = False
                        
                        
                        
                        



                    button = st.button(label="## Book Info Update",icon=":material/bookmark_added:",width="stretch",type="secondary",key="update_book_info")
                    if button:
                        st.session_state.book_update = True
                        st.session_state.book_list_and_delete = False
                        st.session_state.book_add = False
                        st.session_state.update_todo = False  
                        st.session_state.list_todo = False
                        st.session_state.update_member = False
                        st.session_state.todo_add = False
                        st.session_state.add_member_user = False
                        st.session_state.list_user = False
                        st.session_state.update_admin = False 
                        st.session_state.update_stuff = False  
                        st.session_state.add_admin_user = False
                        st.session_state.add_stuff_user = False
                        

            with st.container(horizontal=True,horizontal_alignment="left") as Todo_menu_panel:
                with st.expander(label="  Todo Settings",icon=":material/fact_check:"):
                    button = st.button(label="➕ Todo Info Add",width="stretch",type="secondary",key="add_todo_to_user")
                    if button:
                        st.session_state.list_todo = False
                        st.session_state.todo_add = True
                        st.session_state.update_member = False
                        st.session_state.add_member_user = False
                        st.session_state.list_user = False
                        st.session_state.update_admin = False 
                        st.session_state.update_stuff = False  
                        st.session_state.add_admin_user = False
                        st.session_state.add_stuff_user = False
                        st.session_state.update_todo = False  
                        st.session_state.book_add = False
                        st.session_state.book_list_and_delete = False
                        st.session_state.book_update = False

                    button = st.button(label="📋Todo Info List",width="stretch",type="secondary",key="list_info_todo")
                    if button:
                        st.session_state.list_todo = True 
                        st.session_state.todo_add = False
                        st.session_state.update_member = False
                        st.session_state.add_member_user = False
                        st.session_state.list_user = False
                        st.session_state.update_admin = False 
                        st.session_state.update_stuff = False  
                        st.session_state.add_admin_user = False
                        st.session_state.add_stuff_user = False  
                        st.session_state.update_todo = False 
                        st.session_state.book_add = False 
                        st.session_state.book_list_and_delete= False  
                        st.session_state.book_update = False     

                    button = st.button(label="⚙️Todo Info Update",width="stretch",type="secondary",key="update_todo_info")
                    if button:
                        st.session_state.update_todo = True
                        st.session_state.list_todo = False 
                        st.session_state.todo_add = False
                        st.session_state.update_member = False
                        st.session_state.add_member_user = False
                        st.session_state.list_user = False
                        st.session_state.update_admin = False 
                        st.session_state.update_stuff = False  
                        st.session_state.add_admin_user = False
                        st.session_state.add_stuff_user = False  
                        st.session_state.book_add = False
                        st.session_state.book_list_and_delete = False
                        st.session_state.book_update = False
                        

            st.markdown("<hr>",unsafe_allow_html=True)
            

            # Eğer session_state içinde yoksa varsayılanı ekle
            

            with st.container(horizontal=True, horizontal_alignment="center") as delete_and_list:

                if "user_role_select_for_delete_and_list" not in st.session_state:
                    st.session_state.user_role_select_for_delete_and_list = ""

                user_role = st.selectbox(
                    "List and Delete Users",
                    ["", "Stuff", "Member", "Admin"],
                    index=["", "Stuff", "Member", "Admin"].index(st.session_state.user_role_select_for_delete_and_list),
                    key="user_role_select_for_delete_and_list"
                )

                # Eğer selectbox boş değilse diğer sessionları kapat ve listeyi aç
                if st.session_state.user_role_select_for_delete_and_list != "":
                    st.session_state.list_user = True
                    st.session_state.add_admin_user = False
                    st.session_state.update_admin = False
                    st.session_state.add_stuff_user = False
                    st.session_state.update_stuff = False
                    st.session_state.add_member_user = False
                    st.session_state.update_member = False
                    st.session_state.todo_add = False
                    st.session_state.list_todo = False
                    st.session_state.update_todo = False
                    st.session_state.todo_add = False
                    st.session_state.book_add = False
                    st.session_state.book_list_and_delete = False
                    st.session_state.book_update = False
                    
                    
                    

                    if st.session_state.user_role_select_for_delete_and_list.lower() == "stuff":
                        users_info = self.database.list_users_for_stuff()
                        st.session_state["list_user_values"] = users_info
                        self.table_name = "stuff"

                    elif st.session_state.user_role_select_for_delete_and_list.lower() == "admin":
                        users_info = self.database.list_users_for_admin()
                        st.session_state["list_user_values"] = users_info
                        self.table_name = "admin"

                    elif st.session_state.user_role_select_for_delete_and_list.lower() == "member":
                        users_info = self.database.list_users_for_member()
                        st.session_state["list_user_values"] = users_info
                        self.table_name = "member"


            
                        
                        
                        

        

                

    def menu(self):
        
        cols = st.columns([2,4,1])
        with cols[0]:
             with st.container(horizontal=True,horizontal_alignment="left"):
                
                with st.container(horizontal=True):
                    st.image("images/github.ico")
                    st.link_button("Github","http.google.com",type="tertiary")
               
                with st.container(horizontal=True):
                    st.image("images/youtube_14198.ico")
                    st.link_button("Youtube","http.google.com",type="tertiary")
                
                with st.container(horizontal=True):
                    st.image("images/instagram.ico")
                    st.link_button("Instagram","http.google.com",type="tertiary")
                
                with st.container(horizontal=True):
                    st.image("images/facebook.ico")
                    st.link_button("Facebook","http.google.com",type="tertiary")            
             
        with cols[1]:
            st.markdown("""
            <div style='margin-top:-40px;'>
                <h1 style="text-align:center;">📚 Welcome to the Library & TODO App</h1>
                
            </div>
            """, unsafe_allow_html=True)

    
        with cols[2]:
             with st.container(horizontal=True, horizontal_alignment="right"):
                    with st.container(horizontal= True):
                        st.image("images/exit.ico")
                        button_sign_in = st.button("Logout",type="tertiary",key="button_sign_in")
                        if button_sign_in:
                            st.session_state.clear()
                            st.switch_page("pages/index.py")
                            
                        
                        

                    
                    
          
    
            
            

if __name__ == "__main__":
    app = Index()
    app.menu()
    app.sidebar()
    if st.session_state.add_admin_user:#Session Aktif İse  Formu Getir  Sonra Kapat Kapatma Kısmını Fonksiyon İçinde Yapıyoruz  
        app.admin_added()

    if st.session_state.list_user:
         app.list_all_person_and_delete_by_admin() 

    if st.session_state["update_admin"] == True:
        app.update_admin()

    if st.session_state.add_stuff_user:
        app.stuff_added()

    if st.session_state.update_stuff:
         app.update_stuff()

    if st.session_state.add_member_user:
        app.member_added()

    if st.session_state.update_member:
         app.update_member()

    if st.session_state.todo_add:
        app.todo()

    if st.session_state.list_todo:
        app.todo_list()

    if st.session_state.update_todo:
        app.todo_update()

    if st.session_state.book_add:
        app.Books_Add()

    if st.session_state.book_list_and_delete:
        app.list_and_delete_books()

    if st.session_state.book_update:
        app.update_books_info()

    
         

    
    