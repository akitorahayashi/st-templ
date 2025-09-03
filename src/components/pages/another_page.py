import streamlit as st
from src.router import Page


def render_another_page():
    """
    Renders the another page of the application.
    """
    st.title("Another Page")
    st.write("Welcome to the another page!")

    app_router = st.session_state.app_router

    if st.button("Go back to Main Page", type="primary"):
        app_router.go_to(Page.MAIN)
        st.rerun()
