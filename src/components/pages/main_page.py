import streamlit as st

# Load and apply custom CSS for this component
try:
    with open("src/static/css/main_page.css", "r", encoding="utf-8") as f:
        css_content = f.read()
    st.markdown(f"<style>{css_content}</style>", unsafe_allow_html=True)
except FileNotFoundError:
    # Continue without custom styling if the CSS file is not found
    pass

st.title("🎉 Hello Streamlit!")

st.write(
    "This is a simple application to demonstrate a clean and scalable project structure."
)

counter = st.session_state.counter

st.write(f"Current counter value: {counter.get_count()}")

# Button to increment the counter
if st.button("Increment Counter"):
    counter.increment()
    st.rerun()

if st.button("Go to Result Page", type="primary"):
    st.switch_page("components/pages/result_page.py")
