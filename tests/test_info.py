import pytest
from todo_app.sidebar.info import info


@pytest.fixture
def mock_streamlit(mocker):
    st = mocker.patch("todo_app.sidebar.info.st")
    st.session_state = {}

    # Mock per sidebar.expander come context manager
    cm = mocker.MagicMock()
    cm.__enter__.return_value = None
    cm.__exit__.return_value = None
    st.sidebar.expander.return_value = cm

    # Mock per chiamate a markdown
    st.markdown = mocker.MagicMock()
    st.sidebar.markdown = mocker.MagicMock()

    return st


# -------------------------------------------------------------


def test_info_renders_sidebar_content(mock_streamlit):
    info()

    mock_streamlit.sidebar.expander.assert_called_once_with("ℹ️ Info", expanded=False)
    mock_streamlit.markdown.assert_called_once()
    mock_streamlit.sidebar.markdown.assert_called_once_with("---")
