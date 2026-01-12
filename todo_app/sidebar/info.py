import streamlit as st


def info():
    with st.sidebar.expander("ℹ️ Info", expanded=False):
        st.markdown("""
        *Puoi ingrandire la dimensione della sidebar con drag del mouse*

        **HOMEPAGE**
        - **Nuova lista**: Crea una nuova TO-DO list inserendone il nome.
        - **Elimina lista**: Elimina la TO-DO list selezionata.
        - **Crea nuova cartella**: Crea una nuova cartella inserendone il nome.
        - **Gestione cartelle**: Sposta una lista nella cartella selezionata.
        - **Elimina cartella**: Permette di eliminare la cartella selezionata senza cancellarne le liste contenute.
        - **Le mie cartelle**: Visualizza le cartelle create con le relative liste inserite al loro interno.

        **LIST-PAGE**
        - **Torna alla Homepage**: Salva le modifiche applicate alla lista e torna alla homepage.
        - **Aggiungi elemento**: Aggiunge un nuovo elemento nella lista inserendone il nome.
        - **Modifica elemento**: Modifica il testo di un elemento nella lista.
        - **Elimina elemento**: Elimina un elemento selezionato.
        - **Ordina elemento**: Cambia l'ordine degli elementi nella lista.
        - **Task completato**: Segna un elemento nella lista come completato.
        - **Etichetta**: Attribuisce un'etichetta ad un elemento per simboleggiarne la priorità rispetto agli altri.
        - **Modifica Stile**: Applica Grassetto/Italics/Colore all'elemento selezionato.

        Buon Lavoro 😊! 
        """)
    st.sidebar.markdown("---")
