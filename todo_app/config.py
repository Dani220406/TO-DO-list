import streamlit as st

def init_session_state():
    if "vista" not in st.session_state:
        st.session_state.vista = "welcome"

    if "my_lists" not in st.session_state:
        st.session_state.my_lists = []

    if "active_list" not in st.session_state:
        st.session_state.active_list = None

    if "folders" not in st.session_state:
        st.session_state.folders = []
