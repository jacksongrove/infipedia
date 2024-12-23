import streamlit as st
import re
from app import create_new_page
from utils.page_generator import *

SEARCH_QUERY = """wolves"""
TITLE = """Wolf"""

st.set_page_config(initial_sidebar_state="collapsed")
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

# Check query parameters
query_params = st.query_params
linked_txt = query_params.get("action", None)

# Handle link clicks by dynamically calling `create_new_page`
if linked_txt:
    create_new_page(linked_txt)

# Generate & display content with working links
content = ""
content_placeholder = st.empty()
linked = False
linked_content = ""

for chunk in generate_content(TITLE, SEARCH_QUERY):
    chunk = chunk if chunk else ""

    # Track text between link delimiters
    if "[[" in chunk:
        linked = True
        linked_content += chunk
    # When delimiters end, replace tracked text with a working link
    elif linked and "]]" in chunk:
        linked_content += chunk

        # Regex to find and replace linked text
        pattern = r"\[\[(.*?)\]\]"
        processed_chunk = re.sub(
            pattern, 
            lambda m: f"[{m.group(1)}](?action={m.group(1).replace(' ', '_')})",
            linked_content
        )

        # Escape special characters
        processed_chunk = processed_chunk.replace("$", "\\$")

        # Append the processed link without delimiters
        content += processed_chunk
        content_placeholder.markdown(content, unsafe_allow_html=True)

        # Reset linked content tracking
        linked = False
        linked_content = ""

    # Add incomplete linked content to the buffer
    elif linked:
        linked_content += chunk
    # Otherwise, add normal chunks to content
    else:
        content += chunk
        content_placeholder.markdown(content, unsafe_allow_html=True)
