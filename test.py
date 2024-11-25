import streamlit as st

# Define your functions
def greet():
    st.write("Hello! This is the result of the `greet` function!")

def show_info():
    st.write("Here's some information from the `show_info` function.")

# Helper function to call appropriate actions
def handle_action(action):
    if action == "greet":
        greet()
    elif action == "info":
        show_info()
    else:
        st.write("Click on a link to perform an action.")

# Read query parameters
query_params = st.experimental_get_query_params()
action = query_params.get("action", [None])[0]

# Display the content based on the action
handle_action(action)

# Inline clickable text
st.markdown(
    """
    This is some inline text where you can 
    [greet someone](?action=greet) or 
    [get more information](?action=info).
    """,
    unsafe_allow_html=True,
)