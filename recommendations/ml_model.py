import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import joblib
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATASET_PATH = os.path.join(BASE_DIR, "construction_data.csv")
MODEL_PATH = os.path.join(BASE_DIR, "ml_model.pkl")


def train_model():
    # Load dataset
    data = pd.read_csv(DATASET_PATH)

    # Encode categorical variables
    label_encoders = {}
    for col in ["CementQuality", "BrickQuality", "SandQuality", "IronQuality", "EnvironmentalCondition", "Price"]:
        le = LabelEncoder()
        data[col] = le.fit_transform(data[col])
        label_encoders[col] = le

    # Features & Target
    X = data[["CementQuality",  "BrickQuality",
              "SandQuality",  "IronQuality",  "EnvironmentalCondition"]]
    y = data["Price"]

    # Split Data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train Model
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # Save Model & Encoders
    joblib.dump(model, MODEL_PATH)
    joblib.dump(label_encoders, os.path.join(BASE_DIR, "label_encoders.pkl"))

    print("Model trained and saved.")


def predict_price(cement_quality, brick_quality, sand_quality, iron_quality, env_condition):
    # Load model & encoders
    model = joblib.load(MODEL_PATH)
    label_encoders = joblib.load(os.path.join(BASE_DIR, "label_encoders.pkl"))

    # Encode categorical inputs
    cement_quality = label_encoders["CementQuality"].transform([cement_quality])[0]
    brick_quality = label_encoders["BrickQuality"].transform([brick_quality])[0]
    sand_quality = label_encoders["SandQuality"].transform([sand_quality])[0]
    iron_quality = label_encoders["IronQuality"].transform([iron_quality])[0]
    env_condition = label_encoders["EnvironmentalCondition"].transform([env_condition])[0]

    # Predict
    predicted_price = model.predict([[cement_quality,  brick_quality,
                                      sand_quality, iron_quality,  env_condition]])

    return round(predicted_price[0], 2)


if __name__ == "__main__":
    train_model()




import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import joblib
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
print(f"Base Directory: {BASE_DIR}")
DATASET_PATH = os.path.join(BASE_DIR, "construction_data.csv")
MODEL_PATH = os.path.join(BASE_DIR, "ml_model.pkl")
ENCODERS_PATH = os.path.join(BASE_DIR, "label_encoders.pkl")


def add_new_data(new_data):
    """
    Adds new rows to the CSV file without changing the model.

    new_data: List of dictionaries containing the new rows.
    """
    try:
        # Create a DataFrame from new data
        new_df = pd.DataFrame(new_data)
        print(new_df)
        # Check if the dataset already exists
        if os.path.exists(DATASET_PATH):
            # Append data without writing the header again
            new_df.to_csv(DATASET_PATH, mode='a', header=False, index=False)
            print("New data added to CSV.")
        else:
            # If the file does not exist, write the new data with header
            new_df.to_csv(DATASET_PATH, mode='w', header=True, index=False)
            print("CSV file created and data added.")

    except Exception as e:
        print(f"Error adding data to CSV: {e}")


def retrain_model():
    # Load dataset
    data = pd.read_csv(DATASET_PATH)

    # Ensure the necessary columns exist in the dataset
    required_columns = [
        "CementQuality", "BrickQuality", "SandQuality", "IronQuality", "EnvironmentalCondition",
        "Seller", "Price"
    ]
    if not all(col in data.columns for col in required_columns):
        print("Error: Missing required columns in the dataset.")
        return

    # Encode categorical variables
    label_encoders = {}
    for col in ["CementQuality", "BrickQuality", "SandQuality", "IronQuality", "EnvironmentalCondition", "Price"]:
        le = LabelEncoder()
        data[col] = le.fit_transform(data[col])
        label_encoders[col] = le

    # Features & Target
    X = data[["CementQuality", "BrickQuality", "SandQuality", "IronQuality", "EnvironmentalCondition"]]
    y = data["Price"]

    # Split Data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train Model
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # Save Model & Encoders
    joblib.dump(model, MODEL_PATH)
    joblib.dump(label_encoders, ENCODERS_PATH)

    print("Model retrained and saved.")


def predict_price(cement_quality, brick_quality, sand_quality, iron_quality, env_condition):
    # Load model & encoders
    model = joblib.load(MODEL_PATH)
    label_encoders = joblib.load(ENCODERS_PATH)

    # Encode categorical inputs
    cement_quality = label_encoders["CementQuality"].transform([cement_quality])[0]
    brick_quality = label_encoders["BrickQuality"].transform([brick_quality])[0]
    sand_quality = label_encoders["SandQuality"].transform([sand_quality])[0]
    iron_quality = label_encoders["IronQuality"].transform([iron_quality])[0]
    env_condition = label_encoders["EnvironmentalCondition"].transform([env_condition])[0]

    # Predict
    predicted_price = model.predict([[cement_quality, brick_quality, sand_quality, iron_quality, env_condition]])

    return round(predicted_price[0], 2)


# if __name__ == "__main__":
    # Example: Add new data
    # new_data = [
    #     {
    #         "ConstructionType": "Residential",
    #         "ConstructionName": "Building X",
    #         "CementQuality": "High",
    #         "CementPrice": 120,
    #         "BrickQuality": "Medium",
    #         "BrickPrice": 80,
    #         "SandQuality": "Good",
    #         "SandPrice": 50,
    #         "IronQuality": "Low",
    #         "IronPrice": 90,
    #         "EnvironmentalCondition": "Urban",
    #         "Seller": "Seller A",
    #         "Price": 250000
    #     },
    #     # Add more rows if needed
    # ]
    #
    # add_new_data(new_data)

    # Retrain the model with updated data
    # retrain_model()
