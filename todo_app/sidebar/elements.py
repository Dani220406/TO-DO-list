import streamlit as st
from utils.helpers import parse_styled_text, build_styled_text

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

# -------------------------------------------------------------

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

# -------------------------------------------------------------

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

    if "style_element_idx" not in st.session_state:
        st.session_state.style_element_idx = 0

    with st.sidebar.popover("✏️ Modifica Stile", use_container_width=True):
        elementi = [(parse_styled_text(item)["text"], i) for i, item in enumerate(lista["dati"])]

        scelta, idx = st.selectbox("Seleziona elemento", elementi, index=st.session_state.style_element_idx, format_func=lambda x: x[0], key="style_element_select")
        st.session_state.style_element_idx = idx
        current = parse_styled_text(lista["dati"][idx])

        bold_now = st.checkbox("Grassetto", value=current["bold"], key=f"style_bold_{idx}")
        italic_now = st.checkbox("Corsivo", value=current["italic"], key=f"style_italic_{idx}")
        colori = ["nessuno", "red", "green", "blue", "orange", "violet"]
        color_now = st.selectbox("Colore", colori, index=colori.index(current["color"]) if current["color"] in colori else 0, key=f"style_color_{idx}")
        preview = {"text": current["text"], "bold": bold_now, "italic": italic_now, "color": color_now}
        st.markdown(f"**Anteprima:** {build_styled_text(preview)}")

        if st.button("Applica", key=f"apply_style_{idx}"):
            lista["dati"][idx] = build_styled_text(preview)
            st.rerun()

# -------------------------------------------------------------

# Funzione per modificare il testo di un elemento
def edit_text():
    nome_lista = st.session_state.active_list
    lista = next((l for l in st.session_state.my_lists if l["nome"] == nome_lista), None)

    if not lista or not lista["dati"]:
        st.sidebar.info("Nessun elemento da modificare")
        return

    if "edit_element_idx" not in st.session_state:
        st.session_state.edit_element_idx = 0

    with st.sidebar.popover("📝 Modifica elemento", use_container_width=True):
        elementi = [(parse_styled_text(item)["text"], i) for i, item in enumerate(lista["dati"])]

        scelta, idx = st.selectbox("Seleziona elemento", elementi, index=st.session_state.edit_element_idx, format_func=lambda x: x[0], key="edit_element_select")
        st.session_state.edit_element_idx = idx
        current = parse_styled_text(lista["dati"][idx])
        new_text = st.text_area("Modifica testo", value=current["text"], key=f"edit_text_input_{idx}")

        if st.button("Salva testo", key=f"save_text_{idx}"):
            updated = {"text": new_text, "bold": current["bold"], "italic": current["italic"], "color": current["color"]}
            lista["dati"][idx] = build_styled_text(updated)
            st.rerun()

# -------------------------------------------------------------

# Funzione per ordinare elementi nella lista
def reorder_elements():
    nome_lista = st.session_state.active_list
    lista = next((l for l in st.session_state.my_lists if l["nome"] == nome_lista), None)

    if not lista or not lista["dati"]:
        st.sidebar.info("Nessun elemento da ordinare")
        return

    if "reorder_idx" not in st.session_state:
        st.session_state.reorder_idx = 0

    with st.sidebar.popover("🔀 Ordina elementi", use_container_width=True):
        elementi = [(parse_styled_text(item)["text"], i) for i, item in enumerate(lista["dati"])]

        scelta, idx = st.selectbox("Seleziona elemento da spostare", elementi, index=st.session_state.reorder_idx, format_func=lambda x: x[0], key="reorder_select")
        st.session_state.reorder_idx = idx

        col1, col2 = st.columns(2)
        with col1:
            if st.button("⬆️ Su", key=f"move_up_{idx}"):
                if idx > 0:
                    lista["dati"][idx], lista["dati"][idx-1] = lista["dati"][idx-1], lista["dati"][idx]
                    st.session_state.reorder_idx -= 1
                    st.rerun()
        with col2:
            if st.button("⬇️ Giù", key=f"move_down_{idx}"):
                if idx < len(lista["dati"]) - 1:
                    lista["dati"][idx], lista["dati"][idx+1] = lista["dati"][idx+1], lista["dati"][idx]
                    st.session_state.reorder_idx += 1
                    st.rerun()