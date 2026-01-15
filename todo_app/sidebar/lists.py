import streamlit as st
from todo_app.sidebar.elements import (
    add_element,
    remove_element,
    mark_task_done,
    edit_style,
    edit_text,
    reorder_elements,
    priority_element,
)


# Method to Create a new List
def create_new_list():
    with st.sidebar.popover("➕ Create New List", use_container_width=True):
        with st.form(key="form_crea_lista", clear_on_submit=True):
            nome = st.text_input("List Name")
            submit = st.form_submit_button("Create List")

            if submit:
                if not nome:
                    st.error("The name of the list cannot be empty.")
                    return

                nomi_esistenti = [t["nome"] for t in st.session_state.my_lists]

                if nome in nomi_esistenti:
                    st.warning("A list with this name already exists.")
                else:
                    st.session_state.my_lists.append(
                        {"nome": nome, "dati": [], "cartella": None}
                    )
                    st.rerun()


# -------------------------------------------------------------


# Method to Delete a List
def delete_list():
    if not st.session_state.my_lists:
        return

    with st.sidebar.popover("🗑️ Delete List", use_container_width=True):
        with st.form(key="form_elimina_lista"):
            nomi_liste = [t["nome"] for t in st.session_state.my_lists]
            lista_da_eliminare = st.selectbox(
                "Select List", nomi_liste, key="delete_list_select"
            )
            submit = st.form_submit_button("Delete List")

            if submit:
                st.session_state.my_lists = [
                    t
                    for t in st.session_state.my_lists
                    if t["nome"] != lista_da_eliminare
                ]
                st.success(f"List '{lista_da_eliminare}' deleted")
                st.rerun()


# -------------------------------------------------------------


# Method to show all lists in the homepage
def show_lists():
    liste = st.session_state.my_lists
    if not liste:
        st.info("No list was yet created.")
        return

    CARDS_PER_ROW = 4
    for i in range(0, len(liste), CARDS_PER_ROW):
        row = liste[i : i + CARDS_PER_ROW]
        cols = st.columns(len(row))

        for col, lista in zip(cols, row):
            with col:
                if st.button(
                    f"{lista['nome']}",
                    key=f"open_{lista['nome']}",
                    use_container_width=True,
                ):
                    st.session_state.active_list = lista["nome"]
                    st.rerun()


# -------------------------------------------------------------


# Method to open the selected list
def show_selected_list():
    nome = st.session_state.active_list
    st.markdown(f"## {nome}")
    st.markdown("---")
    lista = next((t for t in st.session_state.my_lists if t["nome"] == nome), None)
    if lista:
        if lista["dati"]:
            for idx, item in enumerate(lista["dati"], 1):
                st.markdown(f"{idx}. {item}")
        else:
            st.info("The list is empty, add a new element.")


# -------------------------------------------------------------


# Sidebar after having opened a list
def sidebar_selected_list(nome):
    if st.sidebar.button("⬅️ Back to Homepage"):
        st.session_state.active_list = None
        st.rerun()
    add_element()
    edit_text()
    remove_element()
    reorder_elements()
    mark_task_done()
    priority_element()
    edit_style()
