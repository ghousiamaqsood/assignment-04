# import streamlit as st
# import pandas as pd
# import json
# import os
# import datetime 
# import time
# import random
# import plotly.express as px
# import plotly.graph_objects as go
# import requests
# from streamlit_lottie import st_lottie

# # Page Configuration
# st.set_page_config(
#     page_title="Personal Library Management System",
#     page_icon="📚",
#     layout="wide",
#     initial_sidebar_state="expanded",
# )

# # --- Session State Initialization ---
# if 'library' not in st.session_state:
#     st.session_state.library = []
# if 'book_removed' not in st.session_state:
#     st.session_state.book_removed = False
# if 'current_view' not in st.session_state:
#     st.session_state.current_view = 'home'
# if 'search_result' not in st.session_state:
#     st.session_state.search_result = []
# if 'book_added' not in st.session_state:
#     st.session_state.book_added = False
# if 'book_updated' not in st.session_state:
#     st.session_state.book_updated = False
# if 'current_book' not in st.session_state:
#     st.session_state.current_book = "library"

# # --- Utility Functions ---
# def load_library():
#     try:
#         with open("library.json", "r") as f:
#             return json.load(f)
#     except FileNotFoundError:
#         return []

# def save_library():
#     with open("library.json", "w") as f:
#         json.dump(st.session_state.library, f)

# def remove_book(index):
#     if 0 <= index < len(st.session_state.library):
#         del st.session_state.library[index]
#         save_library()
#         return True
#     return False

# def search_books(search_term, search_by):
#     search_result = []
#     for book in st.session_state.library:
#         if search_by == "Title" and search_term.lower() in book['title'].lower():
#             search_result.append(book)
#         elif search_by == "Author" and search_term.lower() in book['author'].lower():
#             search_result.append(book)
#         elif search_by == "Genre" and search_term.lower() in book['genre'].lower():
#             search_result.append(book)
#     st.session_state.search_result = search_result

# def add_book(title, author, genre, year):
#     new_book = {
#         "title": title,
#         "author": author,
#         "genre": genre,
#         "read_status": False,
#         "published_year": year
#     }
#     st.session_state.library.append(new_book)
#     save_library()

# # --- UI Layout ---
# st.markdown("""
# <style>
#     .main_header {
#         font-size: 3rem !important;
#         color: #FF4B4B !important;
#         text-align: center !important;
#         text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.1);
#     }
#     .sub_header2 {
#         font-size: 2rem !important;
#         color: #FF4B4B !important;
#         margin-top: 1rem;
#         margin-bottom: 1rem;
#         font-weight: bold;
#     }
#     .book-card {
#         background-color: #F3F4F6;
#         border-radius: 0.5rem;
#         padding: 1rem;
#         border-left: 5px solid #3B82F6;
#         transition: all 0.3s ease;
#     }
#     .read-badge {
#         background-color: #10B981;
#         color: white;
#         padding: 0.25rem 0.875rem;
#         border-radius: 1rem;
#         font-size: 0.75rem;
#         font-weight: bold;
#     }
# </style>
# """, unsafe_allow_html=True)

# st.markdown("<h1 class='main_header'>Personal Library Management System</h1>", unsafe_allow_html=True)

# # --- Main Navigation ---
# view = st.sidebar.radio("Choose view", ["Library", "Search Book", "Add Book", "Statistics"])

# # --- Views ---
# if view == "Add Book":
#     st.markdown("<h2 class='sub_header2'>Add a New Book</h2>", unsafe_allow_html=True)
#     title = st.text_input("Title")
#     author = st.text_input("Author")
#     genre = st.text_input("Genre")
#     published_year = st.text_input("Published Year")

#     if st.button("Add Book"):
#         add_book(title, author, genre, published_year)
#         st.success(f"Book '{title}' added successfully!")

# elif view == "Library":
#     st.header("Library")
#     if st.session_state.library:
#         for i, book in enumerate(st.session_state.library):
#             with st.container():
#                 st.markdown(f"**Title:** {book['title']}  \n**Author:** {book['author']}  \n**Genre:** {book['genre']}  \n**Year:** {book['published_year']}  \n**Status:** {'✅ Read' if book['read_status'] else '❌ Unread'}")

