import streamlit as st

st.title("My To-DO List Creator")

if "my_todo_list" not in st.session_state:
    st.session_state.my_todo_list = ["Buy groceries", "Learn Stramlit", "Learn Python"]
# st.write("My current To-Do list is: ", st.session_state.my_todo_list)
new_todo = st.text_input("What do you need to do?")

if st.button("Add the new To-Do item"):
    st.write("Adding a new item to the list")
    st.session_state.my_todo_list.append(new_todo)

st.write("My new To-Do list is:", st.session_state.my_todo_list)