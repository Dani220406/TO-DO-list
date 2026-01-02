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

if "folders" not in st.session_state:
    st.session_state.folders = []

# -------------------------------------------------------------

# Funzione che da' il benvenuto all'utente
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
    time.sleep(3)  # Per simulare il caricamento dell'app
    st.session_state.vista = "home"
    st.rerun()

# -------------------------------------------------------------

# Funzione per creare una nuova lista
def create_new_list():
    st.sidebar.subheader("➕ Crea nuova lista")
    nome = st.sidebar.text_input("Nome lista")

    if st.sidebar.button("✔️ Crea lista"):
        if not nome:
            st.sidebar.error("Il nome della lista non può essere vuoto")
            return

        nomi_esistenti = [l["nome"] for l in st.session_state.my_lists]

        if nome in nomi_esistenti:
            st.sidebar.warning("Esiste già una lista con questo nome.")
        else:
            st.session_state.my_lists.append({"nome": nome, "dati": [], "cartella": None})
            st.rerun()

# -------------------------------------------------------------

# Funzione per cancellare una lista
def delete_list():
    st.sidebar.subheader("🗑️ Elimina lista")

    if not st.session_state.my_lists:
        st.sidebar.info("Nessuna lista da eliminare")
        return

    nomi_liste = [l["nome"] for l in st.session_state.my_lists]
    lista_da_eliminare = st.sidebar.selectbox("Seleziona lista", nomi_liste, key="delete_list_select")

    if st.sidebar.button("❌ Elimina lista"):
            st.session_state.my_lists = [
                l for l in st.session_state.my_lists
                if l["nome"] != lista_da_eliminare
            ]
            st.sidebar.success(f"Lista '{lista_da_eliminare}' eliminata")
            st.rerun()

# -------------------------------------------------------------

# Funzione per creare una cartella in cui inserire liste
def create_folder():
    st.sidebar.markdown("---")
    st.sidebar.subheader("📁 Crea nuova cartella")

    nome_cartella = st.sidebar.text_input("Nome cartella")

    if st.sidebar.button("✔️ Crea cartella"):
        if not nome_cartella:
            st.sidebar.error("Il nome della cartella non può essere vuoto.")
            return

        if nome_cartella in st.session_state.folders:
            st.sidebar.warning("Esiste già una cartella con questo nome.")
            return

        st.session_state.folders.append(nome_cartella)
        st.rerun()

# -------------------------------------------------------------

# Funzione per mostrare le cartelle create nella sidebar
def show_folders_sidebar():
    if not st.session_state.folders:
        return

    st.sidebar.subheader("📂 Le mie Cartelle")

    for folder in st.session_state.folders:
        with st.sidebar.expander(f"{folder}", expanded=False):
            liste_nella_cartella = [
                l for l in st.session_state.my_lists
                if l.get("cartella") == folder
            ]

            if not liste_nella_cartella:
                st.caption("Nessuna lista")
            else:
                for l in liste_nella_cartella:
                    if st.button(
                        l["nome"],
                        key=f"open_{folder}_{l['nome']}",
                        use_container_width=True
                    ):
                        st.session_state.active_list = l["nome"]
                        st.rerun()

# -------------------------------------------------------------

# Funzione per gestire le liste nelle cartelle
def manage_list_folder():
    if not st.session_state.my_lists or not st.session_state.folders:
        return

    st.sidebar.subheader("🗂️ Gestione cartelle")

    lista_nome = st.sidebar.selectbox(
        "Lista",
        [l["nome"] for l in st.session_state.my_lists],
        key="manage_list_folder_list"
    )

    cartella_corrente = next(
        (l.get("cartella") for l in st.session_state.my_lists if l["nome"] == lista_nome),
        None
    )

    cartelle_opzioni = ["— Nessuna —"] + st.session_state.folders
    selezione = st.sidebar.selectbox(
        "Cartella",
        cartelle_opzioni,
        index=cartelle_opzioni.index(cartella_corrente)
        if cartella_corrente in cartelle_opzioni else 0,
        key="manage_list_folder_select"
    )

    if st.sidebar.button("🔄 Sposta Lista"):
        for l in st.session_state.my_lists:
            if l["nome"] == lista_nome:
                l["cartella"] = None if selezione == "— Nessuna —" else selezione
        st.rerun()

# ----------------------------------------------------

