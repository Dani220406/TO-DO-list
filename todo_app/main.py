import streamlit as st
from config import init_session_state
from screens.welcome import welcome_screen
from screens.home import home

st.set_page_config(layout="wide")
init_session_state()

def main():
    if st.session_state.vista == "welcome":
        welcome_screen()
    elif st.session_state.vista == "home":
        home()

if __name__ == "__main__":
    main()