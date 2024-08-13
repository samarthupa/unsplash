import streamlit as st
import webbrowser

def generate_unsplash_url(keyword):
    # Generates a URL based on the provided keyword
    base_url = "https://unsplash.com/s/photos/"
    full_url = f"{base_url}{keyword}?license=free&orientation=portrait"
    return full_url

def main():
    st.title("Unsplash Image Search")
    
    # Input for the keyword
    keyword = st.text_input("Enter a keyword for your search:")

    if st.button("Search on Unsplash"):
        if keyword:
            # Generate the URL
            unsplash_url = generate_unsplash_url(keyword)
            st.write(f"Opening Unsplash for keyword: **{keyword}**")
            
            # Open the URL in a new browser window
            webbrowser.open(unsplash_url, new=2)
        else:
            st.warning("Please enter a keyword to search.")

if __name__ == "__main__":
    main()
