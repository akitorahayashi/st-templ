import streamlit as st

from src.components.navigations import render_sidebar
from src.components.pages import (
    render_another_page,
    render_main_page,
    render_sub_page,
)
from src.router import AppRouter, Page


def main():
    """
    The main function that runs the Streamlit application.
    """

    if "app_router" not in st.session_state:
        st.session_state.app_router = AppRouter()

    app_router = st.session_state.app_router

    # Render sidebar for navigation
    render_sidebar()

    # Page routing
    if app_router.current_page == Page.MAIN:
        render_main_page()
    elif app_router.current_page == Page.ANOTHER:
        render_another_page()
    elif app_router.current_page == Page.SUB:
        render_sub_page()


if __name__ == "__main__":
    main()
