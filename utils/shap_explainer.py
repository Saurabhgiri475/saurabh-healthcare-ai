import shap
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np


def show_shap(model,input_data,feature_names):

    df = pd.DataFrame(input_data,columns=feature_names)

    background = np.zeros((1,len(feature_names)))

    explainer = shap.KernelExplainer(model.predict,background)

    shap_values = explainer.shap_values(df)

    fig, ax = plt.subplots()

    shap.summary_plot(
        shap_values,
        df,
        feature_names=feature_names,
        plot_type="bar",
        show=False
    )

    st.pyplot(fig)