import streamlit as st

# Initialize session state
if "tasks" not in st.session_state:
    st.session_state.tasks = []

st.set_page_config(
    page_title="To-Do List",
    page_icon="📝",
    layout="centered"
)

st.title("📝 To-Do List App")
st.write("Manage your daily tasks with ease.")

# -----------------------
# Add Task
# -----------------------
st.subheader("➕ Add Task")

new_task = st.text_input("Enter a new task")

if st.button("Add Task"):
    if new_task.strip():
        st.session_state.tasks.append(new_task)
        st.success("Task added successfully!")
        st.rerun()
    else:
        st.warning("Please enter a task.")

st.divider()

# -----------------------
# View Tasks
# -----------------------
st.subheader("📋 Your Tasks")

if st.session_state.tasks:

    for i, task in enumerate(st.session_state.tasks):

        col1, col2, col3 = st.columns([6,2,2])

        with col1:
            st.write(f"**{i+1}. {task}**")

        # Update
        with col2:
            if st.button("Edit", key=f"edit{i}"):
                st.session_state.edit_index = i

        # Delete
        with col3:
            if st.button("Delete", key=f"delete{i}"):
                st.session_state.tasks.pop(i)
                st.success("Task deleted.")
                st.rerun()

else:
    st.info("No tasks available.")

st.divider()

# -----------------------
# Update Task
# -----------------------
if "edit_index" in st.session_state:

    index = st.session_state.edit_index

    st.subheader("✏️ Update Task")

    updated_task = st.text_input(
        "Modify Task",
        value=st.session_state.tasks[index]
    )

    col1, col2 = st.columns(2)

    with col1:
        if st.button("Save Changes"):

            if updated_task.strip():
                st.session_state.tasks[index] = updated_task
                del st.session_state.edit_index
                st.success("Task updated successfully!")
                st.rerun()

    with col2:
        if st.button("Cancel"):
            del st.session_state.edit_index
            st.rerun()

st.divider()

# -----------------------
# Footer
# -----------------------
st.caption("Built with ❤️ using Python & Streamlit")