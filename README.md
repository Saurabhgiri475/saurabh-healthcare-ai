---

# 🏥 Saurabh Healthcare & Diagnostic Intelligence System

### AI-Powered Preventive Healthcare & Diabetes Risk Prediction Platform

---

# 📌 Project Overview

**Saurabh Healthcare & Diagnostic Intelligence System** is an **AI-powered healthcare analytics platform** designed to assist medical professionals in **predicting diabetes risk and generating automated medical reports**.

The system simulates a **real-world diagnostic center workflow** using **Artificial Intelligence, Deep Learning, and Data Analytics**.

The platform integrates:

🧠 Deep Learning Diabetes Prediction
📊 Interactive Hospital Analytics Dashboard
📄 AI Medical Report Generation
📑 Professional PDF Medical Reports
🗄 Patient History Database (SQLite)
🔐 Secure Login Authentication
📈 Risk Visualization Charts
🧬 Medical Recommendation Engine

---

# 🚀 Features

---

# 🔮 1. Diabetes Risk Prediction

Predicts whether a patient is at **risk of diabetes** using a Deep Learning model.

### Input Parameters

```
Age
Glucose Level
BMI
Blood Pressure
Insulin
```

### Output

```
Diabetes Probability %
Risk Level (Low / Medium / High)
AI Diagnosis Recommendation
```

---

# 📊 2. Hospital Analytics Dashboard

Interactive medical analytics powered by **Plotly**.

Displays:

• Patient Risk Distribution
• BMI vs Age Risk Scatter Plot
• Glucose Level Visualization
• Patient Statistics

Helps doctors **analyze health trends quickly**.

---

# 📈 3. Future Risk Forecast

AI visualization predicts **future diabetes risk trends**.

Used for:

• monitoring disease progression
• predicting patient health trajectory
• preventive healthcare planning

---

# 📄 4. AI Medical Report Generator

Automatically generates **AI-powered diagnostic reports** including:

✔ Patient medical summary
✔ Risk explanation
✔ Lifestyle recommendations
✔ Preventive healthcare suggestions

---

# 📑 5. Professional Medical Report (PDF)

Generated using **ReportLab**.

Report includes:

• Hospital Logo
• Patient Details
• Medical Parameters
• AI Risk Analysis
• Medical Recommendation
• Authorized Stamp
• Report ID & Timestamp

---

# 🗄 6. Patient Database System

SQLite based patient management system.

Stores:

```
Patient Name
Age
Gender
Medical Parameters
Prediction Probability
Risk Level
```

Allows healthcare staff to **track patient history and predictions**.

---

# 🔐 7. Authentication System

Secure login system for healthcare staff.

Login roles:

```
Admin
Doctor
```

Prevents unauthorized access to patient data.

---

# 📊 8. Risk Visualization Tools

The system generates medical charts including:

📈 Risk Forecast Graph
📊 Patient Risk Scatter Plot
📉 Analytics Dashboard

Helps doctors understand patient risk **visually and quickly**.

---

# 🧠 Machine Learning Details

Dataset used:

```
PIMA Diabetes Dataset
```

### Model Type

Deep Learning Neural Network

### Features Used

```
Age
Glucose
BMI
Blood Pressure
Insulin
Skin Thickness
Pregnancies
Diabetes Pedigree Function
```

### Output

```
Probability Score
Binary Prediction
Risk Classification
```

---

# 🖥 System Architecture

```
Patient Input → Streamlit Interface → Deep Learning Model → Risk Prediction
                                      ↓
                              Patient Database
                                      ↓
                             Medical Report Generator
                                      ↓
                           Analytics Dashboard
```

---

# 📦 Installation Guide

---

## 1️⃣ Clone Repository

```
git clone https://github.com/Saurabhgiri475/saurabh-healthcare-ai.git
```

```
cd saurabh-healthcare-ai
```

---

## 2️⃣ Create Virtual Environment

```
python -m venv venv
```

Activate environment

Windows

```
venv\Scripts\activate
```

Linux / Mac

```
source venv/bin/activate
```

---

## 3️⃣ Install Dependencies

```
pip install -r requirements.txt
```

---

## 4️⃣ Run Application

```
streamlit run app.py
```

---

# 🌐 Live Deployment

The system is deployed on **Streamlit Cloud**.

```
https://saurabh-healthcare-ai-d.streamlit.app/
```

---

# 🗃 Project Structure

```
saurabh-healthcare-ai
│
├── app.py
├── auth.py
├── database.py
│
├── models
│   └── diabetes_dl_model.h5
│
├── utils
│   ├── llm_report.py
│   ├── pdf_report.py
│   ├── risk_gauge.py
│   ├── automl_models.py
│   └── recommendation_engine.py
│
├── hospital.db
├── logo.png
├── stamp.png
├── requirements.txt
└── README.md
```

---

# 👨‍⚕️ Admin Credentials

Default login:

```
Username: admin
Password: admin123
```

Doctor:

```
Username: doctor
Password: doctor123
```

⚠ Change credentials in production.

---

# 📊 System Interface

System includes:

✔ Login Interface
✔ AI Prediction Dashboard
✔ Patient Profile Cards
✔ Risk Analytics Dashboard
✔ Medical Report Generator

---

# 🔒 Security Notes

⚠ Do NOT expose:

```
Database credentials
API keys
Production passwords
```

Use **environment variables (.env)** in production deployments.

---

# 🌍 Future Improvements

Planned upgrades:

• AI Doctor Chatbot
• Medical Image Diagnosis
• Appointment Booking System
• Multi-disease Prediction
• Cloud Hospital ERP System
• Role Based Access Control

---

# 👨‍💻 Developed By

### **Saurabh Giri**

AI & Healthcare Technology Developer

BBD Northern India Institute of Technology

GitHub:

```
https://github.com/Saurabhgiri475
```

---

# 📜 License

This project is created for **educational and research purposes**.

---

⭐ If you found this project useful, please **give it a star on GitHub**.

---

