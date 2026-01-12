import pytest
from unittest.mock import MagicMock
from todo_app.sidebar.folders import create_folder, show_folders_sidebar, manage_list_folder, delete_folder


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
    st = mocker.patch("todo_app.sidebar.folders.st")
    st.session_state = DotDict(folders=[], my_lists=[], active_list=None)

    # context manager mock (form, popover, expander)
    cm = MagicMock()
    cm.__enter__.return_value = None
    cm.__exit__.return_value = None

    st.sidebar.popover.return_value = cm
    st.sidebar.expander.return_value = cm
    st.form.return_value = cm

    # comportamento UI di default
    st.form_submit_button.return_value = True
    st.button.return_value = True
    st.text_input.return_value = "Cartella Test"
    st.selectbox.return_value = "Cartella Test"

    return st

# -------------------------------------------------------------

# create_folder
def test_create_folder_empty_name(mock_streamlit):
    mock_streamlit.text_input.return_value = ""
    create_folder()
    mock_streamlit.error.assert_called_once()
    assert mock_streamlit.session_state.folders == []

def test_create_folder_duplicate(mock_streamlit):
    mock_streamlit.session_state.folders = ["Cartella Test"]
    create_folder()
    mock_streamlit.warning.assert_called_once()

def test_create_folder_success(mock_streamlit):
    create_folder()
    assert "Cartella Test" in mock_streamlit.session_state.folders
    mock_streamlit.success.assert_called_once()
    mock_streamlit.rerun.assert_called_once()

# -------------------------------------------------------------

# show_folders_sidebar
def test_show_folders_sidebar_empty(mock_streamlit):
    show_folders_sidebar()
    mock_streamlit.sidebar.subheader.assert_not_called()

def test_show_folders_sidebar_no_lists(mock_streamlit):
    mock_streamlit.session_state.folders = ["Cartella Test"]
    show_folders_sidebar()
    mock_streamlit.caption.assert_called_once()

def test_show_folders_sidebar_open_list(mock_streamlit):
    mock_streamlit.session_state.folders = ["Cartella Test"]
    mock_streamlit.session_state.my_lists = [DotDict(nome="Lista 1", cartella="Cartella Test")]
    show_folders_sidebar()
    assert mock_streamlit.session_state.active_list == "Lista 1"
    mock_streamlit.rerun.assert_called_once()

# -------------------------------------------------------------

# manage_list_folder
def test_manage_list_folder_early_return(mock_streamlit):
    manage_list_folder()
    mock_streamlit.sidebar.popover.assert_not_called()

def test_manage_list_folder_assign(mock_streamlit):
    mock_streamlit.session_state.folders = ["Cartella Test"]
    mock_streamlit.session_state.my_lists = [DotDict(nome="Lista 1", cartella=None)]
    mock_streamlit.selectbox.side_effect = ["Lista 1", "Cartella Test"]
    manage_list_folder()

    assert mock_streamlit.session_state.my_lists[0].cartella == "Cartella Test"
    mock_streamlit.rerun.assert_called_once()

# -------------------------------------------------------------

# delete_folder
def test_delete_folder_early_return(mock_streamlit):
    delete_folder()
    mock_streamlit.sidebar.popover.assert_not_called()

def test_delete_folder_success(mock_streamlit):
    mock_streamlit.session_state.folders = ["Cartella Test"]
    mock_streamlit.session_state.my_lists = [DotDict(nome="Lista 1", cartella="Cartella Test")]
    delete_folder()

    assert "Cartella Test" not in mock_streamlit.session_state.folders
    assert mock_streamlit.session_state.my_lists[0].cartella is None
    mock_streamlit.success.assert_called_once()
    mock_streamlit.rerun.assert_called_once()
