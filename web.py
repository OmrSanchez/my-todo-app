import streamlit as st
import functions

todos = functions.get_todos()

def add_todo():
    todo_local = st.session_state["new_todo"] + "\n"
    print(todo_local)
    todos.append(todo_local)
    functions.write_todos(todos)

st.title("My Todo App")
st.subheader("This is my todo app.")

for index, task in enumerate(todos):
    checkbox = st.checkbox(task, key=task)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[task]
        st.rerun()

st.text_input(label="Enter a todo:", placeholder="Add new todo...",
              on_change=add_todo, key='new_todo')