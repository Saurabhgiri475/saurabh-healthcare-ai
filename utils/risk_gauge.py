import plotly.graph_objects as go
import streamlit as st


def risk_gauge(score):

    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=score,
        title={'text': "Diabetes Risk Score"},
        gauge={
            'axis': {'range':[0,100]},
            'steps':[
                {'range':[0,30],'color':"lightgreen"},
                {'range':[30,70],'color':"yellow"},
                {'range':[70,100],'color':"red"}
            ]
        }
    ))

    st.plotly_chart(fig)