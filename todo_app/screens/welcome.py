import streamlit as st
import time


def welcome_screen():
    st.markdown(
        """
        <div style="text-align:center; padding-top:30vh;">
            <h1>Welcome</h1>
            <h3>What are your plans for today?</h3>
        </div>
        """,
        unsafe_allow_html=True,
    )
    time.sleep(3)  # To simulate the app's loading
    st.session_state.vista = "home"
    st.rerun()
