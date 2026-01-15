import pytest
from types import SimpleNamespace


# Fixture to patch st and simulate session_state
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

    # Import main AFTER having patched st and the layers
    from todo_app.main import main

    main()

    welcome_mock.assert_called_once()
    home_mock.assert_not_called()


# -------------------------------------------------------------


def test_main_calls_home(mock_st, mocker):
    mock_st.session_state.vista = "home"
    welcome_mock = mocker.patch("todo_app.main.welcome_screen")
    home_mock = mocker.patch("todo_app.main.home")

    # Import main AFTER having patched st and the layers
    from todo_app.main import main

    main()

    home_mock.assert_called_once()
    welcome_mock.assert_not_called()
