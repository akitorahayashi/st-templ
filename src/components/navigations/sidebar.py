import streamlit as st
from src.router import Page, AppRouter


def render_sidebar():
    """
    Renders the sidebar for navigation.
    """
    st.sidebar.title("Navigation")
    app_router: AppRouter = st.session_state.app_router

    pages = {
        "Main": Page.MAIN,
        "Sub": Page.SUB,
    }

    current_page_label = next(
        (label for label, page in pages.items() if page == app_router.current_page),
        "Main",
    )

    selection = st.sidebar.radio(
        "",
        options=list(pages.keys()),
        key="sidebar_navigation",
        index=list(pages.keys()).index(current_page_label),
    )

    if pages[selection] != app_router.current_page:
        app_router.go_to(pages[selection])
        st.rerun()
