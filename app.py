from flask import Flask, request, jsonify
import joblib
import string
from bs4 import BeautifulSoup

app = Flask(__name__)

# Load the trained model and the TF-IDF vectorizer
log_reg = joblib.load('logistic_regression_model.pkl')
tfidf_vectorizer = joblib.load('tfidf_vectorizer.pkl')

# Text Preprocessing Function
def preprocess_text(text):
    # Lowercase the text
    text = text.lower()

    # Remove HTML tags
    text = BeautifulSoup(text, "html.parser").get_text()

    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))
    
    return text

# Define the /predict route
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get the JSON data from the request
        data = request.get_json()

        print(f"Received data: {data}")  # Debugging line

        if not data or 'review_text' not in data:
            return jsonify({'error': 'No review_text provided'}), 400

        review_text = data['review_text']

        # Step 1: Preprocess the review text
        cleaned_review = preprocess_text(review_text)

        # Step 2: Vectorize the review and make prediction using Logistic Regression (TF-IDF model)
        review_tfidf = tfidf_vectorizer.transform([cleaned_review])
        prediction = log_reg.predict(review_tfidf)[0]

        # Convert numeric prediction to sentiment label
        sentiment = "positive" if prediction == 1 else "negative"

        # Step 3: Return the result as JSON
        response = {'sentiment_prediction': sentiment}
        print(f"Sending response: {response}")  # Debugging line

        return jsonify(response)

    except Exception as e:
        error_response = {'error': str(e)}
        print(f"Error: {error_response}")  # Debugging line
        return jsonify(error_response), 500

if __name__ == '__main__':
    app.run(debug=True)
