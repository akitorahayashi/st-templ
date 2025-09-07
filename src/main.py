import streamlit as st

from src.components.navigations.sidebar import render_sidebar
from src.models.counter import Counter

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
            st.Page("components/pages/main_page.py", title="Main", default=True),
            st.Page("components/pages/sub_page.py", title="Sub"),
            st.Page("components/pages/result_page.py", title="Result"),
        ],
        position="hidden",
    )

    # アプリケーションを実行
    pg.run()

    # Render sidebar
    render_sidebar()


def initialize_session():
    """Initializes the session state."""
    if "counter" not in st.session_state:
        is_debug = st.secrets.get("DEBUG", False)
        if is_debug:
            from dev.mocks.counter import MockCounter

            st.session_state.counter = MockCounter()
        else:
            st.session_state.counter = Counter()


if __name__ == "__main__":
    main()
