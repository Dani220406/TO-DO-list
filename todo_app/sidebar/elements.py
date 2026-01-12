# pylint: disable=unused-argument
import streamlit as st
from todo_app.utils.helpers import parse_styled_text, build_styled_text, toggle_prefix_emoji

# Funzione per pulire l'index in ogni nuova lista
def safe_index(key: str, length: int):
    if key not in st.session_state or st.session_state[key] >= length:
        st.session_state[key] = 0

# -------------------------------------------------------------

# Funzione per aggiungere un elemento alla lista selezionata
def add_element():
    st.sidebar.markdown("---")
    nome_lista = st.session_state.active_list
    lista = next((l for l in st.session_state.my_lists if l["nome"] == nome_lista), None)

    if lista is None:
        return

    with st.sidebar.popover("➕ Aggiungi elemento", use_container_width=True):
        with st.form(key="form_aggiunta", clear_on_submit=True):
            nuovo_item = st.text_input("Cosa vuoi aggiungere?")
            if st.form_submit_button("Aggiungi"):
                if nuovo_item.strip():
                    lista["dati"].append(nuovo_item.strip())
                    st.rerun()
                else:
                    st.error("Nessun elemento inserito.")

# -------------------------------------------------------------

# Funzione che rimuove un elemento dalla lista
def remove_element():
    nome_lista = st.session_state.active_list
    lista = next((l for l in st.session_state.my_lists if l["nome"] == nome_lista), None)

    if not lista or not lista["dati"]:
        return

    with st.sidebar.popover("❌ Rimuovi elemento", use_container_width=True):
        with st.form(key="form_rimozione", clear_on_submit=True):
            elementi = [(parse_styled_text(item)["text"], i) for i, item in enumerate(lista["dati"])]
            scelta, idx = st.selectbox("Seleziona elemento da rimuovere", elementi, format_func=lambda x: x[0])

            if st.form_submit_button("Rimuovi"):
                lista["dati"].pop(idx)
                st.rerun()

# -------------------------------------------------------------

# Funzione che segna un elemento della lista come completato
def mark_task_done():
    nome_lista = st.session_state.active_list
    lista = next((l for l in st.session_state.my_lists if l["nome"] == nome_lista), None)

    if not lista or not lista["dati"]:
        return

    with st.sidebar.popover("✅ Segna task completato", use_container_width=True):
        elementi = [(parse_styled_text(item)["text"], i) for i, item in enumerate(lista["dati"])]

        safe_index("done_idx", len(elementi))

        scelta, idx = st.selectbox("Seleziona task", elementi, index=st.session_state.done_idx, format_func=lambda x: x[0], key="done_select")
        st.session_state.done_idx = idx
        st.warning("Confermare un task già completato rimuoverà il checkmark")

        if st.button("Completato"):
            testo = lista["dati"][idx]
            
            lista["dati"][idx] = toggle_prefix_emoji(testo, "✔️")
            st.rerun()

# -------------------------------------------------------------

# Funzione per etichettare un elemento
def priority_element():
    nome_lista = st.session_state.active_list
    lista = next((l for l in st.session_state.my_lists if l["nome"] == nome_lista), None)

    if not lista or not lista["dati"]:
        return

    with st.sidebar.popover("🏷️ Etichetta", use_container_width=True):
        elementi = [(parse_styled_text(item)["text"], i) for i, item in enumerate(lista["dati"])]

        safe_index("label_idx", len(elementi))

        scelta, idx = st.selectbox("Seleziona elemento", elementi, index=st.session_state.label_idx, format_func=lambda x: x[0], key="label_select")
        st.session_state.label_idx = idx
        st.warning("Etichettare un task già etichettato rimuoverà l'etichetta")

        if st.button("Etichetta"):
            testo = lista["dati"][idx]
            
            lista["dati"][idx] = toggle_prefix_emoji(testo, "🏷️")
            st.rerun()

# -------------------------------------------------------------

# Funzione per modificare lo stile di un elemento
def edit_style():
    nome_lista = st.session_state.active_list
    lista = next((l for l in st.session_state.my_lists if l["nome"] == nome_lista), None)

    if not lista or not lista["dati"]:
        return

    with st.sidebar.popover("✏️ Modifica stile", use_container_width=True):
        elementi = [(parse_styled_text(item)["text"], i) for i, item in enumerate(lista["dati"])]

        safe_index("style_element_idx", len(elementi))

        scelta, idx = st.selectbox("Seleziona elemento", elementi, index=st.session_state.style_element_idx, format_func=lambda x: x[0], key="style_element_select")
        st.session_state.style_element_idx = idx
        current = parse_styled_text(lista["dati"][idx])
        bold_now = st.checkbox("Grassetto", value=current["bold"])
        italic_now = st.checkbox("Corsivo", value=current["italic"])

        colori = ["nessuno", "red", "green", "blue", "orange", "violet"]
        color_now = st.selectbox("Colore", colori, index=colori.index(current["color"]) if current["color"] in colori else 0)
        preview = {"text": current["text"], "bold": bold_now, "italic": italic_now, "color": color_now,}
        st.markdown(f"**Anteprima:** {build_styled_text(preview)}")

        if st.button("Applica"):
            lista["dati"][idx] = build_styled_text(preview)
            st.rerun()

# -------------------------------------------------------------

# Funzione per modificare il testo di un elemento
def edit_text():
    nome_lista = st.session_state.active_list
    lista = next((l for l in st.session_state.my_lists if l["nome"] == nome_lista), None)

    if not lista or not lista["dati"]:
        return

    with st.sidebar.popover("📝 Modifica elemento", use_container_width=True):
        elementi = [(parse_styled_text(item)["text"], i) for i, item in enumerate(lista["dati"])]

        safe_index("edit_element_idx", len(elementi))

        scelta, idx = st.selectbox("Seleziona elemento", elementi, index=st.session_state.edit_element_idx, format_func=lambda x: x[0], key="edit_element_select")
        st.session_state.edit_element_idx = idx
        current = parse_styled_text(lista["dati"][idx])
        new_text = st.text_area("Modifica testo", value=current["text"])

        if st.button("Modifica"):
            updated = {"text": new_text, "bold": current["bold"], "italic": current["italic"], "color": current["color"],}
            lista["dati"][idx] = build_styled_text(updated)
            st.rerun()

# -------------------------------------------------------------

# Funzione per ordinare elementi nella lista
def reorder_elements():
    nome_lista = st.session_state.active_list
    lista = next((l for l in st.session_state.my_lists if l["nome"] == nome_lista), None)

    if not lista or not lista["dati"]:
        return

    with st.sidebar.popover("🔀 Ordina elementi", use_container_width=True):
        elementi = [(parse_styled_text(item)["text"], i) for i, item in enumerate(lista["dati"])]

        safe_index("reorder_idx", len(elementi))

        scelta, idx = st.selectbox("Seleziona elemento da spostare", elementi, index=st.session_state.reorder_idx, format_func=lambda x: x[0], key="reorder_select")
        st.session_state.reorder_idx = idx
        col1, col2 = st.columns(2)

        with col1:
            if st.button("⬆️ Su") and idx > 0:
                lista["dati"][idx], lista["dati"][idx - 1] = lista["dati"][idx - 1], lista["dati"][idx]
                st.session_state.reorder_idx -= 1
                st.rerun()

        with col2:
            if st.button("⬇️ Giù") and idx < len(lista["dati"]) - 1:
                lista["dati"][idx], lista["dati"][idx + 1] = lista["dati"][idx + 1], lista["dati"][idx]
                st.session_state.reorder_idx += 1
                st.rerun()
