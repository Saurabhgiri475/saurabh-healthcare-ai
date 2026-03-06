import streamlit as st

def show_patient_card(name, gender, age, patient_id):

    st.markdown(f"""
    <div style="
        background:white;
        padding:20px;
        border-radius:12px;
        box-shadow:0px 3px 10px rgba(0,0,0,0.1);
        margin-bottom:20px;
    ">
        <h3>{name}</h3>
        <p><b>Patient ID:</b> {patient_id}</p>
        <p><b>Gender:</b> {gender}</p>
        <p><b>Age:</b> {age}</p>
    </div>
    """, unsafe_allow_html=True)