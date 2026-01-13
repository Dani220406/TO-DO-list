import streamlit as st
import time


def welcome_screen():
    st.markdown(
        """
        <div style="text-align:center; padding-top:30vh;">
            <h1>Benvenuto</h1>
            <h3>Quali sono i tuoi piani per oggi?</h3>
        </div>
        """,
        unsafe_allow_html=True,
    )
    time.sleep(3)  # Per simulare il caricamento dell'app
    st.session_state.vista = "home"
    st.rerun()
