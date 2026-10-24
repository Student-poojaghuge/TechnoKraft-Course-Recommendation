# 🎓 TechnoKraft Course Recommendation System

A Machine Learning-based web application that helps students explore course recommendations, view course fees, compare institute fees, and submit reviews. The system includes separate Student and Admin dashboards built using Streamlit.

## 🚀 Project Features

### 👨‍🎓 Student Dashboard
- **Course Recommendation:** Predicts Yes/No based on course and market-related inputs using a Random Forest classifier.
- **Course Fees:** View minimum, maximum, and average TechnoKraft course fees.
- **Fee Comparison:** Compare TechnoKraft fees with average fees from other institutes.
- **Student Reviews:** Submit course ratings and feedback.
- **Home Dashboard:** View course and institute statistics.

### 👨‍💼 Admin Dashboard
- View total institutes and available courses.
- Explore institute-wise course fee details.
- Compare competitor fees and suggested TechnoKraft fees.
- View student reviews and average ratings.
- Analyze institute and course statistics.

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Random Forest Classifier
- Streamlit
- Joblib
- CSV datasets
- Git and GitHub

## 📁 Project Structure

```text
TechnoKraft-Course-Recommendation/
├── app/
│   ├── app.py
│   ├── login.py
│   ├── student_dashboard.py
│   └── admin_dashboard.py
├── data/
│   ├── TechnoKraft_Course_Recommendation_ML_Dataset.csv
│   ├── Institute_ML_Dataset.csv
│   ├── Institute_ML_Dataset_Cleaned.csv
│   ├── TechnoKraft_Fee_Comparison.csv
│   └── Student_Reviews.csv
├── models/
│   ├── course_recommendation_model.pkl
│   └── feature_columns.pkl
├── notebooks/
│   └── course_recommendation.ipynb
├── requirements.txt
├── .gitignore
└── README.md
```

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/Student-poojaghuge/TechnoKraft-Course-Recommendation.git
```

### 2. Open the project folder

```bash
cd TechnoKraft-Course-Recommendation
```

### 3. Create a virtual environment (recommended)

```bash
python -m venv venv
```

Activate it on Windows:

```powershell
.\venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```bash
python -m pip install -r requirements.txt
```

If any required package is missing, install it using:

```bash
python -m pip install streamlit pandas scikit-learn joblib
```

### 5. Run the application

```bash
streamlit run app/app.py
```

Open the local URL displayed in the terminal, usually `http://localhost:8501`.

## 🧠 Machine Learning Workflow

1. Load the course recommendation dataset.
2. Preprocess categorical and numerical features.
3. Separate input features and the target variable.
4. Train a Random Forest classification model.
5. Evaluate model performance using accuracy, precision, recall, F1 score, and cross-validation.
6. Save the trained model and feature columns using Joblib.
7. Load the saved model in the Streamlit application to generate predictions.

**Target variable:** `Recommendation` — Yes or No.

**Note:** Model performance depends on the quality and representativeness of the training dataset. Results on the current dataset do not guarantee real-world accuracy.

## 💰 Fee Comparison

The institute fee dataset is maintained separately from the recommendation model. It supports institute-wise fee lookup and comparison of TechnoKraft fees with available competitor fee statistics.

The fee comparison is based on the available dataset and should not be interpreted as verified, real-time market pricing.

## 🔐 Login Information

The application currently uses demo credentials defined in the login code. Configure secure authentication before deploying publicly. Do not use demo credentials for real student or administrator accounts.

## 🔮 Future Scope

- Database integration for users and reviews.
- Secure authentication and role-based access control.
- Improved recommendations using larger, real-world datasets.
- Course enrollment and personalized student profiles.
- Updated institute fee information.
- Deployment to a cloud platform.

## 👩‍💻 Author

**Pooja Ghuge**

Electronics and Telecommunication Engineering

## 📌 Disclaimer

This project is developed for educational and demonstration purposes. Course recommendations and fee comparisons are based on the supplied datasets and should not be treated as guaranteed career guidance or verified current pricing.
