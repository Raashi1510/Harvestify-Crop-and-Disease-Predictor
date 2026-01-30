import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import pickle
import os

# Create models folder if not exists
if not os.path.exists('models'):
    os.makedirs('models')

# Load dataset
data = pd.read_csv('Crop_recommendation.csv')

# Select numeric features only
feature_columns = ['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall']
X = data[feature_columns].astype(float)

# Target column
y = data['Crop']

# Train model
model = RandomForestClassifier()
model.fit(X, y)

# Save model
with open('models/crop_model.pkl', 'wb') as f:
    pickle.dump(model, f)

print("Model trained and saved successfully.")

