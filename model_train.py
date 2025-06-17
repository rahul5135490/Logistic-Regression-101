# train_model.py
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib

# Step 1: Data Load karo
iris = load_iris()
X = iris.data
y = (iris.target == 0).astype(int)  # Binary classification

# Step 2: Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 3: Model Train
model = LogisticRegression()
model.fit(X_train, y_train)

# Step 4: Accuracy Check
y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))

# Step 5: Save the model
joblib.dump(model, 'logistic_model.pkl')
