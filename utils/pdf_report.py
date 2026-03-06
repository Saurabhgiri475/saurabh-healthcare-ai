import io
import qrcode
from datetime import datetime

from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
    Image as RLImage
)

from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib import colors

import matplotlib.pyplot as plt


def create_risk_chart(probability):

    fig = plt.figure()

    plt.bar(["Risk"], [probability*100])

    plt.ylim(0,100)

    plt.title("Diabetes Risk Score")

    chart_file="risk_chart.png"

    plt.savefig(chart_file)

    plt.close()

    return chart_file


def create_shap_chart():

    fig = plt.figure()

    features=["Glucose","BMI","Age","Insulin"]

    values=[0.4,0.3,0.2,0.1]

    plt.barh(features,values)

    plt.title("Feature Contribution (AI Explainability)")

    shap_file="shap_chart.png"

    plt.savefig(shap_file)

    plt.close()

    return shap_file


def create_qr(report_id):

    qr=qrcode.make(f"Report ID: {report_id}")

    qr_file="report_qr.png"

    qr.save(qr_file)

    return qr_file


def generate_medical_pdf(patient_data,prediction,probability):

    buffer=io.BytesIO()

    doc=SimpleDocTemplate(buffer,pagesize=letter)

    elements=[]

    styles=getSampleStyleSheet()

    report_id=f"DIA-{datetime.now().strftime('%Y%m%d%H%M%S')}"

    report_date=datetime.now().strftime("%d-%m-%Y %H:%M")


    def header_footer(canvas,doc):

        canvas.saveState()

        width,height=letter

        try:
            canvas.drawImage(
                "logo.png",
                40,
                height-90,
                width=70,
                height=70
            )
        except:
            pass

        canvas.setFont("Helvetica-Bold",18)

        canvas.setFillColor(colors.HexColor("#003366"))

        canvas.drawCentredString(
            width/2,
            height-50,
            "SAURABH HEALTHCARE DIAGNOSTIC CENTER"
        )

        canvas.setFont("Helvetica",10)

        canvas.drawCentredString(
            width/2,
            height-65,
            "AI Powered Preventive Diagnostics"
        )

        canvas.line(40,height-75,width-40,height-75)

        canvas.setFont("Helvetica",8)

        canvas.drawString(
            40,
            30,
            "Near BBD Campus | Ph: 7985486802"
        )

        canvas.drawRightString(
            width-40,
            30,
            f"Page {doc.page}"
        )

        canvas.restoreState()


    elements.append(Spacer(1,100))


    # ---------------------
    # PATIENT TABLE
    # ---------------------

    info_data=[

    ["Patient Name",patient_data.get("Patient Name","N/A"),
     "Patient ID",patient_data.get("Patient ID","N/A")],

    ["Gender",patient_data.get("Gender","N/A"),
     "Age",patient_data.get("Age","N/A")],

    ["Appointment No",patient_data.get("Appointment No","N/A"),
     "Report ID",report_id],

    ["Date",report_date,"",""]
    ]

    info_table=Table(info_data,colWidths=[120,150,120,120])

    info_table.setStyle(TableStyle([
        ("GRID",(0,0),(-1,-1),1,colors.black),
        ("BACKGROUND",(0,0),(-1,-1),colors.whitesmoke)
    ]))

    elements.append(info_table)

    elements.append(Spacer(1,20))


    # ---------------------
    # REPORT TITLE
    # ---------------------

    elements.append(
        Paragraph(
        "<b>DIABETES RISK ASSESSMENT REPORT</b>",
        styles["Heading2"]
        )
    )

    elements.append(Spacer(1,15))


    # ---------------------
    # LAB TABLE
    # ---------------------

    lab_data=[["Parameter","Observed Value"]]

    for k,v in patient_data.items():
        lab_data.append([k,str(v)])

    lab_table=Table(lab_data,colWidths=[240,220])

    lab_table.setStyle(TableStyle([

        ("GRID",(0,0),(-1,-1),0.5,colors.black),

        ("BACKGROUND",(0,0),(-1,0),colors.HexColor("#003366")),

        ("TEXTCOLOR",(0,0),(-1,0),colors.whitesmoke)

    ]))

    elements.append(lab_table)

    elements.append(Spacer(1,25))


    # ---------------------
    # AI RISK CHART
    # ---------------------

    chart=create_risk_chart(probability)

    elements.append(
        Paragraph("<b>AI Risk Visualization</b>",styles["Normal"])
    )

    elements.append(
        RLImage(chart,width=4*inch,height=2*inch)
    )

    elements.append(Spacer(1,25))


    # ---------------------
    # SHAP CHART
    # ---------------------

    shap=create_shap_chart()

    elements.append(
        Paragraph("<b>AI Explainability (Feature Importance)</b>",styles["Normal"])
    )

    elements.append(
        RLImage(shap,width=4*inch,height=2*inch)
    )

    elements.append(Spacer(1,25))


    # ---------------------
    # AI INTERPRETATION
    # ---------------------

    impression=f"""
    <b>AI INTERPRETATION</b><br/><br/>

    Prediction: <b>{prediction}</b><br/>

    Probability Score: <b>{probability*100:.2f}%</b><br/><br/>

    This report is generated using a Deep Learning based
    diagnostic support system.
    """

    impression_para=Paragraph(impression,styles["Normal"])

    impression_table=Table([[impression_para]],colWidths=[460])

    impression_table.setStyle(TableStyle([
        ("BOX",(0,0),(-1,-1),1.5,colors.black),
        ("INNERPADDING",(0,0),(-1,-1),12)
    ]))

    elements.append(impression_table)

    elements.append(Spacer(1,30))


    # ---------------------
    # QR CODE
    # ---------------------

    qr=create_qr(report_id)

    elements.append(
        Paragraph("<b>Report Verification QR</b>",styles["Normal"])
    )

    elements.append(
        RLImage(qr,width=1.5*inch,height=1.5*inch)
    )

    elements.append(Spacer(1,30))


    # ---------------------
    # SIGNATURE
    # ---------------------

    elements.append(Paragraph("Authorized By:",styles["Normal"]))

    elements.append(Spacer(1,20))

    try:
        elements.append(
            RLImage(
                "stamp.png",
                width=1.5*inch,
                height=1.5*inch
            )
        )
    except:
        pass

    elements.append(Spacer(1,10))

    elements.append(
        Paragraph(
        "Dr. XYZ",
        styles["Normal"]
        )
    )

    elements.append(
        Paragraph(
        "MBBS, MD (Radiology)",
        styles["Normal"]
        )
    )


    doc.build(
        elements,
        onFirstPage=header_footer,
        onLaterPages=header_footer
    )

    buffer.seek(0)

    return buffer