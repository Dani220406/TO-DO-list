import pytest
from types import SimpleNamespace


# Fixture per patchare st e simulare session_state
@pytest.fixture
def mock_st(mocker):
    st = mocker.patch("todo_app.main.st")
    st.session_state = SimpleNamespace()
    return st


# -------------------------------------------------------------


def test_main_calls_welcome_screen(mock_st, mocker):
    mock_st.session_state.vista = "welcome"
    welcome_mock = mocker.patch("todo_app.main.welcome_screen")
    home_mock = mocker.patch("todo_app.main.home")

    # Importiamo main DOPO aver patchato st e le schermate
    from todo_app.main import main

    main()

    welcome_mock.assert_called_once()
    home_mock.assert_not_called()


# -------------------------------------------------------------


def test_main_calls_home(mock_st, mocker):
    mock_st.session_state.vista = "home"
    welcome_mock = mocker.patch("todo_app.main.welcome_screen")
    home_mock = mocker.patch("todo_app.main.home")

    # Importiamo main DOPO aver patchato st e le schermate
    from todo_app.main import main

    main()

    home_mock.assert_called_once()
    welcome_mock.assert_not_called()
