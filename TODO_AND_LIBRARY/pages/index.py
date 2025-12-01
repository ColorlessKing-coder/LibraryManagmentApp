import streamlit as st
from PIL import Image



class Index:
    def __init__(self) -> None:
        st.set_page_config(layout="wide", page_title=" Next Generation Library APP",page_icon="images/app.ico")
       




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
            with st.container(horizontal_alignment="left"):
                st.markdown("""
                    <h1 style="text-align:center;">📚 Welcome to the Library & TODO App</h1>
                    <p style="text-align:center; font-size:18px;">
                        Manage books, keep track of tasks, stay organized.
                    </p>
                """, unsafe_allow_html=True)
    
        with cols[2]:
             with st.container(horizontal=True, horizontal_alignment="right"):
                    with st.container(horizontal= True):
                        st.image("images/login.ico")
                        button_sign_in = st.button("Sign In",type="tertiary",key="button_sign_in")
                        if button_sign_in:
                            st.switch_page("pages/login.py")
                        
                        

                    
                    with st.container(horizontal=True):
                        st.image("images/add_user.ico")
                        button_sign_up = st.button("Sign UP",type="tertiary",key="button_sign_up")
                        if button_sign_up:
                            st.switch_page("pages/logup.py")

    def books_menu(self)->None:
        st.markdown("")
        st.markdown("")
        st.markdown("")
        st.markdown("")
        st.markdown("")
        st.markdown("")
       
       
        PhotoMid  = st.columns([1,3,1]) 
        with PhotoMid[0]:
            if st.button("Next >>",key="left"):
                st.write("Go to next")

        with PhotoMid[2]:
            if st.button("Next >>",key="right"):
                st.write("Go to next")

        with PhotoMid[1]:
            st.subheader("The Most Reading Books This Year")

            with st.container(border=True, width=1000):
                # Görsellerin yolu
                image_paths = [
                    "images/rng_aksam_gunesi_.jpg",
                    "images/unnamed.jpg",
                    "images/books.jpg",
                    "images/ak.jpg",
                    "images/ak1.jpg"  # 5. görseli ekleyin
                ]
                cols = st.columns(5)

                for i, img_path in enumerate(image_paths):
                    with cols[i]:
                        img = Image.open(img_path)
                        
                        img_resized = img.resize((1080,1920))
                        st.image(img_resized)


    def abouth_menu(self)->None:
        st.markdown("")
        st.markdown("")
        st.markdown("")
        st.markdown("")
        
        
        
        Note_Mid = st.columns([1,3,1])
        
        with Note_Mid[1]:
            st.subheader("Application Guide")
            with st.container(width=1000,border=True):
                
                # TODO (Tasks) Expander
                with st.expander("📌 TODO Tasks", expanded=True):
                    st.markdown("""
                **What can you do with TODO tasks?**

                - **Add tasks:** Use the **'Add'** button to create new tasks.  
                - **List tasks:** View all your added tasks in the list.  
                - **Edit tasks:** Use the **'Edit'** button to modify task details.  
                - **Delete tasks:** Use the **'Delete'** button to remove tasks you no longer need.  
                """)

                # Books / Library Expander
                with st.expander("📚 Books & Library"):
                    st.markdown("""
                **What can you do with books?**

                - **Add new books:** Fill in the title, author, pages, and date, then click **'Add'**.  
                - **Update books:** Click **'Edit'** to change book details.  
                - **Search & Filter:** Use search or filter options to find books quickly.  
                - **Add comments:** Write and submit comments under each book.  
                - **Add to favorites:** Mark books as favorites to access them easily later.  
                """)

                # Users / General Expander
                with st.expander("👤 Users & General Operations"):
                    st.markdown("""
                **What can you do with users & general operations?**

                - **Add new users:** Use the **'Add User'** form in the admin panel.  
                - **Update user info:** Click **'Edit'** in the user list to modify user information.  
                - **Data safety:** All information is stored in the database (SQLite), ensuring your data remains safe even if the app is closed.  
                """)


if __name__ =="__main__":
    index_page = Index()
    index_page.menu()
    index_page.books_menu()
    index_page.abouth_menu()