#                 col1, col2 = st.columns(2)
#                 with col1:
#                     if st.button("Remove Book", key=f"remove_{i}"):
#                         if remove_book(i):
#                             st.success("Book removed.")
#                             st.rerun()
#                 with col2:
#                     new_status = not book['read_status']
#                     status_label = "Mark as Read" if not book['read_status'] else "Mark as Unread"
#                     if st.button(status_label, key=f"status_{i}"):
#                         st.session_state.library[i]['read_status'] = new_status
#                         save_library()
#                         st.rerun()
#     else:
#         st.info("Library is empty.")

# elif view == "Search Book":
#     st.header("Search for a Book")
#     search_by = st.selectbox("Search By", ["Title", "Author", "Genre"])
#     search_term = st.text_input("Enter Search Term:")

#     if st.button("Search"):
#         if search_term:
#             with st.spinner("Searching..."):
#                 time.sleep(0.5)
#                 search_books(search_term, search_by)

#     if st.session_state.search_result:
#         for book in st.session_state.search_result:
#             st.markdown(f"**{book['title']}** by *{book['author']}* — {book['genre']} ({book['published_year']})")

# elif view == "Statistics":
#     st.header("Library Statistics")
#     if st.session_state.library:
#         genre_counts = {}
#         for book in st.session_state.library:
#             genre = book['genre']
#             genre_counts[genre] = genre_counts.get(genre, 0) + 1

#         fig = px.bar(
#             x=list(genre_counts.keys()),
#             y=list(genre_counts.values()),
#             labels={"x": "Genre", "y": "Number of Books"},
#             title="Books by Genre"
#         )
#         st.plotly_chart(fig)
#     else:
#         st.info("No data available for statistics.")
#         # Load library data
# def load_library():
#     try:
#         with open("library.json", "r") as f:
#             return json.load(f)
#     except FileNotFoundError:
#         return []

# # Save library data
# def save_library():
#     with open("library.json", "w") as f:
#         json.dump(st.session_state.library, f)

# # Remove a book
# def remove_book(index):
#     del st.session_state.library[index]
#     save_library()
#     return True

# # Search books
# def search_books(search_term, search_by):
#     search_result = []
#     for book in st.session_state.library:
#         if search_by == "Title" and search_term.lower() in book['title'].lower():
#             search_result.append(book)
#         elif search_by == "Author" and search_term.lower() in book['author'].lower():
#             search_result.append(book)
#         elif search_by == "Genre" and search_term.lower() in book['genre'].lower():
#             search_result.append(book)
#     st.session_state.search_result = search_result

# # Set up session state
# if "library" not in st.session_state:
#     st.session_state.library = load_library()

# # Add book feature (for demo purposes)
# def add_book(title, author, genre, year):
#     new_book = {
#         "title": title,
#         "author": author,
#         "genre": genre,
#         "read_status": False,
#         "published_year": year
#     }
#     st.session_state.library.append(new_book)
#     save_library()

# # Streamlit UI
# st.title("Library Management System")
# st.sidebar.title("Navigation")
# view = st.sidebar.radio("Choose view", ["Library", "Search Book", "Add Book", "Statistics"])

# # Add Book
# if view == "Add Book":
#     st.header("Add a New Book")
#     title = st.text_input("Title")
#     author = st.text_input("Author")
#     genre = st.text_input("Genre")
#     published_year = st.text_input("Published Year")
    
#     if st.button("Add Book"):
#         add_book(title, author, genre, published_year)
#         st.success(f"Book '{title}' added successfully!")

# # Library View
# elif view == "Library":
#     st.header("Library")
#     if st.session_state.library:
#         for i, book in enumerate(st.session_state.library):
#             col1, col2 = st.columns(2)
#             with col1:
#                 # st.markdown(f"""



# # Initialize view variable
#                              view = st.selectbox("Select View", ["Library", "Search Book", "Statistics",])

