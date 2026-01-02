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
    with st.sidebar.popover("➕ Nuova lista", use_container_width=True):
        with st.form(key="form_crea_lista", clear_on_submit=True):
            nome = st.text_input("Nome lista")
            submit = st.form_submit_button("✔️ Crea lista")

            if submit:
                if not nome:
                    st.error("Il nome della lista non può essere vuoto")
                    return

                nomi_esistenti = [l["nome"] for l in st.session_state.my_lists]

                if nome in nomi_esistenti:
                    st.warning("Esiste già una lista con questo nome.")
                else:
                    st.session_state.my_lists.append(
                        {"nome": nome, "dati": [], "cartella": None}
                    )
                    st.rerun()

# -------------------------------------------------------------

# Funzione per cancellare una lista
def delete_list():
    if not st.session_state.my_lists:
        st.sidebar.info("Nessuna lista da eliminare")
        return

    with st.sidebar.popover("🗑️ Elimina lista", use_container_width=True):
        with st.form(key="form_elimina_lista"):
            nomi_liste = [l["nome"] for l in st.session_state.my_lists]
            lista_da_eliminare = st.selectbox(
                "Seleziona lista",
                nomi_liste,
                key="delete_list_select"
            )

            submit = st.form_submit_button("❌ Elimina definitivamente")

            if submit:
                st.session_state.my_lists = [
                    l for l in st.session_state.my_lists
                    if l["nome"] != lista_da_eliminare
                ]
                st.success(f"Lista '{lista_da_eliminare}' eliminata")
                st.rerun()

# -------------------------------------------------------------

# Funzione per creare una cartella in cui inserire liste
def create_folder():
    st.sidebar.markdown("---")

    with st.sidebar.popover("📁 Crea nuova cartella", use_container_width=True):
        with st.form(key="form_crea_cartella", clear_on_submit=True):
            nome_cartella = st.text_input("Nome cartella")
            submit = st.form_submit_button("✔️ Crea cartella")

            if submit:
                if not nome_cartella:
                    st.error("Il nome della cartella non può essere vuoto.")
                    return

                if nome_cartella in st.session_state.folders:
                    st.warning("Esiste già una cartella con questo nome.")
                    return

                st.session_state.folders.append(nome_cartella)
                st.success(f"Cartella '{nome_cartella}' creata")
                st.rerun()

# -------------------------------------------------------------

# Funzione per mostrare le cartelle create nella sidebar
def show_folders_sidebar():
    st.sidebar.markdown("---")
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

    with st.sidebar.popover("🗂️ Gestisci cartelle", use_container_width=True):
        with st.form(key="form_manage_list_folder"):
            lista_nome = st.selectbox(
                "Lista",
                [l["nome"] for l in st.session_state.my_lists]
            )

            cartella_corrente = next(
                (l.get("cartella") for l in st.session_state.my_lists if l["nome"] == lista_nome),
                None
            )

            cartelle_opzioni = ["— Nessuna —"] + st.session_state.folders

            selezione = st.selectbox(
                "Cartella",
                cartelle_opzioni,
                index=cartelle_opzioni.index(cartella_corrente)
                if cartella_corrente in cartelle_opzioni else 0
            )

            submit = st.form_submit_button("🔄 Sposta lista")

            if submit:
                for l in st.session_state.my_lists:
                    if l["nome"] == lista_nome:
                        l["cartella"] = None if selezione == "— Nessuna —" else selezione
                        break
                st.rerun()

# ----------------------------------------------------

# Funzione per cancellare una cartella
def delete_folder():
    if not st.session_state.folders:
        return

    with st.sidebar.popover("🗑️ Elimina cartella", use_container_width=True):
        cartella = st.selectbox(
            "Seleziona cartella",
            st.session_state.folders,
            key="delete_folder_select"
        )

        st.warning("⚠️ Le liste contenute nella cartella non verranno eliminate")

        if st.button("❌ Elimina cartella", use_container_width=True):
            st.session_state.folders.remove(cartella)

            for l in st.session_state.my_lists:
                if l.get("cartella") == cartella:
                    l["cartella"] = None

            st.success(f"Cartella '{cartella}' eliminata")
            st.rerun()

# ------------------------------------------------------

# Sidebar una volta selezionata una lista da guardare
def sidebar_selected_list(nome):
    if st.sidebar.button("⬅️ Torna alle liste"):
        st.session_state.active_list = None
        st.rerun()
    add_element()
    remove_element()
    mark_task_done()
    st.sidebar.button("🏷️ Etichetta")      # <-------- Implementare "Sistema di Etichette"

# -------------------------------------------------------------

# Funzione per aggiungere un elemento alla lista selezionata
def add_element():
    st.sidebar.markdown("---")
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

# Funzione che rimuove un elemento dalla lista
def remove_element():
    nome_lista = st.session_state.active_list
    lista = next((l for l in st.session_state.my_lists if l["nome"] == nome_lista), None)

    if lista and lista["dati"]:
        with st.sidebar.popover("❌ Rimuovi elemento", use_container_width=True):
            with st.form(key="form_rimozione", clear_on_submit=True):
                options = [f"{idx+1}. {item}" for idx, item in enumerate(lista["dati"])]
                elemento_da_rimuovere = st.selectbox(
                    "Seleziona elemento da rimuovere",
                    options
                )

                submit = st.form_submit_button("Rimuovi")

                if submit:
                    idx = int(elemento_da_rimuovere.split(".")[0]) - 1
                    lista["dati"].pop(idx)
                    st.rerun()
    else:
        st.sidebar.info("Lista vuota, niente da rimuovere.")

# -------------------------------------------------------------

# Funzione che segna un elemento della lista come completato
def mark_task_done():
    nome_lista = st.session_state.active_list
    lista = next((l for l in st.session_state.my_lists if l["nome"] == nome_lista), None)

    if lista and lista["dati"]:
        with st.sidebar.popover("✅ Segna task completato", use_container_width=True):
            with st.form(key="form_mark_done", clear_on_submit=True):
                options = [f"{idx+1}. {item}" for idx, item in enumerate(lista["dati"])]
                task_selezionato = st.selectbox(
                    "Seleziona task",
                    options
                )

                submit = st.form_submit_button("Conferma")

                if submit:
                    idx = int(task_selezionato.split(".")[0]) - 1
                    task = lista["dati"][idx]

                    # Toggle completato / non completato
                    if task.startswith("✔️"):
                        lista["dati"][idx] = task.replace("✔️ ", "", 1)
                    else:
                        lista["dati"][idx] = "✔️ " + task

                    st.rerun()
    else:
        st.sidebar.info("Lista vuota, niente da completare.")

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
        manage_list_folder()
        delete_folder()
        show_folders_sidebar()
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