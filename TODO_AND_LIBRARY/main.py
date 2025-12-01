import streamlit as st
from streamlit_option_menu import option_menu



class Index:
    def __init__(self) -> None:
        st.set_page_config(page_title=" Next Generation Library APP",page_icon="images/app.ico")

        
        


    
    def before_session(self):
        with st.sidebar:    
            
            pages = [ st.Page("pages/login.py",title="Sign In",icon=":material/login:"),
                      st.Page("pages/logup.py",title="Sign Up",icon=":material/person_add:"),
                      st.Page("pages/index.py",title="Home",icon=":material/home:") ]
           
            
            if st.session_state.get("ROLE") == "admin":
                pages.append(st.Page("pages/admin.py", title="Admin Panel", icon=":material/passkey:"))

            
            if st.session_state.get("ROLE") == "stuff":
                pages.append(st.Page("pages/stuff.py", title="Stuff Panel", icon=":material/admin_panel_settings:"))

            if st.session_state.get("ROLE") == "member":
                pages.append(st.Page("pages/member.py", title="Stuff Panel", icon=":material/attribution:"))


        pg = st.navigation(pages)
        pg.run()             

   

    
            
            

if __name__ == "__main__":
    app = Index()
    app.before_session()
    
    