import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import joblib

# Load CSV
df = pd.read_csv("concrete.csv")

# Feature/Target split
X = df.drop(["strength"], axis=1)
Y = df[["strength"]]

# Train-test split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)

# Train model
model_1 = LinearRegression()
model_1.fit(X_train, Y_train)

# Save the model
joblib.dump(model_1, "concrete_strength_model.pkl")

print("Model trained and saved as concrete_strength_model.pkl")
