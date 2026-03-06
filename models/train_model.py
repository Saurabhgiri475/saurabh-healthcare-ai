
import pandas as pd
import tensorflow as tf
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

data = pd.read_csv("../data/diabetes.csv")

X = data.drop("Outcome",axis=1)
y = data["Outcome"]

scaler = StandardScaler()
X = scaler.fit_transform(X)

X_train,X_test,y_train,y_test = train_test_split(
    X,y,test_size=0.2,random_state=42
)

model = tf.keras.Sequential([
    tf.keras.layers.Dense(16,activation="relu",input_shape=(8,)),
    tf.keras.layers.Dense(8,activation="relu"),
    tf.keras.layers.Dense(1,activation="sigmoid")
])

model.compile(
    optimizer="adam",
    loss="binary_crossentropy",
    metrics=["accuracy"]
)

model.fit(X_train,y_train,epochs=50,batch_size=16)

model.save("diabetes_dl_model.h5")

print("Deep Learning model trained and saved.")
