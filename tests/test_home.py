import pytest
from types import SimpleNamespace
from test_todo_app.screens.home import home

@pytest.fixture
def mock_streamlit(mocker):
    st = mocker.patch("test_todo_app.screens.home.st")
    st.session_state = SimpleNamespace(active_list=None, my_lists=[])
    return st

# -------------------------------------------------------------

def test_home_with_active_list(mocker, mock_streamlit):
    mock_streamlit.session_state.active_list = "Lista Test"
    info = mocker.patch("test_todo_app.screens.home.info")
    sidebar_selected_list = mocker.patch("test_todo_app.screens.home.sidebar_selected_list")
    show_selected_list = mocker.patch("test_todo_app.screens.home.show_selected_list")
    create_new_list = mocker.patch("test_todo_app.screens.home.create_new_list")
    delete_list = mocker.patch("test_todo_app.screens.home.delete_list")
    create_folder = mocker.patch("test_todo_app.screens.home.create_folder")
    manage_list_folder = mocker.patch("test_todo_app.screens.home.manage_list_folder")
    delete_folder = mocker.patch("test_todo_app.screens.home.delete_folder")
    show_folders_sidebar = mocker.patch("test_todo_app.screens.home.show_folders_sidebar")
    show_lists = mocker.patch("test_todo_app.screens.home.show_lists")
    home()

    info.assert_called_once()
    sidebar_selected_list.assert_called_once_with("Lista Test")
    show_selected_list.assert_called_once()
    create_new_list.assert_not_called()
    delete_list.assert_not_called()
    create_folder.assert_not_called()
    manage_list_folder.assert_not_called()
    delete_folder.assert_not_called()
    show_folders_sidebar.assert_not_called()
    show_lists.assert_not_called()

# -------------------------------------------------------------

def test_home_without_active_list(mocker, mock_streamlit):
    info = mocker.patch("test_todo_app.screens.home.info")
    create_new_list = mocker.patch("test_todo_app.screens.home.create_new_list")
    delete_list = mocker.patch("test_todo_app.screens.home.delete_list")
    create_folder = mocker.patch("test_todo_app.screens.home.create_folder")
    manage_list_folder = mocker.patch("test_todo_app.screens.home.manage_list_folder")
    delete_folder = mocker.patch("test_todo_app.screens.home.delete_folder")
    show_folders_sidebar = mocker.patch("test_todo_app.screens.home.show_folders_sidebar")
    show_lists = mocker.patch("test_todo_app.screens.home.show_lists")
    sidebar_selected_list = mocker.patch("test_todo_app.screens.home.sidebar_selected_list")
    show_selected_list = mocker.patch("test_todo_app.screens.home.show_selected_list")
    home()

    info.assert_called_once()
    create_new_list.assert_called_once()
    delete_list.assert_called_once()
    create_folder.assert_called_once()
    manage_list_folder.assert_called_once()
    delete_folder.assert_called_once()
    show_folders_sidebar.assert_called_once()
    show_lists.assert_called_once()
    sidebar_selected_list.assert_not_called()
    show_selected_list.assert_not_called()