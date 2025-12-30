import streamlit as st

if 'my_lists' not in st.session_state:
    st.session_state.my_lists = []

def intestazione():
    col1,col2,col3 = st.columns(3)

    with col1:
        pass

    with col2:
        st.header("Benvenuto!")
        st.write("Vuoi creare una nuova lista?")
        new_list()
    
    with col3:
        st.write("")
        st.write("Le tue liste:")
        show_list()


def new_list():
    x = st.text_input("Come vuoi chiamare la lista?",key="input_nome")
    if (st.button("Conferma e crea")):
        if x:
            st.session_state.my_lists.append({"nome": x, "dati": []})
            st.success(f"lista '{x}' creata!")
        else:
            st.error("Devi scrivere un nome alla lista!")

def show_list(): 
    if st.session_state.my_lists:
        for i, lista in enumerate(st.session_state.my_lists):
            x = lista["nome"]
            if st.button(f"Apri {x}", key=f"btn_{i}"):
                st.write(f"Stai guardando la lista {x}")
    else:
        st.write("Non hai ancora creato liste")

def main():
    intestazione()


if __name__ == "__main__":
    main()