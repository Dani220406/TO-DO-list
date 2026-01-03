import streamlit as st

def info():
    with st.sidebar.expander("ℹ️ Info", expanded=False):
        st.markdown("""
        *Puoi ingrandire la dimensione della sidebar con drag del mouse*
                
        **HOMEPAGE**
        - **Crea nuova lista**: Crea una nuova TO-DO list inserendone il nome.
        - **Elimina lista**: Elimina la TO-DO list selezionata.
        - **Crea nuova cartella**: Crea una nuova cartella inserendone il nome.
        - **Le mie cartelle**: Visualizza le cartelle create con le relative liste inserite al loro interno.
        - **Gestione cartelle**: Sposta una lista nella cartella selezionata.
        - **Elimina cartella**: Permette di eliminare la cartella selezionata senza cancellarne le liste contenute.

        **LIST-PAGE**
        - **Torna alle liste**: Salva le modifiche applicate alla lista e tornare alla homepage.
        - **Aggiungi elemento**: Aggiunge un nuovo elemento nella lista inserendone il nome.
        - **Elimina elemento**: Eliminare un elemento selezionato.
        - **Task completato**: Segna un elemento nella lista come completato.
        - **Etichetta**: Attribuisce un'etichetta ad un elemento per specificarne la priorità rispetto agli altri.

        Buon Lavoro 😊! 
        """)
    st.sidebar.markdown("---")