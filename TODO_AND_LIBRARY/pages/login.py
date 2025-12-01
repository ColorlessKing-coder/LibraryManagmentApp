import streamlit as st
from Database.users_database import UserDatabase
import time


class Login:
    def __init__(self):
        st.set_page_config(
            page_icon="images/app.ico",
            page_title="Next Generation Library APP",
            layout="centered"
        )
        self.database = UserDatabase()

    def login_form(self):
        with st.container(horizontal=True,horizontal_alignment="center"):
            st.image("images/login.png",width=500)
        with st.form(key="login_in_form"):
            user_name = st.text_input("Kullanıcı Adı:")
            password = st.text_input("Şifre:", type="password")
            role = st.selectbox("Role",["Admin","Stuff","Member"])

            submit_button = st.form_submit_button("Giriş Yap")

            if submit_button:

                
                if "USER" not in st.session_state:
                    st.session_state["USER"] = None

                if "ROLE" not in st.session_state:
                    st.session_state["ROLE"] = ""

                if role.lower() == "admin":
                    role = role.lower()
                
                if role.lower() == "stuff":
                    role = role.lower()
                
                if role.lower() == "member":
                    role = role.lower()
                
                user = self.database.check_all_auth(role,user_name, password)
                st.info(user)

            
                if isinstance(user, tuple):
                    user_role = user[-1].lower()
                    st.session_state["USER"] = user
                    st.session_state["ROLE"] = user_role
                    st.success("Giriş Başarılı!")
                    time.sleep(3)
                    

                    st.rerun()       # → Sadece bu! Başka hiçbir yönlendirme yok!
                else:
                    st.error("Kullanıcı bulunamadı. Lütfen önce kayıt olun.")
                    st.session_state["ROLE"] = "guest"
                    time.sleep(1)
                    st.switch_page("pages/logup.py")


                   


if __name__ == "__main__":
    login = Login()
    login.login_form()
