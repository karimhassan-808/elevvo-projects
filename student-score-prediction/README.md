# 🎓 Student Performance Analysis and Prediction

This project analyzes various factors that influence student exam performance and builds predictive models to estimate exam scores.  
It uses **data visualization**, **exploratory data analysis (EDA)**, and **machine learning models** such as Linear Regression, Decision Tree, and Random Forest.

---

## 📁 Dataset

**File:** `StudentPerformanceFactors.csv`  
The dataset contains several factors influencing student performance, including:
- Study habits (e.g., Hours_Studied, Attendance)
- Socioeconomic conditions (e.g., Family_Income, Parental_Education_Level)
- School-related variables (e.g., Teacher_Quality, Access_to_Resources)

---

## ⚙️ Installation & Requirements

Install the required dependencies:

```bash
pip install numpy pandas matplotlib seaborn scikit-learn
```

---

## 🧠 Project Workflow

1. Data loading and cleaning
2. EDA
3. Machine Learning Models
4. Model Selection: After evaluating multiple models, Linear Regression achieved the lowest RMSE,
making it the best choice for deployment in this project.

---

## 🚀 Future Improvements

Include more student behavioral and psychological factors.

Implement advanced ensemble models (XGBoost, LightGBM).

Build a simple web app for real-time performance prediction.

