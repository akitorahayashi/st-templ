import streamlit as st

# Set page configuration
st.set_page_config(
    page_title="Theme Demo",
    page_icon="🎨",
)

# --- Theme-aware CSS Styling ---
# This demonstrates how to use Streamlit's theme variables in custom CSS.
# By using var(--primary-color), var(--background-color), etc., the component
# will automatically adapt to the theme defined in `.streamlit/config.toml`.
themed_css = """
<style>
    .themed-box {
        border: 2px solid var(--primary-color);
        border-radius: 5px;
        padding: 15px;
        margin-bottom: 20px;
        background-color: var(--secondary-background-color);
    }
    .themed-box h2 {
        color: var(--primary-color);
        margin-bottom: 10px;
    }
    .themed-box p {
        color: var(--text-color);
    }
</style>
"""
st.markdown(themed_css, unsafe_allow_html=True)


# --- Application Content ---

st.title("Centralized Theme Demonstration")

st.write(
    "This application demonstrates how to use a centralized theme "
    "defined in `.streamlit/config.toml`."
)

# --- Standard Widgets ---
st.header("Standard Widgets")
st.write(
    "Standard Streamlit widgets like `st.title`, `st.header`, and `st.button` "
    "will automatically use the theme colors."
)
st.button("Primary Color Button")


# --- Custom Themed Component ---
st.header("Custom Themed Component")
st.markdown(
    """
    <div class="themed-box">
        <h2>This is a Custom Themed Box</h2>
        <p>
            Its border and title color come from <code>primaryColor</code>,
            its background from <code>secondaryBackgroundColor</code>,
            and its text from <code>textColor</code>.
        </p>
        <p>
            By using CSS variables (e.g., <code>var(--primary-color)</code>),
            the styling is kept separate from the Python code.
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)

st.success(
    "Refactoring complete! All styles are now managed via " "`.streamlit/config.toml`."
)
