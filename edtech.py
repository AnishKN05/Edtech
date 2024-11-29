from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Initialize Flask app
app = Flask(__name__)

# Enable CORS for all routes
CORS(app)  # This allows all domains to access the API

# Sample data for training
data = {
    'age': [12, 15, 14, 13, 16],
    'interest_in_subject': [1, 2, 1, 1, 2],
    'previous_scores': [80, 60, 70, 85, 55],
    'recommended_subject': [1, 2, 1, 1, 2]  # 1: Math, 2: Science
}

# Create DataFrame
df = pd.DataFrame(data)

# Feature and target variables
X = df[['age', 'interest_in_subject', 'previous_scores']]
y = df['recommended_subject']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=40)

# Initialize and train the Random Forest model
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# Define Flask endpoint
@app.route('/api/recommend', methods=['POST'])
def recommend_subject():
    """
    Endpoint to recommend a subject based on input data (age, interest, score).
    """
    try:
        # Get JSON data from the request
        input_data = request.json

        # Validate required fields
        if not all(key in input_data for key in ['age', 'interest', 'score']):
            return jsonify({'error': 'Invalid input. Please provide age, interest, and score.'}), 400

        # Create a DataFrame for the new student data
        new_student = pd.DataFrame([[
            input_data['age'],
            input_data['interest'],
            input_data['score']
        ]], columns=['age', 'interest_in_subject', 'previous_scores'])

        # Predict the recommended subject
        recommended_subject = model.predict(new_student)[0]

        # Convert numeric result to a readable subject
        subject = "Math" if recommended_subject == 1 else "Science"

        # Return the result as JSON
        return jsonify({'recommended_subject': subject}), 200

    except Exception as e:
        # Handle any server-side errors
        return jsonify({'error': str(e)}), 500

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
