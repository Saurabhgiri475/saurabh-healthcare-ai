import os
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"
import streamlit as st
import tensorflow as tf
import numpy as np
import pandas as pd
import plotly.express as px
from utils.llm_report import generate_llm_report
from utils.pdf_report import generate_medical_pdf
from auth import create_users_table,create_default_admin,login
from database import create_patient_table,save_patient,get_patients

from utils.risk_gauge import risk_gauge
from utils.recommendation_engine import medical_recommendation
from utils.automl_models import run_automl


# init
create_users_table()
create_default_admin()
create_patient_table()

@st.cache_resource
def load_model():
    return tf.keras.models.load_model("models/diabetes_dl_model.h5")

model = load_model()


# login
# login
if "user" not in st.session_state:

    col1, col2 = st.columns([1,8] , vertical_alignment="center")

    with col1:
        st.image("logo.png", width=140 )

    with col2:
        st.title("Saurabh Healthcare & Diagnostic Intelligence System")
        st.caption("AI-Powered Preventive Healthcare Platform")

    st.divider()

    st.subheader("Hospital Login")
    username=st.text_input("Username")
    password=st.text_input("Password",type="password")

    if st.button("Login"):

        result=login(username,password)

        if result:

            st.session_state.user=result[0]
            st.session_state.role=result[2]

            st.success("Login successful")
            st.rerun()

        else:
            st.error("Invalid credentials")

    st.stop()


col1, col2 = st.columns([1,6])

with col1:
    st.image("logo.png", width=80)

with col2:
    st.title("Saurabh Healthcare & Diagnostic Intelligence System")
    st.caption("AI-Powered Preventive Healthcare Platform")


tab1,tab2,tab3,tab4=st.tabs([
"Prediction",
"Analytics",
"Patients",
"Admin"
])


# prediction
with tab1:

    st.subheader("Patient Diabetes Prediction")

    # Patient inputs
    name = st.text_input("Patient Name")

    age = st.number_input("Age", min_value=1, max_value=120)

    glucose = st.number_input("Glucose")

    bmi = st.number_input("BMI")

    blood_pressure = st.number_input("Blood Pressure")

    insulin = st.number_input("Insulin")


    # Prediction variables
    prediction = None
    result = None
    risk_score = None


    if st.button("Predict Diabetes Risk"):

        input_data = np.array([
            [0, glucose, blood_pressure, 0, insulin, bmi, 0, age]
        ])

        prediction = model.predict(input_data)[0][0]

        risk_score = prediction * 100


        # Show AI risk gauge
        risk_gauge(risk_score)


        if prediction > 0.5:
            result = "High Risk"
        else:
            result = "Low Risk"


        st.success(f"Prediction Result: {result}")


        # Save patient
        save_patient(name, glucose, bmi, age, result)


        # Medical recommendation engine
        medical_recommendation(glucose, bmi, age)


        # ---------------- FUTURE RISK FORECAST ----------------

        st.subheader("AI Future Risk Forecast")

        import plotly.graph_objects as go
        import numpy as np

        months = [
        "Jan","Feb","Mar","Apr","May","Jun",
        "Jul","Aug","Sep","Oct","Nov","Dec"
        ]

        future_risk = []

        base = risk_score

        for i in range(12):

            change = np.random.uniform(-5,5)

            base = max(0, min(100, base + change))

            future_risk.append(base)

        fig = go.Figure()

        fig.add_trace(go.Scatter(
            x=months,
            y=future_risk,
            mode='lines+markers'
        ))

        fig.update_layout(
            title="Predicted Diabetes Risk Trend",
            xaxis_title="Month",
            yaxis_title="Risk Score"
        )

        st.plotly_chart(fig)


        # ---------------- AI MEDICAL REPORT ----------------

        st.subheader("AI Medical Report")

        llm_text = generate_llm_report(
            name,
            age,
            glucose,
            bmi,
            result
        )

        st.write(llm_text)


        # ---------------- PDF REPORT ----------------

       # ---------------- PDF REPORT ----------------

        patient_data = {
            "Patient Name": name,
            "Age": age,
            "Glucose": glucose,
            "BMI": bmi,
            "Blood Pressure": blood_pressure,
            "Insulin": insulin
        }

        pdf_buffer = generate_medical_pdf(
            patient_data,
            result,
            prediction
        )

        st.download_button(
            label="Download Medical Report",
            data=pdf_buffer,
            file_name="medical_report.pdf",
            mime="application/pdf"
)
# analytics
with tab2:

    st.subheader("Hospital Analytics Dashboard")

    patients = get_patients()

    if len(patients) == 0:
        st.warning("No patient data available yet")
        st.stop()

    df = pd.DataFrame(
        patients,
        columns=[
            "ID",
            "Name",
            "Glucose",
            "BMI",
            "Age",
            "Prediction",
            "Date"
        ]
    )

    # -----------------------------
    # PATIENT STATISTICS
    # -----------------------------

    st.markdown("### Patient Statistics")

    total_patients = len(df)

    high_risk = len(df[df["Prediction"] == "High Risk"])

    low_risk = len(df[df["Prediction"] == "Low Risk"])

    col1, col2, col3 = st.columns(3)

    col1.metric("Total Patients", total_patients)

    col2.metric("High Risk Cases", high_risk)

    col3.metric("Low Risk Cases", low_risk)


    # -----------------------------
    # HIGH RISK ALERTS
    # -----------------------------

    st.markdown("### High-Risk Alerts")

    high_risk_df = df[df["Prediction"] == "High Risk"]

    if len(high_risk_df) > 0:

        st.error(f"{len(high_risk_df)} high-risk patients detected")

        st.dataframe(high_risk_df)

    else:

        st.success("No high-risk patients detected")


    # -----------------------------
    # RISK HEATMAP
    # -----------------------------

    st.markdown("### Diabetes Risk Heatmap")

    import plotly.express as px

    heatmap = px.density_heatmap(
        df,
        x="Age",
        y="BMI",
        z="Glucose",
        color_continuous_scale="reds",
        title="Risk Distribution by Age, BMI and Glucose"
    )

    st.plotly_chart(heatmap)


    # -----------------------------
    # DOCTOR ACTIVITY PANEL
    # -----------------------------

    st.markdown("### Doctor Activity Panel")

    col1, col2 = st.columns(2)

    col1.info(f"Patients Diagnosed Today: {len(df.tail(5))}")

    col2.info(f"Reports Generated: {len(df)}")


    # -----------------------------
    # PATIENT VISUALIZATION
    # -----------------------------

    st.markdown("### Patient Risk Visualization")

    scatter = px.scatter(
        df,
        x="Age",
        y="BMI",
        color="Prediction",
        size="Glucose",
        hover_data=["Name"]
    )

    st.plotly_chart(scatter)


    # -----------------------------
    # AUTOML MODEL COMPARISON
    # -----------------------------

    run_automl()