# Funzione per cancellare una cartella
def delete_folder():
    if not st.session_state.folders:
        return

    st.sidebar.subheader("🗑️ Elimina cartella")

    cartella = st.sidebar.selectbox(
        "Seleziona cartella",
        st.session_state.folders,
        key="delete_folder_select"
    )

    if st.sidebar.button("❌ Elimina cartella"):
        st.session_state.folders.remove(cartella)

        for l in st.session_state.my_lists:
            if l.get("cartella") == cartella:
                l["cartella"] = None

        st.sidebar.success(f"Cartella '{cartella}' eliminata")
        st.rerun()

# ------------------------------------------------------

# Sidebar una volta selezionata una lista da guardare
def sidebar_selected_list(nome):
    st.sidebar.subheader(f"Modifica lista: {nome}")
    if st.sidebar.button("⬅️ Torna alle liste"):
        st.session_state.active_list = None
        st.rerun()
    add_element()
    remove_element()
    st.sidebar.button("✅ Task Completato") #  <------ Implementare "Segnare un elemento della lista come completato"
    st.sidebar.button("🏷️ Etichetta")      # <-------- Implementare "Sistema di Etichette"

# -------------------------------------------------------------

# Funzione per aggiungere un elemento alla lista selezionata
def add_element():
    nome_lista = st.session_state.active_list
    lista = next((l for l in st.session_state.my_lists if l["nome"] == nome_lista), None)

    if lista is not None:
        # Il popover sostituisce il bottone e contiene il form in modo stabile
        with st.sidebar.popover("➕ Aggiungi elemento", use_container_width=True):
            with st.form(key="form_aggiunta", clear_on_submit=True):
                nuovo_item = st.text_input("Cosa vuoi aggiungere?")
                submit = st.form_submit_button("Conferma")
                
                if submit:
                    if nuovo_item:
                        lista["dati"].append(nuovo_item)
                        st.rerun()
                    else:
                        st.error("Nessun elemento inserito.")
       
# -------------------------------------------------------------

# Placeholder per funzione "ELIMINA ELEMENTO"
def remove_element():
    nome_lista = st.session_state.active_list
    lista = next((l for l in st.session_state.my_lists if l["nome"] == nome_lista),None)

    if lista and lista["dati"]:
        st.sidebar.subheader("❌ Rimuovi elemento")

        # Lista delle opzioni numerate
        options = [f"{idx+1}. {item}" for idx, item in enumerate(lista["dati"])]

        # Selectbox per scegliere l'elemento da rimuovere
        elemento_da_rimuovere = st.sidebar.selectbox("Seleziona elemento da rimuovere", options)
        
        # Bottone per rimuovere l'elemento selezionato
        if st.sidebar.button("Rimuovi elemento", key="remove_element_button"):
            idx = int(elemento_da_rimuovere.split(".")[0]) - 1  # calcola indice
            rimosso = lista["dati"].pop(idx)
            st.success(f"Elemento '{rimosso}' rimosso!")
            st.rerun()
    else:
        st.sidebar.info("La lista è vuota, niente da rimuovere.")

# -------------------------------------------------------------

# Placeholder per funzione "TASK COMPLETATO"

# -------------------------------------------------------------

# Placeholder per funzione "ETICHETTA"

# -------------------------------------------------------------

# Funzione per mostrare tutte le liste nella homepage
def show_lists():
    liste = st.session_state.my_lists
    if not liste:
        st.info("Non hai ancora creato nessuna lista")
        return

    CARDS_PER_ROW = 4 # Num. Liste mostrate per riga nella homepage

    for i in range(0, len(liste), CARDS_PER_ROW):
        row = liste[i:i + CARDS_PER_ROW]
        cols = st.columns(len(row))

        for col, lista in zip(cols, row):
            with col:
                if st.button(f"{lista['nome']}", key=f"open_{lista['nome']}", use_container_width=True):
                    st.session_state.active_list = lista["nome"]
                    st.rerun()

# -------------------------------------------------------------

# Funzione per mostrare una lista selezionata
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

# Gestione della Homepage (invocazione funzioni)
def home():
    if st.session_state.active_list:
        sidebar_selected_list(st.session_state.active_list)
        show_selected_list()
    else:
        create_new_list()
        delete_list()
        create_folder()
        show_folders_sidebar()
        manage_list_folder()
        delete_folder()
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