import pytest
from todo_app.utils.helpers import (
    parse_styled_text,
    build_styled_text,
    toggle_prefix_emoji,
)


# parse_styled_text
@pytest.mark.parametrize(
    "input_text,expected",
    [
        ("ciao", {"text": "ciao", "bold": False, "italic": False, "color": None}),
        ("**ciao**", {"text": "ciao", "bold": True, "italic": False, "color": None}),
        ("*ciao*", {"text": "ciao", "bold": False, "italic": True, "color": None}),
        (
            ":red[ciao]",
            {"text": "ciao", "bold": False, "italic": False, "color": "red"},
        ),
        (
            ":blue[**ciao**]",
            {"text": "ciao", "bold": True, "italic": False, "color": "blue"},
        ),
        (
            ":green[*ciao*]",
            {"text": "ciao", "bold": False, "italic": True, "color": "green"},
        ),
    ],
)
def test_parse_styled_text(input_text, expected):
    assert parse_styled_text(input_text) == expected


# -------------------------------------------------------------


# build_styled_text
@pytest.mark.parametrize(
    "input_dict,expected",
    [
        ({"text": "ciao", "bold": False, "italic": False, "color": None}, "ciao"),
        ({"text": "ciao", "bold": True, "italic": False, "color": None}, "**ciao**"),
        ({"text": "ciao", "bold": False, "italic": True, "color": None}, "*ciao*"),
        (
            {"text": "ciao", "bold": False, "italic": False, "color": "red"},
            ":red[ciao]",
        ),
        (
            {"text": "ciao", "bold": True, "italic": True, "color": "blue"},
            ":blue[***ciao***]",
        ),
        ({"text": "ciao", "bold": False, "italic": False, "color": "nessuno"}, "ciao"),
    ],
)
def test_build_styled_text(input_dict, expected):
    result = build_styled_text(input_dict)
    assert result.replace("\\", "") == expected


# -------------------------------------------------------------


# toggle_prefix_emoji
def test_toggle_prefix_emoji():
    assert toggle_prefix_emoji("task", "✔️").startswith("✔️")
    assert toggle_prefix_emoji("✔️ task", "✔️") == "task"
    assert toggle_prefix_emoji("✔️ task", "🏷️").startswith("✔️ 🏷️")
    result = toggle_prefix_emoji("task", "🏷️")
    result = toggle_prefix_emoji(result, "✔️")
    assert result.startswith("✔️ 🏷️")
    styled = ":red[**task**]"
    result = toggle_prefix_emoji(styled, "✔️")
    assert result.startswith(":red[**✔️ task**]")
