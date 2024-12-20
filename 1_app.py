import streamlit as st
import pdfplumber

# Path to the PDF file
PDF_PATH = "UTILITIESCODE.pdf"

# Function to get the content of a specific page
@st.cache_data
def get_page_content(pdf_path, page_number):
    with pdfplumber.open(pdf_path) as pdf:
        if page_number < len(pdf.pages):
            page = pdf.pages[page_number]
            return page.extract_text()
        else:
            return None

# Function to get total number of pages
@st.cache_data
def get_total_pages(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        return len(pdf.pages)

# App layout
st.title("Utilities Code Search App")
st.markdown("Search the **Utilities Code** by specific pages or sections.")

# Get the total number of pages
total_pages = get_total_pages(PDF_PATH)

# User selects a page range
start_page, end_page = st.slider(
    "Select page range to search",
    min_value=1,
    max_value=total_pages,
    value=(1, 10),
    step=1,
)

# User enters a search query
search_query = st.text_input("Enter a keyword to search").lower()

# Display results
if search_query:
    st.subheader("Search Results")
    results_found = False

    for page_num in range(start_page - 1, end_page):
        content = get_page_content(PDF_PATH, page_num)
        if content and search_query in content.lower():
            results_found = True
            with st.expander(f"Page {page_num + 1}"):
                st.write(content)

    if not results_found:
        st.warning("No results found for your search query.")
