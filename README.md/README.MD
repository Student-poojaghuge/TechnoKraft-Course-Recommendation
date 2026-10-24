# TechnoKraft Course Recommendation System

## Project Overview

The TechnoKraft Course Recommendation System is a Machine Learning project that recommends whether a course should be offered based on market demand, competition, course duration, placement demand, AI trend, and other course-related factors.

## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Matplotlib
* Seaborn
* Streamlit
* Joblib

## Machine Learning Model

* Random Forest Classifier

## Features

* Course Category
* Market Demand
* Competition
* TechnoKraft Offers
* Course Duration
* Placement Demand
* AI Trend

## Model Evaluation

The Random Forest model achieved 100% accuracy on the current dataset and 100% mean accuracy in 5-fold cross-validation.

The dataset contains 72 records, so additional real-world data is required to validate the model's generalization.

## Application

A Streamlit web application is included for entering course-related details and generating a course recommendation with probability.

## Project Structure

```text
TechnoKraft_Course_Recommendation/
├── data/
│   └── TechnoKraft_Course_Recommendation_ML_Dataset.csv
├── notebooks/
│   └── course_recommendation.ipynb
├── models/
│   ├── course_recommendation_model.pkl
│   └── feature_columns.pkl
├── app/
│   └── app.py
├── requirements.txt
└── README.md
```

## How to Run

```bash
pip install -r requirements.txt
streamlit run app/app.py
```
