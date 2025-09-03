import streamlit as st

from src.router import Page


def render_main_page():
    """
    Renders the main page of the application.
    """
    # Load and apply custom CSS for this component
    try:
        with open("src/static/css/main_page.css", "r", encoding="utf-8") as f:
            css_content = f.read()
        st.markdown(f"<style>{css_content}</style>", unsafe_allow_html=True)
    except FileNotFoundError:
        # Continue without custom styling if the CSS file is not found
        pass

    # Clear previous content when navigating between pages
    st.empty()

    st.title("🎉 Hello Streamlit!")

    st.write(
        "This is a simple application to demonstrate a clean and scalable project structure."
    )

    app_router = st.session_state.app_router

    if st.button("Go to Another Page", type="primary"):
        # Update the page state in the router
        app_router.go_to(Page.ANOTHER)
        # Rerun the script to reflect the page change
        st.rerun()
