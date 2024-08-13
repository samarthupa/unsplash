import streamlit as st
import streamlit.components.v1 as components

def main():
    st.title("Keyword-Based Image Search")
    st.write("Enter a keyword to search for images on Unsplash.")

    keyword = st.text_input("Keyword")

    if st.button("Search"):
        if keyword:
            # Create the URL with the entered keyword
            url = f"https://unsplash.com/s/photos/{keyword}?license=free&orientation=portrait"
            
            # HTML and JavaScript to open a new window
            html_code = f"""
            <script>
            window.open("{url}", "_blank", "width=800,height=600");
            </script>
            """
            components.html(html_code, height=0)
            
            st.success(f"Opening search results for '{keyword}' in a new window.")
        else:
            st.error("Please enter a keyword.")

if __name__ == "__main__":
    main()
