import os

import streamlit as st
from dotenv import load_dotenv

from src.components.navigations import render_sidebar
from src.components.pages import (
    render_main_page,
    render_result_page,
    render_sub_page,
)
from src.models.counter import Counter
from src.router import AppRouter, Page

load_dotenv()


def main():
    """
    The main function that runs the Streamlit application.
    """
    initialize_session()

    app_router = st.session_state.app_router

    # Render sidebar for navigation
    render_sidebar()

    # Page routing
    if app_router.current_page == Page.MAIN:
        render_main_page()
    elif app_router.current_page == Page.RESULT:
        render_result_page()
    elif app_router.current_page == Page.SUB:
        render_sub_page()


def initialize_session():
    """Initializes the session state."""
    if "app_router" not in st.session_state:
        st.session_state.app_router = AppRouter()

    if "counter" not in st.session_state:
        is_debug = os.getenv("DEBUG", "false").lower() in ("true", "1", "yes", "on")
        if is_debug:
            from dev.mocks.counter import MockCounter

            st.session_state.counter = MockCounter()
        else:
            st.session_state.counter = Counter()


if __name__ == "__main__":
    main()
