import streamlit as st


def render_sidebar():
    """
    Renders the sidebar for navigation.
    """
    with st.sidebar:
        st.title("ナビゲーション")
        st.page_link("components/pages/main_page.py", label="メインページ")
        st.page_link("components/pages/sub_page.py", label="サブページ")
