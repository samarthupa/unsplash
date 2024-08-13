import streamlit as st
import webbrowser

def main():
    st.title("Keyword-Based Image Search")
    st.write("Enter a keyword to search for images on Unsplash.")

    keyword = st.text_input("Keyword")

    if st.button("Search"):
        if keyword:
            # Create the URL with the entered keyword
            url = f"https://unsplash.com/s/photos/{keyword}?license=free&orientation=portrait"
            
            # Open the URL in a new browser tab
            webbrowser.open(url, new=2)
            
            st.success(f"Opening search results for '{keyword}' in your browser.")
        else:
            st.error("Please enter a keyword.")

if __name__ == "__main__":
    main()