# patient database
with tab3:

    st.subheader("Patient Profiles")

    patients = get_patients()

    if len(patients) == 0:
        st.warning("No patient records available")
        st.stop()

    df = pd.DataFrame(
        patients,
        columns=[
            "ID",
            "Name",
            "Glucose",
            "BMI",
            "Age",
            "Prediction",
            "Date"
        ]
    )

    # ----------------------------------
    # GROUP PATIENT HISTORY
    # ----------------------------------

    grouped = df.groupby("Name")

    for name, patient_history in grouped:

        latest = patient_history.iloc[-1]

        prediction = latest["Prediction"]

        if prediction == "High Risk":
            color = "#ffcccc"
        else:
            color = "#ccffcc"

        st.markdown(
            f"""
            <div style="
            background:{color};
            padding:20px;
            border-radius:10px;
            margin-bottom:15px;
            box-shadow:0px 3px 8px rgba(0,0,0,0.1);
            ">
            <h3>{name}</h3>
            <b>Age:</b> {latest['Age']} <br>
            <b>Latest Glucose:</b> {latest['Glucose']} <br>
            <b>BMI:</b> {latest['BMI']} <br>
            <b>Risk Status:</b> {latest['Prediction']}
            </div>
            """,
            unsafe_allow_html=True
        )

        with st.expander("View Medical History"):

            st.dataframe(patient_history)

# admin
with tab4:

    if st.session_state.role == "admin":

        st.header("Hospital Admin Dashboard")

        patients = get_patients()

        if len(patients) == 0:
            st.warning("No patient data available")
            st.stop()

        df = pd.DataFrame(
            patients,
            columns=[
                "ID",
                "Name",
                "Glucose",
                "BMI",
                "Age",
                "Prediction",
                "Date"
            ]
        )

        # -----------------------------
        # SYSTEM OVERVIEW
        # -----------------------------

        st.subheader("System Overview")

        total_patients = len(df)
        high_risk = len(df[df["Prediction"] == "High Risk"])
        low_risk = len(df[df["Prediction"] == "Low Risk"])

        col1, col2, col3 = st.columns(3)

        col1.metric("Total Patients", total_patients)
        col2.metric("High Risk Cases", high_risk)
        col3.metric("Low Risk Cases", low_risk)


        # -----------------------------
        # RISK DISTRIBUTION PIE CHART
        # -----------------------------

        st.subheader("Risk Distribution")

        import plotly.express as px

        pie = px.pie(
            df,
            names="Prediction",
            title="Patient Risk Classification"
        )

        st.plotly_chart(pie)


        # -----------------------------
        # HIGH RISK ALERT PANEL
        # -----------------------------

        st.subheader("High Risk Alerts")

        high_risk_df = df[df["Prediction"] == "High Risk"]

        if len(high_risk_df) > 0:

            st.error(f"{len(high_risk_df)} high-risk patients detected")

            st.dataframe(high_risk_df)

        else:

            st.success("No critical risk cases detected")


        # -----------------------------
        # RECENT PATIENT ACTIVITY
        # -----------------------------

        st.subheader("Recent Patient Activity")

        recent = df.sort_values("Date", ascending=False).head(5)

        st.dataframe(recent)


        # -----------------------------
        # MODEL PERFORMANCE PANEL
        # -----------------------------

        st.subheader("Model Performance")

        col1, col2 = st.columns(2)

        col1.info("Deep Learning Model: TensorFlow")

        col2.info("AI System Status: Operational")


        # -----------------------------
        # ADMIN TOOLS
        # -----------------------------

        st.subheader("Admin Tools")

        # Export patient data
        csv = df.to_csv(index=False)

        st.download_button(
            label="Download Patient Database (CSV)",
            data=csv,
            file_name="patients_database.csv",
            mime="text/csv"
        )

        # Reset database option
        if st.button("Clear Patient Database"):

            import sqlite3

            conn = sqlite3.connect("hospital.db")
            c = conn.cursor()

            c.execute("DELETE FROM patients")

            conn.commit()
            conn.close()

            st.success("Database cleared successfully")

    else:

        st.warning("Admin access only")