# # Library view
# if view == "Library":
#     for i, book in enumerate(st.session_state.library):
#         st.markdown(f"""
#         <div class='book-card'>
#             <h3>{book['title']}</h3>
#             <p><strong>Author:</strong> {book['author']}</p>
#             <p><strong>Genre:</strong> {book['genre']}</p>
#             <p><strong>Read Status:</strong> {"Read" if book["read_status"] else "Unread"}</p>
#             <p><strong>Published Year:</strong> {book['published_year']}</p>
#         </div>
#         """, unsafe_allow_html=True)

#         col1, col2 = st.columns(2)
#         with col1:
           
#             if st.button("Remove Book", key=f"remove_{i}", use_container_width=True):
#                 if remove_book(i):
                    
                    
#                     st.session_state.book_removed = True
#         with col2:
#             new_status = not book['read_status']
#             status_label = "Mark as Read" if not book['read_status'] else "Mark as Unread"
#             if st.button(status_label, key=f"status_{i}", use_container_width=True):
#                 st.session_state.library[i]['read_status'] = new_status
#                 save_library()
#                 st.rerun()

# # Search Book
# elif view == "Search Book":
#     st.header("Search for a Book")
#     search_by = st.selectbox("Search By", ["Title", "Author", "Genre"])
#     search_term = st.text_input("Enter Search Term:")

#     if st.button("Search"):
#         if search_term:
#             with st.spinner("Searching..."):
#                 time.sleep(0.5)
#                 search_books(search_term, search_by)

#     if hasattr(st.session_state, 'search_result') and st.session_state.search_result:
#         for book in st.session_state.search_result:
#             st.markdown(f"""
#             <div class='book-card'>
#                 <h3>{book['title']}</h3>
#                 <p><strong>Author:</strong> {book['author']}</p>
#                 <p><strong>Genre:</strong> {book['genre']}</p>
#                 <p><strong>Read Status:</strong> {"Read" if book["read_status"] else "Unread"}</p>
#                 <p><strong>Published Year:</strong> {book['published_year']}</p>
#             </div>
#             """, unsafe_allow_html=True)

# # Statistics
# elif view == "Statistics":
#     st.header("Library Statistics")
#     stats = {
#         'total_books': len(st.session_state.library),
#         'read_books': len([book for book in st.session_state.library if book['read_status']]),
#         'percentage_read': (len([book for book in st.session_state.library if book['read_status']]) / len(st.session_state.library) * 100) if st.session_state.library else 0
#     }
#     col1, col2, col3 = st.columns(3)
#     with col1:
#         st.metric("Total Books", stats['total_books'])
#     with col2:
#         st.metric("Read Books", stats['read_books'])
#     with col3:
#         st.metric("Percentage Read", f"{stats['percentage_read']:.1f}%")

# # Footer
# st.markdown("Copyright @ 2025, Ghousia Maqsood, Personal Library Management System, All rights reserved", unsafe_allow_html=True)



import streamlit as st
import pandas as pd
import json
import os
import datetime
import time
import random
import plotly.express as px
import plotly.graph_objects as go
import requests
from streamlit_lottie import st_lottie

# --- Page Configuration ---
st.set_page_config(
    page_title="Personal Library Management System",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded",
)

# --- Session State Initialization ---
if 'library' not in st.session_state:
    try:
        with open("library.json", "r") as f:
            st.session_state.library = json.load(f)
    except FileNotFoundError:
        st.session_state.library = []

if 'search_result' not in st.session_state:
    st.session_state.search_result = []

# --- Utility Functions ---
def save_library():
    with open("library.json", "w") as f:
        json.dump(st.session_state.library, f)

def remove_book(index):
    if 0 <= index < len(st.session_state.library):
        del st.session_state.library[index]
        save_library()
        return True
    return False

def search_books(search_term, search_by):
    search_result = []
    for book in st.session_state.library:
        if search_by == "Title" and search_term.lower() in book['title'].lower():
            search_result.append(book)
        elif search_by == "Author" and search_term.lower() in book['author'].lower():
            search_result.append(book)
        elif search_by == "Genre" and search_term.lower() in book['genre'].lower():
            search_result.append(book)
    st.session_state.search_result = search_result

