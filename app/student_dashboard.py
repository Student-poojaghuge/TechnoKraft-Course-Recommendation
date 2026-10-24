import streamlit as st
import pandas as pd
import os
import joblib


def student_dashboard():

    BASE_DIR = os.path.dirname(
        os.path.dirname(os.path.abspath(__file__))
    )

    # =========================
    # Model Files
    # =========================

    model_path = os.path.join(
        BASE_DIR,
        "models",
        "course_recommendation_model.pkl"
    )

    feature_path = os.path.join(
        BASE_DIR,
        "models",
        "feature_columns.pkl"
    )

    model = joblib.load(model_path)
    feature_columns = joblib.load(feature_path)

    # =========================
    # Dataset Files
    # =========================

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

    st.sidebar.title("🎓 TechnoKraft")

    st.sidebar.markdown("---")

    menu = st.sidebar.radio(
        "Navigation",
        [
            "🏠 Home",
            "📚 Course Recommendation",
            "💰 Course Fees",
            "📊 Fee Comparison",
            "⭐ Student Reviews"
        ]
    )

    st.sidebar.markdown("---")

    st.sidebar.write("👤 Student")

    # =========================================================
    # HOME
    # =========================================================

    if menu == "🏠 Home":

        st.title("🎓 Welcome to TechnoKraft")

        st.subheader("Course Recommendation System")

        st.write(
            "Find suitable courses, check course fees, "
            "compare fees and explore learning opportunities."
        )

        st.divider()

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric(
                "📚 Available Courses",
                institute_df["Course"].nunique()
            )

        with col2:
            st.metric(
                "🏫 Institutes",
                institute_df["Institute"].nunique()
            )

        with col3:
            st.metric(
                "💰 Fee Comparison",
                fee_comparison["Course"].nunique()
            )

        st.divider()

        st.info(
            "Use the navigation menu on the left to explore "
            "course recommendations, fees and comparisons."
        )

    # =========================================================
    # COURSE RECOMMENDATION
    # =========================================================

    elif menu == "📚 Course Recommendation":

        st.title("📚 Course Recommendation")

        col1, col2 = st.columns(2)

        # -------------------------
        # Left Column
        # -------------------------

        with col1:

            course_category = st.selectbox(
                "Course",
                sorted(
                    institute_df["Course"]
                    .dropna()
                    .unique()
                )
            )

            market_demand = st.selectbox(
                "Market Demand",
                ["High", "Medium", "Low"]
            )

            competition = st.selectbox(
                "Competition",
                ["High", "Medium", "Low"]
            )

            technokraft_offers = st.selectbox(
                "TechnoKraft Offers",
                ["Yes", "No"]
            )

        # -------------------------
        # Right Column
        # -------------------------

        with col2:

            duration = st.number_input(
                "Duration (Months)",
                min_value=1,
                max_value=24,
                value=3
            )

            placement_demand = st.selectbox(
                "Placement Demand",
                ["High", "Medium", "Low"]
            )

            ai_trend = st.selectbox(
                "AI Trend",
                ["Yes", "No"]
            )

        st.divider()

        # -------------------------
        # Recommendation Button
        # -------------------------

        if st.button(
            "🔮 Get Course Recommendation",
            use_container_width=True
        ):

            # Create input using the SAME
            # column names used during model training

            input_data = pd.DataFrame({
                "Category": [course_category],
                "Market_Demand": [market_demand],
                "Competition": [competition],
                "TechnoKraft_Offers": [technokraft_offers],
                "Duration": [duration],
                "Placement_Demand": [placement_demand],
                "AI_Trend": [ai_trend]
            })

            # Encode categorical features

            input_encoded = pd.get_dummies(
                input_data,
                columns=[
                    "Category",
                    "Market_Demand",
                    "Competition",
                    "TechnoKraft_Offers",
                    "Duration",
                    "Placement_Demand",
                    "AI_Trend"
                ],
                dtype=int
            )

            # Match training features exactly

            input_encoded = input_encoded.reindex(
                columns=feature_columns,
                fill_value=0
            )

            # Prediction

            prediction = model.predict(
                input_encoded
            )[0]

            probability = model.predict_proba(
                input_encoded
            )[0]

            # Get predicted class from model

            predicted_class = model.classes_[
                probability.argmax()
            ]

            st.divider()

            # -------------------------
            # Recommendation Result
            # -------------------------

            if predicted_class == "Yes":

                st.success(
                    "✅ Recommendation: YES"
                )

            else:

                st.error(
                    "❌ Recommendation: NO"
                )

            # -------------------------
            # Probability
            # -------------------------

            st.write(
                f"Recommendation Probability: "
                f"{max(probability) * 100:.2f}%"
            )

            # -------------------------
            # Debug Information
            # -------------------------

            with st.expander("🔍 Prediction Details"):

                st.write(
                    "Model Prediction:",
                    prediction
                )

                st.write(
                    "Model Classes:",
                    list(model.classes_)
                )

                st.write(
                    "Input Data:"
                )

                st.dataframe(
                    input_data,
                    use_container_width=True,
                    hide_index=True
                )

    # =========================================================
    # COURSE FEES
    # =========================================================

    elif menu == "💰 Course Fees":

        st.title("💰 TechnoKraft Course Fees")

        course_list = sorted(
            institute_df["Course"]
            .dropna()
            .unique()
        )

        col1, col2 = st.columns([4, 1])

        with col1:

            selected_course = st.selectbox(
                "Select Course",
                ["Select a course"] + course_list,
                key="student_fee_course"
            )

        with col2:

            st.write("")
            st.write("")

            fee_search = st.button(
                "🔍 Search",
                use_container_width=True,
                key="student_fee_search"
            )

        if fee_search:

            if selected_course == "Select a course":

                st.warning(
                    "Please select a course."
                )

            else:

                course_fee = institute_df[
                    (
                        institute_df["Institute"]
                        == "TechnoKraft Training & Solution Pvt. Ltd."
                    )
                    &
                    (
                        institute_df["Course"]
                        == selected_course
                    )
                ]

                if not course_fee.empty:

                    fee = course_fee.iloc[0]

                    col1, col2, col3 = st.columns(3)

                    with col1:

                        st.metric(
                            "Average Fee",
                            f"₹{fee['Avg_Fee_INR']:,.0f}"
                        )

                    with col2:

                        st.metric(
                            "Minimum Fee",
                            f"₹{fee['Min_Fee_INR']:,.0f}"
                        )

                    with col3:

                        st.metric(
                            "Maximum Fee",
                            f"₹{fee['Max_Fee_INR']:,.0f}"
                        )

                    st.info(
                        "📝 Note: The displayed fee is the current "
                        "TechnoKraft course fee. Fees may vary depending "
                        "on course duration, batch, offers, and other "
                        "applicable factors."
                    )

                else:

                    st.warning(
                        "Fee information is not available "
                        "for this course."
                    )

    # =========================================================
    # FEE COMPARISON
    # =========================================================

    elif menu == "📊 Fee Comparison":

        st.title("📊 Course Fee Comparison")

        course_list = sorted(
            fee_comparison["Course"]
            .dropna()
            .unique()
        )

        col1, col2 = st.columns([4, 1])

        with col1:

            selected_course = st.selectbox(
                "Select Course",
                ["Select a course"] + course_list,
                key="comparison_course"
            )

        with col2:

            st.write("")
            st.write("")

            comparison_search = st.button(
                "🔍 Search",
                use_container_width=True,
                key="comparison_search"
            )

        if comparison_search:

            if selected_course == "Select a course":

                st.warning(
                    "Please select a course."
                )

            else:

                tech_fee = institute_df[
                    (
                        institute_df["Institute"]
                        == "TechnoKraft Training & Solution Pvt. Ltd."
                    )
                    &
                    (
                        institute_df["Course"]
                        == selected_course
                    )
                ]

                comparison = fee_comparison[
                    fee_comparison["Course"]
                    == selected_course
                ]

                if (
                    not tech_fee.empty
                    and not comparison.empty
                ):

                    tech = tech_fee.iloc[0]
                    comp = comparison.iloc[0]

                    col1, col2 = st.columns(2)

                    with col1:

                        st.subheader(
                            "🏫 TechnoKraft"
                        )

                        st.metric(
                            "Average Fee",
                            f"₹{tech['Avg_Fee_INR']:,.0f}"
                        )

                        st.write(
                            f"Minimum: "
                            f"₹{tech['Min_Fee_INR']:,.0f}"
                        )

                        st.write(
                            f"Maximum: "
                            f"₹{tech['Max_Fee_INR']:,.0f}"
                        )

                    with col2:

                        st.subheader(
                            "🏢 Other Institutes"
                        )

                        st.metric(
                            "Average Fee",
                            f"₹{comp['Competitor_Avg_Fee']:,.0f}"
                        )

                        st.write(
                            f"Minimum: "
                            f"₹{comp['Competitor_Min_Fee']:,.0f}"
                        )

                        st.write(
                            f"Maximum: "
                            f"₹{comp['Competitor_Max_Fee']:,.0f}"
                        )

                    st.info(
                        "Fees shown are based on the available "
                        "institute dataset and may vary by "
                        "institute, batch and course."
                    )

                else:

                    st.warning(
                        "Fee comparison is not available "
                        "for this course."
                    )

    # =========================================================
    # STUDENT REVIEWS
    # =========================================================

    elif menu == "⭐ Student Reviews":

        st.title("⭐ Student Reviews")

        reviews_path = os.path.join(
            BASE_DIR,
            "data",
            "Student_Reviews.csv"
        )

        st.subheader(
            "📝 Share Your Experience"
        )

        student_name = st.text_input(
            "Student Name"
        )

        review_course = st.selectbox(
            "Course",
            ["Select a course"] +
            sorted(
                institute_df["Course"]
                .dropna()
                .unique()
            ),
            key="review_course"
        )

        rating = st.select_slider(
            "Rating",
            options=[1, 2, 3, 4, 5],
            value=5
        )

        review_text = st.text_area(
            "Your Review"
        )

        if st.button(
            "📤 Submit Review",
            use_container_width=True
        ):

            if (
                student_name.strip() == ""
                or review_course == "Select a course"
                or review_text.strip() == ""
            ):

                st.warning(
                    "Please fill all the fields."
                )

            else:

                new_review = pd.DataFrame({
                    "Student_Name": [student_name],
                    "Course": [review_course],
                    "Rating": [rating],
                    "Review": [review_text]
                })

                if os.path.exists(
                    reviews_path
                ):

                    existing_reviews = pd.read_csv(
                        reviews_path
                    )

                    updated_reviews = pd.concat(
                        [
                            existing_reviews,
                            new_review
                        ],
                        ignore_index=True
                    )

                else:

                    updated_reviews = new_review

                updated_reviews.to_csv(
                    reviews_path,
                    index=False
                )

                st.success(
                    "✅ Thank you! Your review has been submitted."
                )