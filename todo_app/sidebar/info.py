import streamlit as st


def info():
    with st.sidebar.expander("ℹ️ Info", expanded=False):
        st.markdown(
            """
        *You can adjust the dimensions of the sidebar by dragging the mouse.*

        **HOMEPAGE**
        - **Create New List**: Creates a new TO-DO List by adding its name.
        - **Delete List**: Deletes the selected TO-DO List.
        - **Create New Folder**: Creates a new folder by adding its name.
        - **Manage Folders**: Moves a TO-DO List into the chosen folder.
        - **Delete Folder**: Allows to delete the selected folder whilst preserving its contents.
        - **My Folders**: Shows the created folders alongside its contents.

        **LIST-PAGE**
        - **Back to Homepage**: Saves the updated contents of the TO-DO List and returns back to the Homepage.
        - **Add Element**: Creates a new element in the TO-DO List by adding its name.
        - **Edit Element**: Allows to edit the text of the selected element.
        - **Delete Element**: Deletes the selected element.
        - **Order Elements**: Allows to change the order of elements within the TO-DO List.
        - **Complete Task**: Marks the selected task as completed.
        - **Label**: Adds a label to the selected element to simbolize its priority compared to other elements.
        - **Edit Style**: Allows to add Bold/Italics/Text-Color to the selected element.

        Have Fun 😊!
        """
        )
    st.sidebar.markdown("---")
