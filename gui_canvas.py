import streamlit as st

def init_styles():
    """Inject global CSS styles"""
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

    .canvas-container {
        min-height: 85vh;
        padding: 10px;
    }

    .fab-button {
        position: fixed;
        bottom: 30px;
        right: 30px;
        width: 70px;
        height: 70px;
        border-radius: 50%;
        font-size: 36px;
        font-weight: bold;
        z-index: 1000;
    }

    .menu-bubble {
        width: 48px;
        height: 48px;
        border-radius: 50%;
        font-size: 20px;
    }
    </style>
    """, unsafe_allow_html=True)


def init_session_state():
    """Initialize required session state variables"""
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False

    if "screen" not in st.session_state:
        st.session_state.screen = "login"

    if "menu_open" not in st.session_state:
        st.session_state.menu_open = False


def login_screen():
    st.markdown("<h2 style='text-align:center;'>Login</h2>", unsafe_allow_html=True)

    with st.container():
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


def canvas_screen():
    st.markdown("<div class='canvas-container'>", unsafe_allow_html=True)

    with st.container():
        # Top bar
        left, mid, right = st.columns([1, 8, 1])

        with left:
            if st.button("☰"):
                st.session_state.menu_open = not st.session_state.menu_open
                st.rerun()

        # Navigation menu
        if st.session_state.menu_open:
            with st.container():
                st.markdown("### Navigation")
                for i in range(1, 11):
                    if st.button(f"Screen {i}", key=f"nav_{i}"):
                        st.session_state.screen = f"screen_{i}"
                        st.session_state.menu_open = False
                        st.rerun()

    st.markdown("</div>", unsafe_allow_html=True)

    # Floating + button
    if st.button("+", key="fab"):
        st.session_state.screen = "plus"
        st.rerun()

    # Apply styles to special buttons
    st.markdown("""
    <script>
        const buttons = window.parent.document.querySelectorAll('button');
        buttons.forEach(btn => {
            if (btn.innerText === "+") {
                btn.classList.add("fab-button");
            }
            if (btn.innerText === "☰") {
                btn.classList.add("menu-bubble");
            }
        });
    </script>
    """, unsafe_allow_html=True)


def generic_screen(name):
    with st.container():
        st.markdown(f"<h3>{name.replace('_', ' ').title()}</h3>", unsafe_allow_html=True)
        if st.button("Back to Canvas"):
            st.session_state.screen = "canvas"
            st.rerun()


def plus_screen():
    with st.container():
        st.markdown("<h3>Plus Action Screen</h3>", unsafe_allow_html=True)
        if st.button("Back to Canvas"):
            st.session_state.screen = "canvas"
            st.rerun()


def run_gui():
    """
    Main GUI router function.
    Call this from main.py
    """
    init_styles()
    init_session_state()

    if not st.session_state.logged_in:
        login_screen()
    else:
        if st.session_state.screen == "canvas":
            canvas_screen()
        elif st.session_state.screen == "plus":
            plus_screen()
        elif st.session_state.screen.startswith("screen_"):
            generic_screen(st.session_state.screen)