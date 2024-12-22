import streamlit as st
import time
from pathlib import Path
from utils.page_generator import *
from utils.page_template import *
  
def style_page():
    '''
    Initalizes the content and style for the page text.
    '''
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
        p.centered {
            font-size: 18px;
            color: #666;
            margin-top: -15px;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
    # Centered container
    st.markdown('<div class="centered">', unsafe_allow_html=True)
    # Title
    st.markdown('<h1 class="centered">Infipedia</h1>', unsafe_allow_html=True)
    st.markdown('<p class=centered>The Free (infinite) Encyclopedia', unsafe_allow_html=True)

    # Set style for search bar label
    label = "Search and learn something new"
    change_label_style(label, '18px')
    query = st.text_input(label, key="search_query")

    return query

# Search bar
def change_label_style(label, font_size='12px', font_color='white'):
    '''
    A helper function to initalize the style for the search bar label.

    Args:
        :label (str): Value for label css attribute
        :font_size (str): Value for font_size css attribute
        :font_color (str): Value for font_color css attribute
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
    

    # Redirect to the new page upon creation
    start_time = time.time()
    last_size = -1

    while True:
        # Check if the file exists
        if os.path.exists(file_path):
            # Get the current file size
            current_size = os.path.getsize(file_path)

            # If size hasn't changed for two consecutive checks, assume it's ready
            if current_size == last_size:
                print(current_size, last_size)
                time.sleep(3)
                st.switch_page(file_path)
            last_size = current_size
        else:
            # File doesn't exist yet, continue waiting
            pass

        # Timeout handling
        if time.time() - start_time > 30:
            print("Request Timeout: File {file_path} did not stabilize within 30 seconds. Try again.")

        time.sleep(0.1)


def main():
    # Initalizing page content and style
    query = style_page()

    # Redirect on submit button click
    if st.button("Search"):
        if query:
            create_new_page(query)

    st.markdown('</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()