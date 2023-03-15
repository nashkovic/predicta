import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Load data into a Pandas DataFrame
data = pd.read_csv("match_data.csv")

# Prepare data by removing irrelevant columns and filling in missing values
data = data.drop(["Date", "Opponent"], axis=1)
data = data.fillna(0)

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    data.drop("Result", axis=1), data["Result"], test_size=0.3, random_state=42
)

# Train logistic regression model
lr = LogisticRegression()
lr.fit(X_train, y_train)

# Evaluate model on testing set
y_pred = lr.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.2f}")

# Make predictions on new data
new_data = pd.DataFrame({
    "Goals Scored": [20],
    "Goals Conceded": [10],
    "Shots": [100],
    "Shots on Target": [50],
    "Corners": [10],
    "Fouls Committed": [20],
    "Yellow Cards": [2],
    "Red Cards": [0],
})
prediction = lr.predict(new_data)
print(f"Prediction: {prediction}")
