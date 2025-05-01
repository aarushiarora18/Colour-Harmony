import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# Load dataset
df = pd.read_csv('dataset.csv')

# Features and target
X = df[['R', 'G', 'B']]
y = df['season']

# Encode season labels
le = LabelEncoder()
y_encoded = le.fit_transform(y)

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(X, y_encoded, test_size=0.2, random_state=42)

# Train model
model = KNeighborsClassifier(n_neighbors=3)
model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)
print("Model accuracy:", accuracy_score(y_test, y_pred))

# Predict example
import numpy as np

# Predict example with proper column names
sample_rgb = pd.DataFrame(np.array([[210, 160, 145]]), columns=['R','G','B'])
predicted = model.predict(sample_rgb)
season_result = le.inverse_transform(predicted)
print("Predicted Season for", sample_rgb.values[0], "→", season_result[0])
