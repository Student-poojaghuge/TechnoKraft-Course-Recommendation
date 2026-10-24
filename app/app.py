import streamlit as st

from login import login
from student_dashboard import student_dashboard
from admin_dashboard import admin_dashboard


# -----------------------------
# Page Configuration
# -----------------------------

st.set_page_config(
    page_title="TechnoKraft Course Recommendation",
    page_icon="🎓",
    layout="wide"
)


# -----------------------------
# Session State
# -----------------------------

if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False

if "role" not in st.session_state:
    st.session_state["role"] = None


# -----------------------------
# Login
# -----------------------------

if not st.session_state["logged_in"]:

    login()


# -----------------------------
# Admin Dashboard
# -----------------------------

elif st.session_state["role"] == "Admin":

    admin_dashboard()

    st.divider()

    if st.button("🚪 Logout"):

        st.session_state["logged_in"] = False
        st.session_state["role"] = None

        st.rerun()


# -----------------------------
# Student Dashboard
# -----------------------------

elif st.session_state["role"] == "Student":

    student_dashboard()

    st.divider()

    if st.button("🚪 Logout"):

        st.session_state["logged_in"] = False
        st.session_state["role"] = None

        st.rerun()