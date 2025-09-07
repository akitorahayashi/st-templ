import streamlit as st

st.title("Result Page")

# Display the counter value from session state
# Initialize if navigating here directly without visiting main_page first
if "counter" not in st.session_state:
    st.warning("Counter not initialized. Please visit the Main Page first.")
else:
    counter = st.session_state.counter
    st.write(f"Counter value from session state: {counter.get_count()}")

if st.button("Back to Main"):
    st.switch_page("components/pages/main_page.py")
