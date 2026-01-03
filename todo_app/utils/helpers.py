# Funzione per tenere traccia delle modifiche applicate al testo
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

# Funzione per applicare le modifiche di testo agli elementi
def build_styled_text(d):
    t = d["text"]
    if d.get("bold"):
        t = f"**{t}**"
    if d.get("italic"):
        t = f"*{t}*"
    if d.get("color") and d["color"] != "nessuno":
        t = f":{d['color']}[{t}]"
    return t

# -------------------------------------------------------------

# Funzione per gestire conflitto emoji e caratteri *
def toggle_prefix_emoji(task, emoji):
    parsed = parse_styled_text(task)
    text = parsed["text"]

    if text.startswith(f"{emoji} "):
        text = text.replace(f"{emoji} ", "", 1)
    else:
        text = f"{emoji} {text}"

    return build_styled_text({"text": text, "bold": parsed["bold"], "italic": parsed["italic"], "color": parsed["color"]})