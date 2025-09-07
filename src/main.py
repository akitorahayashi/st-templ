import os

import streamlit as st
from dotenv import load_dotenv

from src.models.counter import Counter

load_dotenv()

st.set_page_config(
    page_title="My App",
    page_icon="✨",
    # "centered"/"wide"
    layout="centered",
    # "auto"/"expanded"/"collapsed"
    initial_sidebar_state="collapsed",
)


def main():
    """
    The main function that runs the Streamlit application.
    """
    initialize_session()

    # st.navigationでページのリストを定義
    pg = st.navigation(
        [
            st.Page("src/components/pages/main_page.py", title="Main", default=True),
            st.Page("src/components/pages/sub_page.py", title="Sub"),
            st.Page("src/components/pages/result_page.py", title="Result"),
        ]
    )

    # アプリケーションを実行
    pg.run()


def initialize_session():
    """Initializes the session state."""
    if "counter" not in st.session_state:
        is_debug = os.getenv("DEBUG", "false").lower() in ("true", "1", "yes", "on")
        if is_debug:
            from dev.mocks.counter import MockCounter

            st.session_state.counter = MockCounter()
        else:
            st.session_state.counter = Counter()


if __name__ == "__main__":
    main()
