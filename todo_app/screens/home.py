import streamlit as st
from sidebar.info import info
from sidebar.lists import create_new_list, delete_list, show_lists, sidebar_selected_list, show_selected_list
from sidebar.folders import create_folder, delete_folder, show_folders_sidebar, manage_list_folder

def home():
    if st.session_state.active_list:
        info()
        sidebar_selected_list(st.session_state.active_list)
        show_selected_list()
    else:
        info()
        create_new_list()
        delete_list()
        create_folder()
        manage_list_folder()
        delete_folder()
        show_folders_sidebar()
        show_lists()