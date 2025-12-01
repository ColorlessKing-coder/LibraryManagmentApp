import streamlit as st
import hashlib
import re
from Database.users_database import UserDatabase

class Login:
    def __init__(self):
        st.set_page_config(page_icon="images/app.ico",page_title="Next Generation Library APP",layout="centered")
        self.database = UserDatabase()
    

    def login_form(self):
        with st.container(horizontal=True,horizontal_alignment="center"):
            
            st.image("images/sign_up.png",width=500)
       
        with st.form(key="logup_up_form"):
            user_name = st.text_input("Username:")
            surname = st.text_input("Surname:")
            password = st.text_input("Password:", type="password")
            email = st.text_input("Email:")
            date = st.date_input("Date:")
            role = st.selectbox("Role", ["Stuff", "Member", "Admin"])
            submit_button = st.form_submit_button("Sign Up",width="stretch",type="primary")
            
            if submit_button:
                if len(password) < 8:
                    st.error("Password must be at least 8 characters")
                    return
                if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
                    st.error("Invalid email")
                    return
                try:
                    if role.lower() == "admin": 
                        self.database.create_admin_table()
                        self.database.add_admin_to_table(user_name,surname,password,email,date,role)
                        st.success("Admin Account created successfully!")
                    
                    elif role.lower() == "stuff":
                        self.database.create_stuff_table()
                        self.database.add_stuff_to_table(user_name,surname,password,email,date,role)
                        st.success("Stuff Account created successfully!") 
                    
                    elif role.lower()=="member":
                        self.database.create_member_table()
                        self.database.add_member_to_table(user_name,surname,password,email,date,role)
                        st.success("Member Account created successfully!") 
                    else:
                        st.error("Please Enter Role")
                        return
                except Exception as e:
                    st.error(f"Error : Something went wrong while creating the account. ")


if __name__ == "__main__":
    login = Login()
    login.login_form()
