import streamlit as st


def login():

    st.title("🔐 TechnoKraft Login")

    role = st.selectbox(
        "Login As",
        ["Student", "Admin"]
    )

    username = st.text_input("Username")
    password = st.text_input(
        "Password",
        type="password"
    )

    if st.button(
        "Login",
        use_container_width=True
    ):

        # Admin login
        if role == "Admin":

            if username == "admin" and password == "admin123":

                st.session_state["logged_in"] = True
                st.session_state["role"] = "Admin"

                st.rerun()

            else:

                st.error("Invalid Admin username or password.")

        # Student login
        else:

            if username == "student" and password == "student123":

                st.session_state["logged_in"] = True
                st.session_state["role"] = "Student"

                st.rerun()

            else:

                st.error("Invalid Student username or password.")