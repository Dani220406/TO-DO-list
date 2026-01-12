# 📋 TO-DO-list

## Applicazione per Gestire Task facilmente

## 🔍 Come funziona l'app

L'app è divisa in due "layers", una homepage ed una list-page.

### Homepage

Si apre dopo il messaggio di benvenuto. Nella homepage è possibile eseguire azioni generali sulle TO-DO lists; nello specifico:

- **Crea nuova lista**: Crea una nuova TO-DO list inserendone il nome.
- **Elimina lista**: Elimina la TO-DO list selezionata.
- **Crea nuova cartella**: Crea una nuova cartella inserendone il nome.
- **Gestione cartelle**: Sposta una lista nella cartella selezionata.
- **Elimina cartella**: Permette di eliminare la cartella selezionata senza cancellare le liste contenute all'interno.
- **Le mie cartelle**: Visualizza le cartelle create con le relative liste inserite al loro interno.

### List-Page

Si apre quando è selezionata una TO-DO list. Nella List-Page è possibile eseguire azioni sugli elementi della TO-DO list selezionata; nello specifico:

- **Torna alle liste**: Salva le modifiche applicate alla lista e tornare alla homepage.
- **Aggiungi elemento**: Aggiunge un nuovo elemento nella lista inserendone il nome.
- **Modifica elemento**: Modifica il testo di un elemento nella lista.
- **Elimina elemento**: Eliminare un elemento selezionato.
- **Ordina elemento**: Cambia l'ordine degli elementi nella lista.
- **Task completato**: Segna un elemento nella lista come completato.
- **Etichetta**: Attribuisce un'etichetta ad un elemento per simboleggiarne la priorità rispetto agli altri.
- **Modifica Stile**: Applica Grassetto/Italics/Colore all'elemento selezionato.

## 🔗 Come è strutturato il progetto

```
🌐TO-DO-LIST
    │
    ├── .devcontainer                     # Demo Cloud Streamlit
    │
    ├── 🛠 todo_app/                       # Cartella App
    │       ├── 💻 screens/               # Cartella pagine app
    │       │       ├── 🚧 __init__.py
    │       │       ├── 🏠 home.py        # Gestione Homepage
    │       │       └── 👋 welcome.py     # Welcome message
    │       │
    │       ├── ⛓️ sidebar/                # Cartella Funzioni Sidebar
    │       │       ├── 🚧 __init__.py
    │       │       ├── 🔘 elements.py    # Funzioni Elementi Lista
    │       │       ├── 📁 folders.py     # Funzioni Cartelle
    │       │       ├── ℹ️ info.py        # Info Funzioni
    │       │       └── 📄 lists.py        # Funzioni Lista
    │       │
    │       ├── ⁉️ utils/                 # Cartella Supporto Funzioni
    │       │       ├── 🚧 __init__.py
    │       │       └── 🤲 helpers.py     # Subroutines di alcune Funzioni
    │       │
    │       ├── 🚧 __init__.py
    │       ├── ⚙️ config.py              # Configurazione App
    │       └── 📱 main.py                 # File Main
    │
    ├── 🖥️ app.py                         # Avvio App
    │
    ├── 🔬 tests/                         # Cartella Unit-Tests
    │       ├── 🚧 __init__.py
    │       ├── 🏗️ test_config.py         # Unit-Test Funzioni config.py
    │       ├── 🏗️ test_elements.py       # Unit-Test Funzioni elements.py
    │       ├── 🏗️ test_folders.py        # Unit-Test Funzioni folders.py
    │       ├── 🏗️ test_helpers.py        # Unit-Test Funzioni helpers.py
    │       ├── 🏗️ test_home.py           # Unit-Test Funzioni home.py
    │       ├── 🏗️ test_info.py           # Unit-Test Funzioni info.py
    │       ├── 🏗️ test_lists.py          # Unit-Test Funzioni lists.py
    │       ├── 🏗️ test_main.py           # Unit-Test Funzioni main.py
    │       └── 🏗️ test_welcome.py        # Unit-Test Funzioni welcome.py
    │
    ├── 🚫 .gitignore                    # File Ignorati Git Push
    ├── 🔑 LICENSE                       # Licenza App
    ├── ✏️ README.md                     # Descrizione Progetto
    ├── 🔒 requirements_dev.txt          # Requisiti Unit-Tests
    └── 🔒 requirements.txt              # Requisiti App
```

## ⬇️ Installazione delle dipendenze

### Prerequisiti

- Python 3.12.3 (consigliato)
- pip (package manager)
- venv (consigliato creare un ambiente virtuale)

### Setup dipendenze

1. **Clona la repository:**

```bash
git clone https://github.com/Dani220406/TO-DO-list.git
cd TO-DO-list
```

2. **Installa le dipendenze:**

```bash
pip install -r requirements.txt
```

*oppure manualmente:*

```bash
pip install streamlit
```

3. **Avvia l'app:**

```bash
streamlit run app.py
```

## 📝 Unit-Tests
Abbiamo organizzato gli Unit-Test di tutte le funzioni usate nell'app nella cartella **tests/**. Per poter eseguire i test è necessario:

1. **Installa le dipendenze:**

```bash
pip install -r requirements_dev.txt
```

*oppure manualmente:*

```bash
pip install pytest pytest-mock pytest-cov pylint
```

2. **Esegui i Test:**

I test possono essere eseguiti o tutti contemporaneamente o singolarmente:

*Contemporaneamente:*

```bash
cd TO-DO-list
pytest tests/
pytest --cov=tests/
```

*Singolarmente:*

```bash
cd TO-DO-list
pytest tests/test_elements.py
pytest --cov=tests/test_elements.py
...
```

🏆 *La code coverage del Progetto raggiunge **~98%** !*

## 👨‍💻 Autori

- **[@Dani220406](https://github.com/Dani220406)**
- **[@MrMelus](https://github.com/MrMelus)**
- **[@BecherLiaoumi](https://github.com/BecherLiaoumi)**

---

🏅 *Progetto realizzato per il corso Quality Development 2025/2026 del DMI UNICT*