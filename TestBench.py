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

/* Black canvas vertical container */
.canvas-container {
    min-height: 85vh;
    padding: 10px;
}

/* Floating Action Button (Button B) */
.fab-button {
    position: fixed;
    bottom: 30px;
    right: 30px;
    width: 70px;
    height: 70px;
    border-radius: 50%;
    background-color: #4da6ff;
    color: black;
    font-size: 36px;
    font-weight: bold;
    border: none;
    cursor: pointer;
    box-shadow: 0px 4px 10px rgba(0,0,0,0.5);
    z-index: 1000;
}

.fab-button:hover {
    background-color: #66b3ff;
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

    with st.container():  # vertical layout
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            username = st.text_input("Username")
            password = st.text_input("Password", type="password")

            if st.button("Login"):
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

    # -------- Black Canvas (Vertical Container) --------
    st.markdown("<div class='canvas-container'>", unsafe_allow_html=True)
    with st.container():

        # ---- Top Bar (Horizontal inside canvas) ----
        top_left, top_mid, top_right = st.columns([1, 8, 1])

        with top_left:
            if st.button("☰"):
                st.session_state.screen = "menu"
                st.rerun()

        # ---- Canvas Content Area (Vertical space) ----
        with st.container():
            st.markdown("<br><br>", unsafe_allow_html=True)
            # Future widgets / charts / content go here

    st.markdown("</div>", unsafe_allow_html=True)

    # ---- Floating Action Button (outside layout flow) ----
    if st.button("+", key="fab"):
        st.session_state.screen = "plus"
        st.rerun()

    # Apply FAB style
    st.markdown("""
    <script>
        const buttons = window.parent.document.querySelectorAll('button');
        const fab = buttons[buttons.length - 1];
        fab.classList.add('fab-button');
    </script>
    """, unsafe_allow_html=True)

# -----------------------------
# Menu Screen
# -----------------------------
def menu_screen():
    with st.container():  # vertical screen container
        st.markdown("<h3>Menu Screen</h3>", unsafe_allow_html=True)

        if st.button("Back"):
            st.session_state.screen = "canvas"
            st.rerun()

# -----------------------------
# Plus Button Screen
# -----------------------------
def plus_screen():
    with st.container():  # vertical screen container
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