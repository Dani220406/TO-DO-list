import streamlit as st


# Funzione per creare una cartella in cui inserire liste
def create_folder():
    st.sidebar.markdown("---")
    with st.sidebar.popover("📁 Crea nuova cartella", use_container_width=True):
        with st.form(key="form_crea_cartella", clear_on_submit=True):
            nome_cartella = st.text_input("Nome cartella")
            submit = st.form_submit_button("Crea Cartella")

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
                t for t in st.session_state.my_lists if t.get("cartella") == folder
            ]
            if not liste_nella_cartella:
                st.caption("Nessuna lista")
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


# Funzione per gestire le liste nelle cartelle
def manage_list_folder():
    if not st.session_state.my_lists or not st.session_state.folders:
        return

    with st.sidebar.popover("🗂️ Gestisci cartelle", use_container_width=True):
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
            cartelle_opzioni = ["— Nessuna —"] + st.session_state.folders
            selezione = st.selectbox(
                "Cartella",
                cartelle_opzioni,
                index=(
                    cartelle_opzioni.index(cartella_corrente)
                    if cartella_corrente in cartelle_opzioni
                    else 0
                ),
                key="manage_folder_select",
            )
            submit = st.form_submit_button("Sposta Lista")

            if submit:
                for t in st.session_state.my_lists:
                    if t["nome"] == lista_nome:
                        t["cartella"] = (
                            None if selezione == "— Nessuna —" else selezione
                        )
                        break
                st.rerun()


# -------------------------------------------------------------


# Funzione per cancellare una cartella
def delete_folder():
    if not st.session_state.folders:
        return

    with st.sidebar.popover("🗑️ Elimina cartella", use_container_width=True):
        cartella = st.selectbox(
            "Seleziona cartella", st.session_state.folders, key="delete_folder_select"
        )
        st.warning("Le liste contenute nella cartella non verranno eliminate")
        if st.button("Elimina Cartella", use_container_width=True):
            st.session_state.folders.remove(cartella)

            for t in st.session_state.my_lists:
                if t.get("cartella") == cartella:
                    t["cartella"] = None

            st.success(f"Cartella '{cartella}' eliminata")
            st.rerun()