def add_book(title, author, genre, year):
    new_book = {
        "title": title,
        "author": author,
        "genre": genre,
        "read_status": False,
        "published_year": year
    }
    st.session_state.library.append(new_book)
    save_library()

# --- UI Styling ---
st.markdown("""
<style>
    .main_header {
        font-size: 3rem !important;
        color: #FF4B4B !important;
        text-align: center !important;
    }
    .sub_header2 {
        font-size: 2rem !important;
        color: #FF4B4B !important;
        margin-top: 1rem;
        margin-bottom: 1rem;
        font-weight: bold;
    }
    .book-card {
        background-color: #F3F4F6;
        border-radius: 0.5rem;
        padding: 1rem;
        border-left: 5px solid #3B82F6;
    }
</style>
""", unsafe_allow_html=True)

st.markdown("<h1 class='main_header'>Personal Library Management System</h1>", unsafe_allow_html=True)

# --- Main Navigation ---
st.sidebar.title("Navigation")
view = st.sidebar.radio("Choose view", ["Library", "Search Book", "Add Book", "Statistics"])

# --- Add Book View ---
if view == "Add Book":
    st.markdown("<h2 class='sub_header2'>Add a New Book</h2>", unsafe_allow_html=True)
    title = st.text_input("Title")
    author = st.text_input("Author")
    genre = st.text_input("Genre")
    published_year = st.text_input("Published Year")

    if st.button("Add Book"):
        if title and author and genre and published_year:
            add_book(title, author, genre, published_year)
            st.success(f"Book '{title}' added successfully!")
        else:
            st.warning("Please fill all the fields!")

# --- Library View ---
elif view == "Library":
    st.header("Library")
    if st.session_state.library:
        for i, book in enumerate(st.session_state.library):
            st.markdown(f"""
            <div class='book-card'>
                <h3>{book['title']}</h3>
                <p><strong>Author:</strong> {book['author']}</p>
                <p><strong>Genre:</strong> {book['genre']}</p>
                <p><strong>Read Status:</strong> {"✅ Read" if book["read_status"] else "❌ Unread"}</p>
                <p><strong>Published Year:</strong> {book['published_year']}</p>
            </div>
            """, unsafe_allow_html=True)

            col1, col2 = st.columns(2)
            with col1:
                if st.button("Remove Book", key=f"remove_{i}"):
                    if remove_book(i):
                        st.success("Book removed.")
                        st.rerun()
            with col2:
                new_status = not book['read_status']
                status_label = "Mark as Read" if not book['read_status'] else "Mark as Unread"
                if st.button(status_label, key=f"status_{i}"):
                    st.session_state.library[i]['read_status'] = new_status
                    save_library()
                    st.rerun()
    else:
        st.info("Library is empty.")

# --- Search Book View ---
elif view == "Search Book":
    st.header("Search for a Book")
    search_by = st.selectbox("Search By", ["Title", "Author", "Genre"])
    search_term = st.text_input("Enter Search Term:")

    if st.button("Search"):
        if search_term:
            with st.spinner("Searching..."):
                time.sleep(0.5)
                search_books(search_term, search_by)

    if st.session_state.search_result:
        for book in st.session_state.search_result:
            st.markdown(f"**{book['title']}** by *{book['author']}* — {book['genre']} ({book['published_year']})")

# --- Statistics View ---
elif view == "Statistics":
    st.header("Library Statistics")
    if st.session_state.library:
        genre_counts = {}
        for book in st.session_state.library:
            genre = book['genre']
            genre_counts[genre] = genre_counts.get(genre, 0) + 1

        fig = px.bar(
            x=list(genre_counts.keys()),
            y=list(genre_counts.values()),
            labels={"x": "Genre", "y": "Number of Books"},
            title="Books by Genre"
        )
        st.plotly_chart(fig)
    else:
        st.info("No data available for statistics.")
