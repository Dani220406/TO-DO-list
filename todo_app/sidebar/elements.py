import streamlit as st

# Funzione per aggiungere un elemento alla lista selezionata
def add_element():
    st.sidebar.markdown("---")
    nome_lista = st.session_state.active_list
    lista = next((l for l in st.session_state.my_lists if l["nome"] == nome_lista), None)

    if lista is not None:
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

# Funzione che rimuove un elemento dalla lista
def remove_element():
    nome_lista = st.session_state.active_list
    lista = next((l for l in st.session_state.my_lists if l["nome"] == nome_lista), None)

    if lista and lista["dati"]:
        with st.sidebar.popover("❌ Rimuovi elemento", use_container_width=True):
            with st.form(key="form_rimozione", clear_on_submit=True):
                options = [f"{idx+1}. {item}" for idx, item in enumerate(lista["dati"])]
                elemento_da_rimuovere = st.selectbox("Seleziona elemento da rimuovere", options)

                submit = st.form_submit_button("Rimuovi")

                if submit:
                    idx = int(elemento_da_rimuovere.split(".")[0]) - 1
                    lista["dati"].pop(idx)
                    st.rerun()
    else:
        st.sidebar.info("Lista vuota, niente da rimuovere.")

# Funzione che segna un elemento della lista come completato
def mark_task_done():
    nome_lista = st.session_state.active_list
    lista = next((l for l in st.session_state.my_lists if l["nome"] == nome_lista), None)

    if lista and lista["dati"]:
        with st.sidebar.popover("✅ Segna task completato", use_container_width=True):
            with st.form(key="form_mark_done", clear_on_submit=True):
                options = [f"{idx+1}. {item}" for idx, item in enumerate(lista["dati"])]
                task_selezionato = st.selectbox("Seleziona task", options)

                st.warning("Confermare un task già completato riumoverà il checkmark")
                submit = st.form_submit_button("Conferma")

                if submit:
                    idx = int(task_selezionato.split(".")[0]) - 1
                    task = lista["dati"][idx]

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

#Funzione per applicare modifiche al testo di un elemento della lista
def edit_style():
    nome_lista = st.session_state.active_list
    lista = next((l for l in st.session_state.my_lists if l["nome"] == nome_lista), None)

    if not lista or not lista["dati"]:
        st.sidebar.info("Nessun elemento da modificare")
        return

    with st.sidebar.popover("✏️ Modifica Stile", use_container_width=True):
        with st.form("form_style"):
            scelta = st.selectbox(
                "Elemento",
                [f"{i+1}. {item}" for i, item in enumerate(lista["dati"])],
                key="style_element_select"
            )

            idx = int(scelta.split(".")[0]) - 1
            testo_originale = lista["dati"][idx]
            testo = testo_originale
            colore = None

            if testo.startswith(":") and "[" in testo and testo.endswith("]"):
                colore = testo[1:].split("[", 1)[0]
                testo = testo.split("[", 1)[1][:-1]

            bold_prev = testo.startswith("**") and testo.endswith("**")
            italic_prev = testo.startswith("*") and testo.endswith("*") and not bold_prev

            if bold_prev:
                testo = testo[2:-2]
            if italic_prev:
                testo = testo[1:-1]

            bold_now = st.checkbox("Grassetto", value=bold_prev, key="style_bold_checkbox")
            italic_now = st.checkbox("Corsivo", value=italic_prev, key="style_italic_checkbox")

            colori = ["nessuno", "red", "green", "blue", "orange", "violet"]
            colore_now = st.selectbox(
                "Colore",
                colori,
                index=colori.index(colore) if colore in colori else 0,
                key="style_color_select"
            )

            submit = st.form_submit_button("Applica")

            if submit:
                nuovo = testo

                if bold_now:
                    nuovo = f"**{nuovo}**"
                if italic_now:
                    nuovo = f"*{nuovo}*"
                if colore_now != "nessuno":
                    nuovo = f":{colore_now}[{nuovo}]"

                lista["dati"][idx] = nuovo
                st.rerun()
