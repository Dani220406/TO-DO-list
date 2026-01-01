# 📋 TO-DO-list

## Applicazione per Gestire Task facilmente

## 🌐 Live Demo

Puoi testare l'applicazione online su [Streamlit Cloud](https://to-do-list-hccwvjcjm4vu6z2kewxsqj.streamlit.app)

## 📃 Indice

- [Come funziona l'app](#come-funziona-lapp)
- [Come è strutturato il progetto](#come-è-strutturato-il-progetto)
- [Installazione delle dipendenze](#installazione-delle-dipendenze)
- [Unit-Tests](#unit-tests)
- [Autori](#autori)

## 🔍 Come funziona l'app

Abbiamo diviso l'app in due "layer", una homepage ed una list-page (in cui è possibile eseguire azioni sugli elementi delle TO-DO lists).

### Homepage

E' la pagina che si apre successivamente al messaggio di benvenuto nell'app. Nella homepage è possibile eseguire azioni generali sulle TO-DO lists; nello specifico:

- **Crea nuova lista**: Permette di creare una nuova TO-DO list inserendone il nome. Non possono essere create due liste con lo stesso nome.
- **Elimina lista**: Permette di eliminare la TO-DO list selezionata nel menù a tendina. Se non è stata creata alcuna lista, spunterà la scritta *Nessuna lista da eliminare*.
- **Crea nuova cartella**: Permette di creare una nuova cartella inserendone il nome. Non possono essere create due cartelle con lo stesso nome.
- **Le mie cartelle**: Permette di vedere le cartelle create con le relative liste inserite al loro interno. Questa funzione è visibile solo una volta creata una cartella.
- **Gestione cartelle**: Permette di spostare una lista nella cartella selezionata nel menù a tendina. (L'implementazione di funzionalità drag & drop avrebbe richiesto maggiore complessità di codice, abbiamo preferito mantenere il tutto semplice)
- **Elimina cartella**: Permette di eliminare la cartella selezionata nel menù a tendina, senza cancellare le liste contenute all'interno. Questa funzione è visibile solo una volta creata una cartella.

### List-Page

E' la pagina che si apre quando viene selezionata una TO-DO list da visualizzare. Nella List-Page è possibile eseguire azioni sugli elementi relativi alla TO-DO lists selezionata; nello specifico:

- **Torna alle liste**: Permette di salvare le modifiche applicate alla lista e tornare alla homepage.
- **Aggiungi elemento**: Permette di aggiungere un nuovo elemento nella lista inserendone il nome.
- **Elimina elemento**: Permette di eliminare un elemento selezionato nel menù a tendina.
- **Task completato**: Permette di segnare un elemento nella lista come completato.
- **Etichetta**: Permette di attribuire un'etichetta ad un elemento per specificarne la priorità rispetto agli altri.

## 🔗 Come è strutturato il progetto
WIP (Una volta finito il tutto, speccificare i contenuti/directory relative alla repository)

## ⬇️ Installazione delle dipendenze

### Prerequisiti

- Python 3.12.3 (consigliato)
- pip (package manager)

### Setup dipendenze

1. **Clona il repository:**

```bash
git clone https://github.com/Dani220406/TO-DO-list.git
cd TO-DO-list
```

2. **Installa le dipendenze:**

```bash
pip install -r requirements.txt
```

- **streamlit**: Interfaccia web interattiva
-

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