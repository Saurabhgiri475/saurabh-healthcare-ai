import streamlit as st


def medical_recommendation(glucose,bmi,age):

    st.subheader("Medical Recommendations")

    if glucose > 140:
        st.warning("High glucose detected. Reduce sugar intake.")

    if bmi > 30:
        st.warning("BMI indicates obesity risk. Increase physical activity.")

    if age > 45:
        st.info("Age risk factor detected. Regular diabetes screening recommended.")

    if glucose < 120 and bmi < 25:
        st.success("Healthy metabolic indicators detected.")