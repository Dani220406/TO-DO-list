import streamlit as st
import time

st.set_page_config(layout="wide") #Per organizzare agevolmente il layout della home page

if "vista" not in st.session_state:
    st.session_state.vista = "welcome"

if "my_lists" not in st.session_state:
    st.session_state.my_lists = []

if "active_list" not in st.session_state:
    st.session_state.active_list = None

#Funzione per dare il benvenuto all'utente all'apertura dell'app
def welcome_screen():
    col1, col2, col3 = st.columns([1, 6, 1]) #Per posizionare la scritta al centro dello schermo
    with col2:
        st.markdown(
            """
            <div style="text-align:center; padding-top:30vh;">
                <h1>Benvenuto</h1>
                <h3>Quali sono i tuoi piani per oggi?</h3>
            </div>
            """,
            unsafe_allow_html=True
        )
    time.sleep(3)
    st.session_state.vista = "home"
    st.rerun()

#Funzione per creare una nuova lista
def new_list():
    st.subheader("Crea lista")
    nome = st.text_input("Nome lista")

    if st.button("Crea lista"):
        if nome:
            st.session_state.my_lists.append(
                {"nome": nome, "dati": []}
            )
            st.rerun()

#Funzione per mostrare le liste create
def show_lists_grid():
    liste = st.session_state.my_lists
    if not liste:
        st.info("Non hai ancora creato nessuna lista")
        return

    CARDS_PER_ROW = 4 #dopo 4 liste create, va a capo

    for i in range(0, len(liste), CARDS_PER_ROW):
        row = liste[i:i + CARDS_PER_ROW]
        cols = st.columns(len(row))

        for col, lista in zip(cols, row):
            with col:
                if st.button(
                    f"{lista['nome']}",
                    key=f"open_{lista['nome']}",
                    use_container_width=True
                ):
                    st.session_state.active_list = lista["nome"]
                    st.rerun()

#Funzione per mostrare una lista selezionata
def show_active_list():
    nome = st.session_state.active_list

    st.markdown(f"## {nome}")
    st.markdown("---")

    if st.button("⬅ Torna alle liste"):
        st.session_state.active_list = None
        st.rerun()

#Funzione per gestire la homepage
def home():
    col1, col2, col3 = st.columns([1, 5, 2])

    with col1:
        new_list()

    with col2:
        if st.session_state.active_list:
            show_active_list()
        else:
            show_lists_grid()

    with col3:
        pass

#MAIN
def main():
    if st.session_state.vista == "welcome":
        welcome_screen()
    elif st.session_state.vista == "home":
        home()

if __name__ == "__main__":
    main()