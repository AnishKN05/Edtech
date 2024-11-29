import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Sample Data
data = {
    'age': [12, 15, 14, 13, 16],
    'interest_in_subject': [1, 2, 1, 1, 2],
    'previous_scores': [80, 60, 70, 85, 55],
    'recommended_subject': [1, 2, 1, 1, 2]  # 1: Math, 2: Science
}

df = pd.DataFrame(data)

# Feature and target variables
X = df[['age', 'interest_in_subject', 'previous_scores']]
y = df['recommended_subject']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Predict on test set
y_pred = model.predict(X_test)

# Accuracy
print(f'Accuracy: {accuracy_score(y_test, y_pred)}')

# Recommend subject for a new student
new_student = [[14, 2, 75]]  # Age, Interest in Science (2), Previous Score
recommended_subject = model.predict(new_student)
print(f'Recommended Subject: {"Math" if recommended_subject == 1 else "Science"}')
