import streamlit as st
from sidebar.elements import add_element, remove_element, mark_task_done, edit_style, edit_text, reorder_elements

# Funzione per creare una nuova lista
def create_new_list():
    with st.sidebar.popover("➕ Nuova lista", use_container_width=True):
        with st.form(key="form_crea_lista", clear_on_submit=True):
            nome = st.text_input("Nome lista")
            submit = st.form_submit_button("Crea Lista")

            if submit:
                if not nome:
                    st.error("Il nome della lista non può essere vuoto")
                    return

                nomi_esistenti = [l["nome"] for l in st.session_state.my_lists]

                if nome in nomi_esistenti:
                    st.warning("Esiste già una lista con questo nome.")
                else:
                    st.session_state.my_lists.append({"nome": nome, "dati": [], "cartella": None})
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
            lista_da_eliminare = st.selectbox("Seleziona lista", nomi_liste, key="delete_list_select")
            submit = st.form_submit_button("Elimina Lista")

            if submit:
                st.session_state.my_lists = [l for l in st.session_state.my_lists if l["nome"] != lista_da_eliminare]
                st.success(f"Lista '{lista_da_eliminare}' eliminata")
                st.rerun()

# -------------------------------------------------------------

# Funzione per mostrare tutte le liste nella homepage
def show_lists():
    liste = st.session_state.my_lists
    if not liste:
        st.info("Non hai ancora creato nessuna lista")
        return

    CARDS_PER_ROW = 4
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
                st.markdown(f"{idx}. {item}")
        else:
            st.info("Lista vuota, aggiungi un nuovo elemento.")

# -------------------------------------------------------------

# Sidebar una volta selezionata una lista da guardare
def sidebar_selected_list(nome):
    if st.sidebar.button("⬅️ Torna alla Homepage"):
        st.session_state.active_list = None
        st.rerun()
    add_element()
    edit_text()
    remove_element()
    reorder_elements()
    mark_task_done()
    st.sidebar.button("🏷️ Etichetta")      # <-------- Implementare "Sistema di Etichette"
    edit_style()