import streamlit as st

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Black Canvas App",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# -----------------------------
# Global Styles (CSS)
# -----------------------------
st.markdown("""
<style>
body {
    background-color: black;
    color: white;
}

.stApp {
    background-color: black;
}

input {
    background-color: transparent !important;
    color: white !important;
    border: 1px solid white !important;
}

button {
    background-color: #4da6ff !important;
    color: black !important;
    border-radius: 8px !important;
}

.plus-button {
    font-size: 40px;
    width: 120px;
    height: 120px;
    border-radius: 50%;
}
</style>
""", unsafe_allow_html=True)

# -----------------------------
# Session State
# -----------------------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "screen" not in st.session_state:
    st.session_state.screen = "login"

# -----------------------------
# Login Screen
# -----------------------------
def login_screen():
    st.markdown("<h2 style='text-align:center;'>Login</h2>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1,2,1])

    with col2:
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")

        if st.button("Login"):
            # Basic authentication (demo)
            if username == "admin" and password == "admin":
                st.session_state.logged_in = True
                st.session_state.screen = "canvas"
                st.rerun()
            else:
                st.error("Invalid credentials")

# -----------------------------
# Main Canvas Screen
# -----------------------------
def canvas_screen():
    # Top-left menu bubble
    with st.container():
        col1, col2, col3 = st.columns([1, 8, 1])
        with col1:
            if st.button("☰"):
                st.session_state.screen = "menu"
                st.rerun()

    st.markdown("<br><br><br>", unsafe_allow_html=True)

    # Center + button
    col1, col2, col3 = st.columns([4,2,4])
    with col2:
        if st.button("+", key="plus", help="Add", use_container_width=True):
            st.session_state.screen = "plus"
            st.rerun()

# -----------------------------
# Menu Screen
# -----------------------------
def menu_screen():
    st.markdown("<h3>Menu Screen</h3>", unsafe_allow_html=True)

    if st.button("Back"):
        st.session_state.screen = "canvas"
        st.rerun()

# -----------------------------
# Plus Button Screen
# -----------------------------
def plus_screen():
    st.markdown("<h3>Plus Action Screen</h3>", unsafe_allow_html=True)

    if st.button("Back"):
        st.session_state.screen = "canvas"
        st.rerun()

# -----------------------------
# Screen Router
# -----------------------------
if not st.session_state.logged_in:
    login_screen()
else:
    if st.session_state.screen == "canvas":
        canvas_screen()
    elif st.session_state.screen == "menu":
        menu_screen()
    elif st.session_state.screen == "plus":
        plus_screen()