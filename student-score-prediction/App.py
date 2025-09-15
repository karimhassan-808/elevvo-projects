import streamlit as st 
import numpy as np
import joblib

model = joblib.load('elevvo-projects/student-score-prediction/notebooks/best_model.pkl')

st.title("Student Exam Score Predictor")

Hours_Studied = st.slider("Study Hours", 0.0, 45.0, 2.0)
Attendance = st.slider("Attendance Percentage", 0.0, 100.0, 80.0)
Access_to_Resources = st.selectbox("Access to Resources", ['Low', 'Medium', 'High'])
Previous_Scores = st.slider("Previous Scores Average", 0.0, 100.0, 80.0)
Teacher_Quality = st.selectbox("Teacher Quality", ['Low', 'Medium', 'High'])
Tutoring_Sessions = st.slider("Number of Sessions", 0.0,  8.0, 4.0)

if Teacher_Quality == 'Low':
    Teacher_Quality = 1
elif Teacher_Quality == 'Medium':
    Teacher_Quality = 2
else:
    Teacher_Quality = 0

if Access_to_Resources == 'Low':
    Access_to_Resources = 1
elif Access_to_Resources == 'Medium':
    Access_to_Resources = 2
else:
    Access_to_Resources = 0

if st.button("Predict Exam Score"):
    input_data = np.array([[Hours_Studied, Attendance, Access_to_Resources, Previous_Scores, Teacher_Quality, Tutoring_Sessions]])
    prediction = round(model.predict(input_data)[0])
    
    prediction = max(0, min(100, prediction))

    st.success(f"Predicted Exam Score is: {prediction}")

