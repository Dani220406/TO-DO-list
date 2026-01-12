import pytest
from unittest.mock import MagicMock
from todo_app.sidebar.elements import(
safe_index, add_element, remove_element, mark_task_done, priority_element, edit_style, edit_text, reorder_elements)


# DotDict: dict + accesso tramite attributi
class DotDict(dict):
    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(key)

    def __setattr__(self, key, value):
        self[key] = value

    def __delattr__(self, key):
        del self[key]

# -------------------------------------------------------------


# Mock Streamlit
@pytest.fixture
def mock_streamlit(mocker):
    st = mocker.patch("todo_app.sidebar.elements.st")
    st.session_state = DotDict(active_list="Test", my_lists=[DotDict(nome="Test", dati=["task1", "task2"])])

    # context manager mock (form, popover, columns)
    cm = MagicMock()
    cm.__enter__.return_value = None
    cm.__exit__.return_value = None

    st.sidebar.popover.return_value = cm
    st.form.return_value = cm
    st.columns.return_value = (cm, cm)

    # comportamento UI di default
    st.form_submit_button.return_value = True
    st.button.return_value = True
    st.checkbox.side_effect = [True, False]
    st.selectbox.return_value = ("task1", 0)
    st.text_input.return_value = "nuovo task"
    st.text_area.return_value = "task modificato"

    return st

# -------------------------------------------------------------


# Mock Helpers
@pytest.fixture
def mock_helpers(mocker):
    mocker.patch("todo_app.sidebar.elements.parse_styled_text",
    return_value=DotDict(text="task1", bold=False, italic=False, color="nessuno"))
    mocker.patch("todo_app.sidebar.elements.build_styled_text", return_value="styled-task")
    mocker.patch("todo_app.sidebar.elements.toggle_prefix_emoji", return_value="✔️ task1")

# -------------------------------------------------------------


# safe_index
def test_safe_index_init(mocker):
    st = mocker.patch("todo_app.sidebar.elements.st")
    st.session_state = DotDict()
    safe_index("idx", 5)
    assert st.session_state.idx == 0

def test_safe_index_reset(mocker):
    st = mocker.patch("todo_app.sidebar.elements.st")
    st.session_state = DotDict(idx=10)
    safe_index("idx", 3)
    assert st.session_state.idx == 0

# -------------------------------------------------------------


# add_element
def test_add_element_adds_item(mock_streamlit):
    add_element()
    lista = mock_streamlit.session_state.my_lists[0]
    assert "nuovo task" in lista.dati
    mock_streamlit.rerun.assert_called_once()

def test_add_element_empty_input(mock_streamlit):
    mock_streamlit.text_input.return_value = "   "
    add_element()
    mock_streamlit.error.assert_called_once()

# -------------------------------------------------------------


# remove_element
def test_remove_element(mock_streamlit, mock_helpers):
    remove_element()
    lista = mock_streamlit.session_state.my_lists[0]
    assert len(lista.dati) == 1
    mock_streamlit.rerun.assert_called_once()

# -------------------------------------------------------------


# mark_task_done
def test_mark_task_done(mock_streamlit, mock_helpers):
    mark_task_done()
    lista = mock_streamlit.session_state.my_lists[0]
    assert lista.dati[0].startswith("✔️")
    mock_streamlit.rerun.assert_called_once()

# -------------------------------------------------------------


# priority_element
def test_priority_element(mock_streamlit, mock_helpers):
    priority_element()
    lista = mock_streamlit.session_state.my_lists[0]
    assert "task1" in lista.dati[0]
    mock_streamlit.rerun.assert_called_once()

# -------------------------------------------------------------


# edit_style
def test_edit_style(mock_streamlit, mock_helpers):
    edit_style()
    lista = mock_streamlit.session_state.my_lists[0]
    assert lista.dati[0] == "styled-task"
    mock_streamlit.rerun.assert_called_once()

# -------------------------------------------------------------


# edit_text
def test_edit_text(mock_streamlit, mock_helpers):
    edit_text()
    lista = mock_streamlit.session_state.my_lists[0]
    assert lista.dati[0] == "styled-task"
    mock_streamlit.rerun.assert_called_once()

# -------------------------------------------------------------


# reorder_elements
def test_reorder_elements_up(mock_streamlit, mock_helpers):
    mock_streamlit.selectbox.return_value = ("task2", 1)
    reorder_elements()
    lista = mock_streamlit.session_state.my_lists[0]
    assert lista.dati == ["task2", "task1"]
