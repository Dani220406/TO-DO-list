import streamlit as st
import time

# Setting del programma alla partenza
st.set_page_config(layout="wide")

if "vista" not in st.session_state:
    st.session_state.vista = "welcome"

if "my_lists" not in st.session_state:
    st.session_state.my_lists = []

if "active_list" not in st.session_state:
    st.session_state.active_list = None

# -------------------------------------------------------------

# Funzione che da il benvenuto all'utente
def welcome_screen():
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

# -------------------------------------------------------------

# Placeholder per funzione "IMPOSTAZIONI"

# -------------------------------------------------------------

# Funzione per creare una nuova lista
def create_new_list():
    st.sidebar.subheader("➕ Crea nuova lista")
    nome = st.sidebar.text_input("Nome lista")

    if st.sidebar.button("Conferma"): # <---- Fare che se lista ha stesso nome di un'altra -> Messaggio: scegliere nome diverso
        if nome:
            st.session_state.my_lists.append({"nome": nome, "dati": []})
            st.rerun()

# -------------------------------------------------------------

# Placeholder per funzione "CANCELLAZIONE LISTA"

# -------------------------------------------------------------

# Placeholder per funzione "ORDINA LISTE" [Maybe]
# - Capacità di ordinare le liste semplicemente tenendo premuto su una lista e spostando il cursore

# -------------------------------------------------------------

# Placeholder per funzione "CREA CARTELLA" [Maybe]
# - Capacità di creare cartelle contenenti un insieme di liste create

# -------------------------------------------------------------

# Sidebar una volta selezionata una lista da guardare
def sidebar_selected_list(nome):
    st.sidebar.subheader(f"Modifica lista: {nome}")
    if st.sidebar.button("⬅️ Torna alle liste"):  #  <----- fare che quando si preme questo, la lista viene automaticamente salvata
        st.session_state.active_list = None
        st.rerun()
    st.sidebar.button("➕ Aggiungi elemento") # <----- Implementare "Aggiungi Elemento"
    st.sidebar.button("❌ Elimina elemento") #  <----- Implementare "Elimina Elemento"
    st.sidebar.button("✅ Task Completato") #  <------ Implementare "Segnare un elemento della lista come completato"
    st.sidebar.button("🏷️ Etichetta")      # <-------- Implementare "Sistema di Etichette"
    st.sidebar.button("📥 Scarica Lista") # <------ Implementare "Scaricare lista selezionata in una cartella"

# -------------------------------------------------------------

# Placeholder per funzione "AGGIUNGI ELEMENTO"

# -------------------------------------------------------------

# Placeholder per funzione "ELIMINA ELEMENTO"

# -------------------------------------------------------------

# Placeholder per funzione "TASK COMPLETATO"

# -------------------------------------------------------------

# Placeholder per funzione "ETICHETTA"

# -------------------------------------------------------------

# Placeholder per funzione "SCARICA LISTA"

# -------------------------------------------------------------

# Mostrare tutte le liste nella homepage
def show_lists():
    liste = st.session_state.my_lists
    if not liste:
        st.info("Non hai ancora creato nessuna lista")
        return

    CARDS_PER_ROW = 4 # Num. Liste mostrate per riga nella homepage
    # Potremmo anche mettere un'impostazione che permetta di gestire manualmente il numero di liste per riga

    for i in range(0, len(liste), CARDS_PER_ROW):
        row = liste[i:i + CARDS_PER_ROW]
        cols = st.columns(len(row))

        for col, lista in zip(cols, row):
            with col:
                if st.button(f"{lista['nome']}", key=f"open_{lista['nome']}", use_container_width=True):
                    st.session_state.active_list = lista["nome"]
                    st.rerun()

# -------------------------------------------------------------

# Mostrare lista selezionata
def show_selected_list():
    nome = st.session_state.active_list
    st.markdown(f"## {nome}")
    st.markdown("---")
    lista = next((l for l in st.session_state.my_lists if l["nome"] == nome), None)
    if lista:
        if lista["dati"]:
            for idx, item in enumerate(lista["dati"], 1):
                st.write(f"{idx}. {item}")
        else:
            st.info("Lista vuota, aggiungi un nuovo elemento.")

# -------------------------------------------------------------

# Gestione della Homepage
def home():
    if st.session_state.active_list:
        sidebar_selected_list(st.session_state.active_list)
        show_selected_list()
    else:
        create_new_list()
        show_lists()

# -------------------------------------------------------------

# MAIN
def main():
    if st.session_state.vista == "welcome":
        welcome_screen()
    elif st.session_state.vista == "home":
        home()

if __name__ == "__main__":
    main()