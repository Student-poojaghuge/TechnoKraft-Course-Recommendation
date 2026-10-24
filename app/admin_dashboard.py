import streamlit as st
import pandas as pd
import os


def admin_dashboard():

    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    institute_path = os.path.join(
        BASE_DIR,
        "data",
        "Institute_ML_Dataset_Cleaned.csv"
    )

    fee_path = os.path.join(
        BASE_DIR,
        "data",
        "TechnoKraft_Fee_Comparison.csv"
    )

    institute_df = pd.read_csv(institute_path)
    fee_comparison = pd.read_csv(fee_path)

    # =========================
    # Sidebar
    # =========================

    st.sidebar.title("👨‍💼 TechnoKraft Admin")

    st.sidebar.markdown("---")

    menu = st.sidebar.radio(
        "Navigation",
        [
            "📊 Dashboard",
            "🏫 Institute Fees",
            "💰 Fee Comparison",
            "⭐ Student Reviews",
            "📈 Analytics"
        ]
    )

    st.sidebar.markdown("---")

    st.sidebar.write("👤 Admin")

    # =========================
    # Dashboard
    # =========================

    if menu == "📊 Dashboard":

        st.title("📊 Admin Dashboard")

        st.subheader("Dashboard Overview")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric(
                "🏫 Total Institutes",
                institute_df["Institute"].nunique()
            )

        with col2:
            st.metric(
                "📚 Total Courses",
                institute_df["Course"].nunique()
            )

        with col3:
            st.metric(
                "💰 Fee Comparison Courses",
                fee_comparison["Course"].nunique()
            )

        st.divider()

        st.subheader("📋 System Information")

        col1, col2 = st.columns(2)

        with col1:
            st.info(
                "🎓 Course Recommendation System\n\n"
                "Students can receive course recommendations "
                "based on market and course-related factors."
            )

        with col2:
            st.info(
                "💰 Fee Comparison System\n\n"
                "Compare TechnoKraft fees with available "
                "institute fee data."
            )

    # =========================
    # Institute Fees
    # =========================

    elif menu == "🏫 Institute Fees":

        st.title("🏫 Institute & Fee Details")

        course_list = sorted(
            institute_df["Course"].dropna().unique()
        )

        col1, col2 = st.columns([4, 1])

        with col1:

            selected_course = st.selectbox(
                "Select Course",
                ["Select a course"] + course_list,
                key="admin_institute_course"
            )

        with col2:

            st.write("")
            st.write("")

            institute_search = st.button(
                "🔍 Search",
                use_container_width=True,
                key="institute_search"
            )

        if institute_search:

            if selected_course == "Select a course":

                st.warning("Please select a course.")

            else:

                institute_result = institute_df[
                    institute_df["Course"] == selected_course
                ]

                display_result = institute_result[
                    [
                        "Institute",
                        "Course",
                        "Min_Fee_INR",
                        "Max_Fee_INR",
                        "Avg_Fee_INR"
                    ]
                ].copy()

                display_result.columns = [
                    "Institute",
                    "Course",
                    "Minimum Fee (₹)",
                    "Maximum Fee (₹)",
                    "Average Fee (₹)"
                ]

                st.dataframe(
                    display_result,
                    use_container_width=True,
                    hide_index=True
                )

    # =========================
    # Fee Comparison
    # =========================

    elif menu == "💰 Fee Comparison":

        st.title("💰 Competitor Fee Comparison")

        course_list = sorted(
            fee_comparison["Course"].dropna().unique()
        )

        col1, col2 = st.columns([4, 1])

        with col1:

            selected_course = st.selectbox(
                "Select Course",
                ["Select a course"] + course_list,
                key="admin_comparison_course"
            )

        with col2:

            st.write("")
            st.write("")

            comparison_search = st.button(
                "🔍 Search",
                use_container_width=True,
                key="admin_comparison_search"
            )

        if comparison_search:

            if selected_course == "Select a course":

                st.warning("Please select a course.")

            else:

                fee_result = fee_comparison[
                    fee_comparison["Course"] == selected_course
                ]

                if not fee_result.empty:

                    row = fee_result.iloc[0]

                    col1, col2, col3 = st.columns(3)

                    with col1:
                        st.metric(
                            "Competitor Average",
                            f"₹{row['Competitor_Avg_Fee']:,.0f}"
                        )

                    with col2:
                        st.metric(
                            "TechnoKraft Current",
                            f"₹{row['TechnoKraft_Avg_Fee']:,.0f}"
                        )

                    with col3:
                        st.metric(
                            "Suggested Fee",
                            f"₹{row['Suggested_TechnoKraft_Fee']:,.0f}"
                        )

                    comparison_display = pd.DataFrame({
                        "Fee Type": [
                            "Competitor Minimum Fee",
                            "Competitor Maximum Fee",
                            "Competitor Average Fee",
                            "TechnoKraft Current Average Fee",
                            "Suggested TechnoKraft Fee"
                        ],
                        "Amount (₹)": [
                            row["Competitor_Min_Fee"],
                            row["Competitor_Max_Fee"],
                            row["Competitor_Avg_Fee"],
                            row["TechnoKraft_Avg_Fee"],
                            row["Suggested_TechnoKraft_Fee"]
                        ]
                    })

                    st.dataframe(
                        comparison_display,
                        use_container_width=True,
                        hide_index=True
                    )

                    st.subheader("📈 Fee Difference")

                    difference = row["Fee_Difference"]

                    if difference > 0:

                        st.info(
                            f"TechnoKraft current average fee is "
                            f"₹{difference:,.0f} below the competitor average."
                        )

                    elif difference < 0:

                        st.info(
                            f"TechnoKraft current average fee is "
                            f"₹{abs(difference):,.0f} above the competitor average."
                        )

                    else:

                        st.info(
                            "TechnoKraft current average fee is equal "
                            "to the competitor average."
                        )

                else:

                    st.warning(
                        "Fee comparison information is not available."
                    )

    # =========================
    # Student Reviews
    # =========================

    elif menu == "⭐ Student Reviews":

        st.title("⭐ Student Reviews")

        reviews_path = os.path.join(
            BASE_DIR,
            "data",
            "Student_Reviews.csv"
        )

        if os.path.exists(reviews_path):

            reviews_df = pd.read_csv(reviews_path)

            if not reviews_df.empty:

                st.subheader("📋 Submitted Reviews")

                st.dataframe(
                    reviews_df,
                    use_container_width=True,
                    hide_index=True
                )

                st.divider()

                average_rating = reviews_df["Rating"].mean()

                col1, col2 = st.columns(2)

                with col1:
                    st.metric(
                        "⭐ Average Rating",
                        f"{average_rating:.1f}/5"
                    )

                with col2:
                    st.metric(
                        "📝 Total Reviews",
                        len(reviews_df)
                    )

            else:

                st.info(
                    "No student reviews submitted yet."
                )

        else:

            st.info(
                "No student reviews submitted yet."
            )

    # =========================
    # Analytics
    # =========================

    elif menu == "📈 Analytics":

        st.title("📈 Analytics")

        st.subheader("Institute Dataset Overview")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric(
                "Total Records",
                len(institute_df)
            )

        with col2:
            st.metric(
                "Unique Institutes",
                institute_df["Institute"].nunique()
            )

        with col3:
            st.metric(
                "Unique Courses",
                institute_df["Course"].nunique()
            )

        st.divider()

        st.subheader("📚 Courses by Institute")

        institute_counts = (
            institute_df["Institute"]
            .value_counts()
            .reset_index()
        )

        institute_counts.columns = [
            "Institute",
            "Number of Courses"
        ]

        st.dataframe(
            institute_counts,
            use_container_width=True,
            hide_index=True
        )