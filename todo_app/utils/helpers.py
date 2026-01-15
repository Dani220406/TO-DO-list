# Method to keep track of changes applied to text
def parse_styled_text(s):
    color = None
    bold = False
    italic = False
    text = s

    if text.startswith(":") and "[" in text and text.endswith("]"):
        color = text[1:].split("[", 1)[0]
        text = text.split("[", 1)[1][:-1]

    if text.startswith("**") and text.endswith("**"):
        bold = True
        text = text[2:-2]

    if text.startswith("*") and text.endswith("*"):
        italic = True
        text = text[1:-1]

    return {"text": text, "bold": bold, "italic": italic, "color": color}


# -------------------------------------------------------------


# Method to apply text edits to elements
def build_styled_text(d):
    t = d["text"]
    if d.get("bold"):
        t = f"**{t}**"
    if d.get("italic"):
        t = f"*{t}*"
    if d.get("color") and d["color"] != "none":
        t = f":{d['color']}[{t}]"
    return t


# -------------------------------------------------------------


# Method to manage conflict between emojis and * characters + emoji priority
def toggle_prefix_emoji(task, emoji):
    parsed = parse_styled_text(task)
    text = parsed["text"]

    EMOJIS_ORDER = ["✔️", "🏷️"]
    words = text.split()
    emojis_present = {e for e in EMOJIS_ORDER if e in words}
    words = [w for w in words if w not in EMOJIS_ORDER]

    if emoji in emojis_present:
        emojis_present.remove(emoji)
    else:
        emojis_present.add(emoji)

    ordered_emojis = [e for e in EMOJIS_ORDER if e in emojis_present]
    text = " ".join(ordered_emojis + words)

    return build_styled_text(
        {
            "text": text,
            "bold": parsed["bold"],
            "italic": parsed["italic"],
            "color": parsed["color"],
        }
    )
