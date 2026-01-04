import pytest
from types import SimpleNamespace
from test_todo_app.screens.welcome import welcome_screen

@pytest.fixture
def mock_streamlit_and_time(mocker):
    # Patch di st e time.sleep
    st = mocker.patch("test_todo_app.screens.welcome.st")
    mocker.patch("test_todo_app.screens.welcome.time.sleep")
    st.session_state = SimpleNamespace()
    st.rerun = mocker.MagicMock()
    return st

# -------------------------------------------------------------

def test_welcome_screen_flow(mock_streamlit_and_time):
    st = mock_streamlit_and_time
    welcome_screen()

    st.markdown.assert_called_once()
    _, kwargs = st.markdown.call_args
    assert kwargs.get("unsafe_allow_html") is True
    assert st.session_state.vista == "home"
    st.rerun.assert_called_once()