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
    col1, col2, col3 = st.columns([6, 1, 1])

    col1.write(
        "✅ " + task["title"] if task["done"] else "🔲 " + task["title"]
    )

    if col2.button("✔", key=f"done_{i}"):
        task["done"] = not task["done"]

    if col3.button("🗑️", key=f"delete_{i}"):
        st.session_state.tasks.pop(i)
        st.rerun()

st.header("⏱️ Pomodoro Timer")
st.write("Timer coming here")