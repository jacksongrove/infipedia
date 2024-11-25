def get_template(content):
    page_template = f'''import streamlit as st
from app import create_new_page

CONTENT = """{content}"""
''' + r'''
st.markdown(
    """
    <style>
    .centered {
        display: flex;
        justify-content: center;
        align-items: center;
        flex-direction: column;
    }
    h1 {
        font-size: 70px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Centered container
st.markdown('<div class="centered">', unsafe_allow_html=True)

# Display content with links
st.markdown(CONTENT, unsafe_allow_html=True)

# Check query parameters
query_params = st.query_params
linked_txt = query_params.get("action", None)

# Handle link clicks by dynamically calling `create_new_page`
if linked_txt:
    st.write(f"Captured action: {linked_txt}")
    # You can also print it to the terminal for debugging
    print(f"Captured action parameter: {linked_txt}")
    file_path = create_new_page(linked_txt)
    st.switch_page(file_path)
    '''

    return page_template