import streamlit as st
from todo_app.utils.helpers import (
    parse_styled_text,
    build_styled_text,
    toggle_prefix_emoji,
)


# Method to clear index in every new list
def safe_index(key: str, length: int):
    if key not in st.session_state or st.session_state[key] >= length:
        st.session_state[key] = 0


# -------------------------------------------------------------


# Method to add an element to selected list
def add_element():
    st.sidebar.markdown("---")
    nome_lista = st.session_state.active_list
    lista = next(
        (t for t in st.session_state.my_lists if t["nome"] == nome_lista), None
    )

    if lista is None:
        return

    with st.sidebar.popover("➕ Add Element", use_container_width=True):
        with st.form(key="form_aggiunta", clear_on_submit=True):
            nuovo_item = st.text_input("What to add?")
            if st.form_submit_button("Add Element"):
                if nuovo_item.strip():
                    lista["dati"].append(nuovo_item.strip())
                    st.rerun()
                else:
                    st.error("No element added.")


# -------------------------------------------------------------


# Method to delete an element from list
def remove_element():
    nome_lista = st.session_state.active_list
    lista = next(
        (t for t in st.session_state.my_lists if t["nome"] == nome_lista), None
    )

    if not lista or not lista["dati"]:
        return

    with st.sidebar.popover("❌ Delete Element", use_container_width=True):
        with st.form(key="form_rimozione", clear_on_submit=True):
            elementi = [
                (parse_styled_text(item)["text"], i)
                for i, item in enumerate(lista["dati"])
            ]
            scelta, idx = st.selectbox(
                "Select an element to delete", elementi, format_func=lambda x: x[0]
            )

            if st.form_submit_button("Delete Element"):
                lista["dati"].pop(idx)
                st.rerun()


# -------------------------------------------------------------


# Method to mark list element as completed
def mark_task_done():
    nome_lista = st.session_state.active_list
    lista = next(
        (t for t in st.session_state.my_lists if t["nome"] == nome_lista), None
    )

    if not lista or not lista["dati"]:
        return

    with st.sidebar.popover("✅ Complete Task", use_container_width=True):
        elementi = [
            (parse_styled_text(item)["text"], i) for i, item in enumerate(lista["dati"])
        ]

        safe_index("done_idx", len(elementi))

        scelta, idx = st.selectbox(
            "Select task",
            elementi,
            index=st.session_state.done_idx,
            format_func=lambda x: x[0],
            key="done_select",
        )
        st.session_state.done_idx = idx
        st.warning("Completing an already completed task will remove its checkmark.")

        if st.button("Complete"):
            testo = lista["dati"][idx]
            lista["dati"][idx] = toggle_prefix_emoji(testo, "✔️")
            st.rerun()


# -------------------------------------------------------------


# Method to label an element
def priority_element():
    nome_lista = st.session_state.active_list
    lista = next(
        (t for t in st.session_state.my_lists if t["nome"] == nome_lista), None
    )

    if not lista or not lista["dati"]:
        return

    with st.sidebar.popover("🏷️ Label", use_container_width=True):
        elementi = [
            (parse_styled_text(item)["text"], i) for i, item in enumerate(lista["dati"])
        ]

        safe_index("label_idx", len(elementi))

        scelta, idx = st.selectbox(
            "Select element",
            elementi,
            index=st.session_state.label_idx,
            format_func=lambda x: x[0],
            key="label_select",
        )
        st.session_state.label_idx = idx
        st.warning("Labeling an already labeled task will remove its label.")

        if st.button("Label"):
            testo = lista["dati"][idx]
            lista["dati"][idx] = toggle_prefix_emoji(testo, "🏷️")
            st.rerun()


# -------------------------------------------------------------


# Method to edit an element's text style
def edit_style():
    nome_lista = st.session_state.active_list
    lista = next(
        (t for t in st.session_state.my_lists if t["nome"] == nome_lista), None
    )

    if not lista or not lista["dati"]:
        return

    with st.sidebar.popover("✏️ Edit Style", use_container_width=True):
        elementi = [
            (parse_styled_text(item)["text"], i) for i, item in enumerate(lista["dati"])
        ]

        safe_index("style_element_idx", len(elementi))

        scelta, idx = st.selectbox(
            "Select element",
            elementi,
            index=st.session_state.style_element_idx,
            format_func=lambda x: x[0],
            key="style_element_select",
        )
        st.session_state.style_element_idx = idx
        current = parse_styled_text(lista["dati"][idx])
        bold_now = st.checkbox("Bold", value=current["bold"])
        italic_now = st.checkbox("Italics", value=current["italic"])

        colori = ["none", "red", "green", "blue", "orange", "violet"]
        color_now = st.selectbox(
            "Color",
            colori,
            index=colori.index(current["color"]) if current["color"] in colori else 0,
        )
        preview = {
            "text": current["text"],
            "bold": bold_now,
            "italic": italic_now,
            "color": color_now,
        }
        st.markdown(f"**Preview:** {build_styled_text(preview)}")

        if st.button("Apply Edit"):
            lista["dati"][idx] = build_styled_text(preview)
            st.rerun()


# -------------------------------------------------------------


# Method to edit an element's text
def edit_text():
    nome_lista = st.session_state.active_list
    lista = next(
        (t for t in st.session_state.my_lists if t["nome"] == nome_lista), None
    )

    if not lista or not lista["dati"]:
        return

    with st.sidebar.popover("📝 Edit Element", use_container_width=True):
        elementi = [
            (parse_styled_text(item)["text"], i) for i, item in enumerate(lista["dati"])
        ]

        safe_index("edit_element_idx", len(elementi))

        scelta, idx = st.selectbox(
            "Select element",
            elementi,
            index=st.session_state.edit_element_idx,
            format_func=lambda x: x[0],
            key="edit_element_select",
        )
        st.session_state.edit_element_idx = idx
        current = parse_styled_text(lista["dati"][idx])
        new_text = st.text_area("Edit text", value=current["text"])

        if st.button("Apply Edits"):
            updated = {
                "text": new_text,
                "bold": current["bold"],
                "italic": current["italic"],
                "color": current["color"],
            }
            lista["dati"][idx] = build_styled_text(updated)
            st.rerun()


# -------------------------------------------------------------


# Method to order elements in list
def reorder_elements():
    nome_lista = st.session_state.active_list
    lista = next(
        (t for t in st.session_state.my_lists if t["nome"] == nome_lista), None
    )

    if not lista or not lista["dati"]:
        return

    with st.sidebar.popover("🔀 Order Elements", use_container_width=True):
        elementi = [
            (parse_styled_text(item)["text"], i) for i, item in enumerate(lista["dati"])
        ]

        safe_index("reorder_idx", len(elementi))

        scelta, idx = st.selectbox(
            "Select an element to reorder",
            elementi,
            index=st.session_state.reorder_idx,
            format_func=lambda x: x[0],
            key="reorder_select",
        )
        st.session_state.reorder_idx = idx
        col1, col2 = st.columns(2)

        with col1:
            if st.button("⬆️ Up") and idx > 0:
                lista["dati"][idx], lista["dati"][idx - 1] = (
                    lista["dati"][idx - 1],
                    lista["dati"][idx],
                )
                st.session_state.reorder_idx -= 1
                st.rerun()

        with col2:
            if st.button("⬇️ Down") and idx < len(lista["dati"]) - 1:
                lista["dati"][idx], lista["dati"][idx + 1] = (
                    lista["dati"][idx + 1],
                    lista["dati"][idx],
                )
                st.session_state.reorder_idx += 1
                st.rerun()
