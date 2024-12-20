import streamlit as st
import pdfplumber

# Function to extract and group content by titles
def extract_pdf_content(pdf_path):
    content = {}
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages[:5]:  # Process only the first 5 pages
            text = page.extract_text()
            if text:
                content[f"Page {page.page_number}"] = text.strip()
    return content

# Extract content from the PDF
pdf_file_path = "UTILITIESCODE.pdf"
pdf_content = extract_pdf_content(pdf_file_path)

# Streamlit App Layout
st.title("Utilities Code Search App")
st.markdown("Search the **Utilities Code** and view results grouped by chapters or sections.")

# Search bar
search_query = st.text_input("Enter search term", "").lower()

# Display results
if search_query:
    st.subheader("Search Results")
    results_found = False

    for title, text in pdf_content.items():
        if search_query in text.lower() or search_query in title.lower():
            results_found = True
            with st.expander(title):
                st.write(text)

    if not results_found:
        st.warning("No results found for your search query.")
