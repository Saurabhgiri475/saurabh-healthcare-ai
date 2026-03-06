import pandas as pd
import streamlit as st

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier

@st.cache_data

def run_automl():

    df = pd.read_csv("data/diabetes.csv")

    X = df.drop("Outcome",axis=1)
    y = df["Outcome"]

    X_train,X_test,y_train,y_test = train_test_split(
        X,y,test_size=0.2,random_state=42
    )

    models = {

        "Logistic Regression":LogisticRegression(max_iter=1000),
        "Random Forest":RandomForestClassifier(),
        "SVM":SVC(),
        "KNN":KNeighborsClassifier()

    }

    results=[]

    for name,model in models.items():

        model.fit(X_train,y_train)

        pred=model.predict(X_test)

        acc=accuracy_score(y_test,pred)

        results.append((name,acc))

    result_df=pd.DataFrame(results,columns=["Model","Accuracy"])

    st.subheader("AutoML Model Comparison")

    st.dataframe(result_df)

    st.bar_chart(result_df.set_index("Model"))