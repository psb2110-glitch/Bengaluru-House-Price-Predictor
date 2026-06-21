# Bengaluru House Price Predictor

A Machine Learning-based web application that predicts residential property prices in Bengaluru using location, square footage, number of bedrooms (BHK), and number of bathrooms.

The application is built using Python, Flask, Scikit-Learn, Pandas, HTML, CSS, Bootstrap, JavaScript, and AJAX. It provides real-time predictions along with advanced property analysis features such as price range estimation, location insights, property comparison, and EMI calculation.

---

## Overview

The project aims to assist home buyers, sellers, and investors by providing accurate property price predictions and market insights based on historical housing data from Bengaluru.

The system uses a trained Ridge Regression model and offers an interactive web interface for seamless user experience.

---

## Features

### House Price Prediction

Predict house prices based on:

- Location
- Total Square Feet
- Number of Bedrooms (BHK)
- Number of Bathrooms

### Price Range Estimation

Provides an estimated lower and upper price range around the predicted property value.

### Location Insights

Displays average property prices for the selected location to help users understand local market trends.

### Budget-Based Property Recommendations

Suggests locations that match the user's budget based on historical pricing patterns.

### House Comparison Tool

Allows users to compare two properties and analyze differences in predicted prices.

### EMI Calculator

Calculates estimated monthly EMI based on:

- Loan Amount
- Interest Rate
- Loan Tenure

### Responsive User Interface

- Mobile-friendly design
- Bootstrap-based layout
- Dynamic updates using AJAX
- Real-time prediction results without page refresh

---
## Live Demo

https://bengaluru-house-price-predictor-stdi.onrender.com

## Machine Learning Workflow

1. Data Collection
2. Data Cleaning and Preprocessing
3. Feature Engineering
4. Model Training using Ridge Regression
5. Model Serialization using Pickle
6. Flask Web Application Development
7. Deployment

---

## Technology Stack

### Programming Language

- Python

### Backend

- Flask

### Machine Learning

- Scikit-Learn
- Ridge Regression
- Pandas
- NumPy

### Frontend

- HTML5
- CSS3
- Bootstrap 5
- JavaScript
- AJAX

### Deployment

- GitHub
- Render

---

## Project Structure

```text
Bengaluru-House-Price-Predictor
│
├── main.py
├── Corrected_data.csv
├── RidgeModel.pkl
├── requirements.txt
├── Procfile
│
└── templates
    └── index.html
```

## Input Parameters

The model uses the following features:

- Location
- Total Square Feet
- Number of Bedrooms (BHK)
- Number of Bathrooms

---

## Future Enhancements

- Interactive Price Trend Graphs
- Property Investment Score
- Google Maps Integration
- Nearby Amenities Analysis
- Rental Price Prediction
- Advanced Recommendation Engine
- User Authentication and Saved Searches

---

## Author

Priyanshu Sekhar Bhuyan

Machine Learning Enthusiast | Python Developer | Data Science Learner

---

## Key Highlights

- Machine Learning-based House Price Prediction
- Price Range Estimation
- Location-Based Market Insights
- Budget-Based Recommendations
- House Comparison Tool
- EMI Calculator
- Responsive Web Application
- Real-Time Prediction System
