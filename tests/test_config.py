# pylint: disable=redefined-outer-name,too-few-public-methods
import pytest
from types import SimpleNamespace
from todo_app.config import init_session_state

# Wrapper per permettere 'key' in session_state
class SessionState(SimpleNamespace):
    def __contains__(self, key):
        return hasattr(self, key)

# -------------------------------------------------------------

@pytest.fixture
def mock_streamlit(mocker):
    st = mocker.patch("todo_app.config.st")
    st.session_state = SessionState()
    return st

# -------------------------------------------------------------

def test_init_session_state_all_keys_added(mock_streamlit):
    st = mock_streamlit
    init_session_state()

    assert st.session_state.vista == "welcome"
    assert st.session_state.my_lists == []
    assert st.session_state.active_list is None
    assert st.session_state.folders == []

# -------------------------------------------------------------

def test_init_session_state_preserves_existing_keys(mock_streamlit):
    st = mock_streamlit
    st.session_state.vista = "home"
    st.session_state.my_lists = ["Lista esistente"]

    init_session_state()

    assert st.session_state.vista == "home"
    assert st.session_state.my_lists == ["Lista esistente"]
    assert st.session_state.active_list is None
    assert st.session_state.folders == []
