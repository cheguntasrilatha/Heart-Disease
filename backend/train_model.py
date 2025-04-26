import pandas as pd
import numpy as np
import pickle
import os
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier

# Load the dataset
df = pd.read_csv('heart.csv')

# Replace '?' with NaN
df.replace('?', np.nan, inplace=True)

# Convert all columns to numeric (force errors to NaN)
df = df.apply(pd.to_numeric, errors='coerce')

# Drop rows with any NaN values
df.dropna(inplace=True)

print(f"✅ Data loaded: {df.shape[0]} rows, {df.shape[1]} columns")
print("Columns in dataset:", df.num)


# Split features and target
X = df.drop('num', axis=1)
y = df['num']

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Scale the data
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Train the model
model = RandomForestClassifier()
model.fit(X_train_scaled, y_train)

# Save the model and scaler
os.makedirs('models', exist_ok=True)
with open('models/heart_model.pkl', 'wb') as f:
    pickle.dump(model, f)
with open('models/scaler.pkl', 'wb') as f:
    pickle.dump(scaler, f)

# Print accuracy
print(f"🎯 Model accuracy: {model.score(X_test_scaled, y_test):.2f}")
print("✅ Model and scaler saved successfully.")
