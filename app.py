import streamlit as st
import time
from pathlib import Path
from utils.page_generator import *
from utils.page_template import *

def style_page():
    '''
    Initializes the content and style for the page text.
    '''
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
        p.centered {
            font-size: 18px;
            color: #666;
            margin-top: -15px;
        }
        /* Remove border, padding, and shadow from the form */
        div[data-testid="stForm"] {
            border: none !important;
            padding: 0 !important;
            box-shadow: none !important;
        }

        /* Remove padding from the form submit button */
        button[kind="primaryFormSubmit"] {
            margin-top: 10px !important;
            padding: 8px 16px !important;
            border-radius: 5px !important;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
    # Centered container
    st.markdown('<div class="centered">', unsafe_allow_html=True)
    # Title
    st.markdown('<h1 class="centered">Infipedia</h1>', unsafe_allow_html=True)
    st.markdown('<p class=centered>The Free (Infinite) Encyclopedia</p>', unsafe_allow_html=True)

    # Search form
    with st.form(key="search_form"):
        query = st.text_input("Search and learn something new", key="search_query")
        # Submit button inside the form
        submit = st.form_submit_button(label="Search")
    st.markdown('</div>', unsafe_allow_html=True)

    return query, submit


def change_label_style(label, font_size='12px', font_color='white'):
    '''
    A helper function to initialize the style for the search bar label.
    '''
    html = f"""
    <script>
        var elems = window.parent.document.querySelectorAll('p');
        var elem = Array.from(elems).find(x => x.innerText == '{label}');
        elem.style.fontSize = '{font_size}';
        elem.style.color = '{font_color}';
    </script>
    """
    st.components.v1.html(html)


# Dynamic page creation
def create_new_page(search_query):
    '''
    Creates a new page based on a search query and redirects the user to that page.

    Args:
        :search_query (str): A search query to be parsed as input for content generation
    '''
    # Get title for page
    page_title = generate_title(search_query)

    # Define the file path
    fname = page_title.replace(" ", "")
    file_path = f"pages/{fname}.py"
    
    # Create new file & write the page content to the file
    Path(file_path).touch()
    with open(file_path, "w") as file:
        page_content = get_template(title=page_title, search_query=search_query)
        file.write(page_content)
    
    # Wait until the file is populated
    start_time = time.time()
    last_size = -1

    while True:
        # Check if the file exists
        if os.path.exists(file_path):
            # Get the current file size
            current_size = os.path.getsize(file_path)

            # If size hasn't changed for two consecutive checks, assume it's ready
            if current_size == last_size:
                time.sleep(3)
                st.switch_page(file_path)
            last_size = current_size
        else:
            # File doesn't exist yet, continue waiting
            pass

        # Timeout handling
        if time.time() - start_time > 30:
            raise TimeoutError(f"Request Timeout: File {file_path} did not stabilize within 30 seconds. Try again.")

        time.sleep(0.1)


def main():
    # Initialize page style
    st.set_page_config(initial_sidebar_state="collapsed")
    query, submit = style_page()

    # Redirect on submit button click
    if submit and query:
        create_new_page(query)

if __name__ == "__main__":
    main()