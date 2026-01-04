import streamlit as st

# Initialize task list in memory
if "tasks" not in st.session_state:
    st.session_state.tasks = []

st.title("🧠 Task Manager + Pomodoro")

st.header("📋 Tasks")
new_task = st.text_input("Enter a new task")

if st.button("Add Task"):
    if new_task.strip() != "":
        st.session_state.tasks.append(
            {"title": new_task, "done": False}
        )
st.subheader("Your Tasks")

for i, task in enumerate(st.session_state.tasks):
    col1, col2 = st.columns([8, 1])

    # Checkbox auto-ticks and stores state
    task["done"] = col1.checkbox(
        task["title"],
        value=task["done"],
        key=f"task_{i}"
    )

    if col2.button("🗑️", key=f"delete_{i}"):
        st.session_state.tasks.pop(i)
        st.rerun()

st.header("⏱️ Pomodoro Timer")
st.write("Timer coming here")