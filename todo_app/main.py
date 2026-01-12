import streamlit as st
from todo_app.config import init_session_state
from todo_app.screens.welcome import welcome_screen
from todo_app.screens.home import home

st.set_page_config(layout="wide")
init_session_state()

def main():
    if st.session_state.vista == "welcome":
        welcome_screen()
    elif st.session_state.vista == "home":
        home()
