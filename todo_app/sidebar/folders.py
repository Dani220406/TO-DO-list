import streamlit as st


# Method to create a list to put lists in
def create_folder():
    st.sidebar.markdown("---")
    with st.sidebar.popover("📁 Create New Folder", use_container_width=True):
        with st.form(key="form_crea_cartella", clear_on_submit=True):
            nome_cartella = st.text_input("Folder Name")
            submit = st.form_submit_button("Create Folder")

            if submit:
                if not nome_cartella:
                    st.error("The name of the folder cannot be empty.")
                    return

                if nome_cartella in st.session_state.folders:
                    st.warning("A folder with this name already exists.")
                    return

                st.session_state.folders.append(nome_cartella)
                st.success(f"Folder '{nome_cartella}' created")
                st.rerun()


# -------------------------------------------------------------


# Method to show created folders in sidebar
def show_folders_sidebar():
    st.sidebar.markdown("---")
    if not st.session_state.folders:
        return

    st.sidebar.subheader("📂 My Folders")
    for folder in st.session_state.folders:
        with st.sidebar.expander(f"{folder}", expanded=False):
            liste_nella_cartella = [
                t for t in st.session_state.my_lists if t.get("cartella") == folder
            ]
            if not liste_nella_cartella:
                st.caption("The folder is empty.")
            else:
                for t in liste_nella_cartella:
                    if st.button(
                        t["nome"],
                        key=f"open_{folder}_{t['nome']}",
                        use_container_width=True,
                    ):
                        st.session_state.active_list = t["nome"]
                        st.rerun()


# -------------------------------------------------------------


# Method to manage lists in folders
def manage_list_folder():
    if not st.session_state.my_lists or not st.session_state.folders:
        return

    with st.sidebar.popover("🗂️ Manage Folders", use_container_width=True):
        with st.form(key="form_manage_list_folder"):
            lista_nome = st.selectbox(
                "Lista", [t["nome"] for t in st.session_state.my_lists]
            )
            cartella_corrente = next(
                (
                    t.get("cartella")
                    for t in st.session_state.my_lists
                    if t["nome"] == lista_nome
                ),
                None,
            )
            cartelle_opzioni = ["— None —"] + st.session_state.folders
            selezione = st.selectbox(
                "Folder",
                cartelle_opzioni,
                index=(
                    cartelle_opzioni.index(cartella_corrente)
                    if cartella_corrente in cartelle_opzioni
                    else 0
                ),
                key="manage_folder_select",
            )
            submit = st.form_submit_button("Move List")

            if submit:
                for t in st.session_state.my_lists:
                    if t["nome"] == lista_nome:
                        t["cartella"] = None if selezione == "— None —" else selezione
                        break
                st.rerun()


# -------------------------------------------------------------


# Method to delete a folder
def delete_folder():
    if not st.session_state.folders:
        return

    with st.sidebar.popover("🗑️ Delete Folder", use_container_width=True):
        cartella = st.selectbox(
            "Select Folder", st.session_state.folders, key="delete_folder_select"
        )
        st.warning("Lists within this folder will not be deleted.")
        if st.button("Delete Folder", use_container_width=True):
            st.session_state.folders.remove(cartella)

            for t in st.session_state.my_lists:
                if t.get("cartella") == cartella:
                    t["cartella"] = None

            st.success(f"Folder '{cartella}' deleted")
            st.rerun()
