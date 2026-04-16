import argparse
import joblib
import numpy as np


def main():
    parser = argparse.ArgumentParser(description="Make a prediction with the trained model.")
    parser.add_argument("feature1", type=float, help="Value for feature1")
    parser.add_argument("feature2", type=float, help="Value for feature2")
    args = parser.parse_args()

    model = joblib.load("model.joblib")
    features = np.array([[args.feature1, args.feature2]])
    prediction = model.predict(features)

    print(f"prediction: {prediction[0]:.4f}")


if __name__ == "__main__":
    main()
