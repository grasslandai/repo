import streamlit as st
import pickle
import numpy as np

def load_model():
    with open("saved_model.pkl", "rb") as file:
        data = pickle.load(file)
    return data

data = load_model()
regressor_loaded = data["model"]

def show_predict_page():
    st.title("Heart Disease Prediction")
    st.write("""### Prior information to predict heart disease""")

    age_slider = st.slider("Age", min_value=29, max_value=77, value=50 )

    gender_radio = st.radio("Gender", ("Male", "Female"))
    if gender_radio == "Male":
        gender_radio = 1
    else:
        gender_radio = 0

    chest_pain_type = st.radio("Chest Pain Type", (0,1,2,3))

    restingbp_slider = st.slider("Resting BP/mmHg on admission to the hospital", min_value=94, max_value=200, value=100 )

    serum_cholestrol_slider = st.slider("serum_cholestrol in mg/dl", min_value=126, max_value=564, value=200)

    fasting_blood_sugar_radio = st.radio("Fasting blood sugar >= 120 mg/dl", ("Yes", "No"))
    if fasting_blood_sugar_radio == "Yes":
        fasting_blood_sugar_radio = 1
    else:
        fasting_blood_sugar_radio = 0

    resting_ecg_radio = st.radio("Resting ECG results", (0,1,2))

    maximum_heart_rate_slider = st.slider("Maximum heart rate achieve", min_value=71, max_value=202, value=149)

    angina_radio  = st.radio("Exercise induced angina", ("Yes", "No"))
    if angina_radio == "Yes":
        angina_radio = 1
    else:
        angina_radio = 0

    depression_no = st.number_input("ST depression induced by exercise relative to rest from 0.0 to 6.2")
    #st.write("ST depression level", depression_no)

    slope = st.radio("the slope of the peak exercise ST segment", (0,1,2))

    ca = st.radio("number of major vessels (0-3) colored by flourosopy", (0,1,2,3))

    thal = st.radio("thal", ("Normal", "fixed defect", "reversible defect"))
    if thal == "Normal":
        thal = 1
    elif thal == "fixed defect":
        thal = 2
    elif thal == "reversible defect":
        thal = 3

    on_click = st.button("Try Predict")

    if on_click:

        X = np.array([[
            age_slider,
            gender_radio,
            chest_pain_type,
            restingbp_slider,
            serum_cholestrol_slider,
            fasting_blood_sugar_radio,
            resting_ecg_radio,
            maximum_heart_rate_slider,
            angina_radio,
            depression_no,
            slope,
            ca,
            thal
        ]])
        X = X.astype(float)

        # For debug purpose
        #input_data = (71, 0, 0, 112, 149, 0, 1, 125, 0, 1.6, 1, 0, 2) # with disease
        #input_data = (52, 1, 0, 125, 212, 0, 1, 168, 0, 1.0, 2, 2, 3) # without disease
        #X_new = np.asarray(input_data)
        #X_new = X_new.reshape(1, -1)
        #X_new = X_new.astype(float)
        #have_disease = regressor_loaded.predict(X_new)
        
        have_disease = regressor_loaded.predict(X)

        if have_disease == 1:
            st.subheader("This case was very likely to have heart disease")
        else:
            st.subheader("This case was likely safe")


