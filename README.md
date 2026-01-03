# 📋 TO-DO-list

## Applicazione per Gestire Task facilmente

## 🌐 Live Demo

(WIP, da aggiornare)
Prova l'applicazione online su: [Streamlit Cloud](https://to-do-list-hccwvjcjm4vu6z2kewxsqj.streamlit.app)

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
- **Etichetta**: Attribuisce un'etichetta ad un elemento per specificarne la priorità rispetto agli altri.
- **Modifica Stile**: Applica Grassetto/Italics/Colore all'elemento selezionato

## 🔗 Come è strutturato il progetto

```
🌐TO-DO-LIST
    │
    ├── .devcontainer                     # Demo Cloud Streamlit
    │
    ├── 🛠 todo_app/                       # Cartella App
    │       ├── 💻 screens/               # Cartella pagine app
    │       │       ├── 🏠 home.py        # Gestione Homepage
    │       │       └── 👋 welcome.py     # Welcome message
    │       │
    │       ├── ⛓️ sidebar/                # Cartella Funzioni Sidebar
    │       │       ├── 🔘 elements.py    # Funzioni Elementi Lista
    │       │       ├── 📁 folders.py     # Funzioni Cartelle
    │       │       ├── ℹ️ info.py        # Info Funzioni
    │       │       └── 📄 lists.py        # Funzioni Lista
    │       │
    │       ├── ⁉️ utils/                 # Cartella Supporto Funzioni
    │       │       └── 🤲 helpers.py     # Subroutines di alcune Funzioni
    │       │
    │       ├── ⚙️ config.py              # Configurazione App
    │       └── 📱 main.py                # Avvio app
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

- **streamlit**: Interfaccia web interattiva

3. **Avvia l'app:**

```bash
streamlit run ToDoList.py
```

## 📝 Unit-Tests
WIP (Una volta finito il tutto, aggiungere informazioni sugli Unit Test e come eseguirli da terminale)

## 👨‍💻 Autori

- **[@Dani220406](https://github.com/Dani220406)**
- **[@MrMelus](https://github.com/MrMelus)**
- **[@BecherLiaoumi](https://github.com/BecherLiaoumi)**

---

🏅 *Progetto realizzato per il corso Quality Development 2025/2026 del DMI UNICT*