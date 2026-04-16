import pandas as pd
from sklearn.linear_model import LinearRegression
import mlflow
import mlflow.sklearn
import joblib

# Set experiment (VERY IMPORTANT)
mlflow.set_experiment("house-price-exp")

# Load data
data = pd.read_csv("data.csv")
X = data[['area', 'rooms']]
y = data['price']

with mlflow.start_run():

    model = LinearRegression()
    model.fit(X, y)

    # Log parameter
    mlflow.log_param("model", "LinearRegression")

    # Log metric
    r2 = model.score(X, y)
    mlflow.log_metric("r2_score", r2)

    # Log model
    mlflow.sklearn.log_model(model, "model")

    # Save model locally
    joblib.dump(model, "model.pkl")

print("Training Done")