import pytest
from types import SimpleNamespace
from todo_app.sidebar import lists


@pytest.fixture
def mock_streamlit(mocker):
    st = mocker.patch("todo_app.sidebar.lists.st")
    st.session_state = SimpleNamespace(my_lists=[], active_list=None)

    cm = mocker.MagicMock()
    cm.__enter__.return_value = None
    cm.__exit__.return_value = None

    st.sidebar.popover.return_value = cm
    st.form.return_value = cm
    st.columns.return_value = [cm]
    st.button.return_value = True
    st.sidebar.button.return_value = True
    st.form_submit_button.return_value = True
    st.text_input.return_value = "Lista Test"
    st.selectbox.return_value = "Lista Test"

    return st

# -------------------------------------------------------------


# create_new_list
def test_create_new_list_empty_name(mock_streamlit):
    mock_streamlit.text_input.return_value = ""
    lists.create_new_list()
    mock_streamlit.error.assert_called_once()
    assert mock_streamlit.session_state.my_lists == []

def test_create_new_list_duplicate(mock_streamlit):
    mock_streamlit.session_state.my_lists = [{"nome": "Lista Test", "dati": [], "cartella": None}]
    lists.create_new_list()
    mock_streamlit.warning.assert_called_once()
    assert len(mock_streamlit.session_state.my_lists) == 1

def test_create_new_list_success(mock_streamlit):
    lists.create_new_list()
    assert len(mock_streamlit.session_state.my_lists) == 1
    assert mock_streamlit.session_state.my_lists[0]["nome"] == "Lista Test"
    mock_streamlit.rerun.assert_called_once()

# -------------------------------------------------------------


# delete_list
def test_delete_list_empty(mock_streamlit):
    lists.delete_list()
    mock_streamlit.sidebar.popover.assert_not_called()

def test_delete_list_success(mock_streamlit):
    mock_streamlit.session_state.my_lists = [{"nome": "Lista Test", "dati": [], "cartella": None}]
    lists.delete_list()
    assert mock_streamlit.session_state.my_lists == []
    mock_streamlit.success.assert_called_once()
    mock_streamlit.rerun.assert_called_once()

# -------------------------------------------------------------


# show_lists
def test_show_lists_empty(mock_streamlit):
    lists.show_lists()
    mock_streamlit.info.assert_called_once()

def test_show_lists_click_opens_list(mock_streamlit):
    mock_streamlit.session_state.my_lists = [{"nome": "Lista Test", "dati": []}]
    lists.show_lists()
    assert mock_streamlit.session_state.active_list == "Lista Test"
    mock_streamlit.rerun.assert_called_once()

# -------------------------------------------------------------


# show_selected_list
def test_show_selected_list_empty(mock_streamlit):
    mock_streamlit.session_state.my_lists = [{"nome": "Lista Test", "dati": []}]
    mock_streamlit.session_state.active_list = "Lista Test"
    lists.show_selected_list()
    mock_streamlit.info.assert_called_once()

def test_show_selected_list_with_items(mock_streamlit):
    mock_streamlit.session_state.my_lists = [{"nome": "Lista Test", "dati": ["task1", "task2"]}]
    mock_streamlit.session_state.active_list = "Lista Test"
    lists.show_selected_list()
    assert mock_streamlit.markdown.call_count >= 3

# -------------------------------------------------------------


# sidebar_selected_list
def test_sidebar_selected_list_calls_all(mocker, mock_streamlit):
    mocker.patch("todo_app.sidebar.lists.add_element")
    mocker.patch("todo_app.sidebar.lists.edit_text")
    mocker.patch("todo_app.sidebar.lists.remove_element")
    mocker.patch("todo_app.sidebar.lists.reorder_elements")
    mocker.patch("todo_app.sidebar.lists.mark_task_done")
    mocker.patch("todo_app.sidebar.lists.priority_element")
    mocker.patch("todo_app.sidebar.lists.edit_style")

    lists.sidebar_selected_list("Lista Test")

    assert mock_streamlit.session_state.active_list is None
    mock_streamlit.rerun.assert_called_once()
