# End-to-End-Sentiment-Analysis-Pipeline

This repository contains a sentiment analysis pipeline for IMDb movie reviews. The project is implemented in Python and uses a **Logistic Regression** model to classify movie reviews as **positive** or **negative**. The pipeline is connected to an SQLite database (`imdb_reviews.db`) containing the review data.

---

## **Deliverables**

### 1. **Code Repository**
The repository contains the following files:

- **`data_setup.py`**: Script to set up the SQLite database and load the IMDb dataset into the database.
- **`train_model.py`**: Script for training the logistic regression model on the IMDb dataset.
- **`logistic_regression_model.pkl`**: Saved Logistic Regression model after training.
- **`tfidf_vectorizer.pkl`**: Saved TF-IDF vectorizer used for transforming the text data.
- **`app.py`**: A simple Flask application to serve the sentiment analysis model.
- **`requirements.txt`**: A list of Python dependencies.
- **`imdb_reviews.db`**: SQLite database containing the IMDb reviews.
- **`README.md`**: Project documentation.
- **`.gitignore`**: Git ignore file for Python-related files.

### 2. **Database Schema**

- **SQLite Database (`imdb_reviews.db`)**:
    - The database file is named `imdb_reviews.db`.
    - The table `imdb_reviews` contains the following columns:
        - `id` (INTEGER, Primary Key)
        - `review_text` (TEXT)
        - `sentiment` (TEXT)
        - `cleaned_review` (TEXT, Optional, created after data cleaning)

    - To create the table in SQLite:
    ```sql
    CREATE TABLE IF NOT EXISTS imdb_reviews (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        review_text TEXT NOT NULL,
        sentiment TEXT NOT NULL,
        cleaned_review TEXT
    );
    ```

### 3. **README**

#### **Project Setup**

1. **Clone the repository:**
    ```bash
    git clone [https://github.com/yourusername/imdb-sentiment-analysis](https://github.com/sivatejachary/End-to-End-Sentiment-Analysis-Pipeline.git
    cd End-to-End-Sentiment-Analysis-Pipeline
    ```

2. **Install dependencies:**
    - Ensure that you have Python 3.6+ installed.
    - Install required Python libraries:
    ```bash
    pip install -r requirements.txt
    ```

3. **Set up the SQLite database:**
    - If you don't have the IMDb dataset, download it from [this Kaggle link](https://www.kaggle.com/datasets/lakshmi25npathi/imdb-dataset-of-50k-movie-reviews).
    - Run the `data_setup.py` script to load the dataset into the `imdb_reviews.db` database.
    ```bash
    python data_setup.py
    ```

---

#### **Data Acquisition**

- The dataset used in this project contains 50,000 movie reviews.
- The data was loaded from a CSV file into an SQLite database using the `data_setup.py` script.
- The dataset includes the review text and sentiment labels (positive/negative).

---

#### **Run Instructions**

1. **Training the Model:**
    - Once the dataset is loaded into the database, you can train the model by running:
    ```bash
    python train_model.py
    ```

2. **Starting the Flask Server:**
    - The `app.py` file contains a simple Flask app to serve the sentiment analysis model.
    - Start the Flask server:
    ```bash
    python app.py
    ```

3. **Testing the Endpoint:**
    - Once the server is running, you can send `POST` requests to the `/predict` endpoint to get sentiment predictions.
    - Example `curl` command to test the endpoint:
    ```bash
    curl -X POST -H "Content-Type: application/json" -d '{"review": "This movie is amazing!"}' http://127.0.0.1:5000/predict
    ```

    - Example response:
    ```json
    {
        "prediction": "positive"
    }
    ```

---
- **Python Code to Test the Model**:
      You can also use the following Python script to test the model via a `POST` request to the Flask server:

  ```python
      import requests
      import json

      # The URL of your Flask app
      url = 'http://127.0.0.1:5000/predict'

      # Review text to send in the POST request
      data = {
          "review_text": "This movie was waste of time"
      }

      # Send the POST request
      response = requests.post(url, json=data)

      # Print the raw response text to debug
      print(f"Raw response: {response.text}")

      # Attempt to print the JSON response
      try:
          print(response.json())
      except Exception as e:
          print(f"Error while decoding JSON: {e}")
  ```

  **Explanation:**
      - The script sends a `POST` request to the Flask app with a review text.
      - It then prints the raw response from the Flask server and attempts to decode the response into JSON format.

---
#### **Model Info**

- **Chosen Model Approach**: Logistic Regression was selected as the classifier for sentiment analysis.
- **Key Results**:
    - Accuracy on the test set: **87.50%**
    - Precision: **89.02%**
    - Recall: **86.05%**
    - F1-Score: **87.51%**

---
---

## **Requirements**

- Python 3.6+
- Libraries listed in `requirements.txt`:
  - pandas
  - scikit-learn
  - Flask
  - beautifulsoup4
  - numpy
  - string

---

## **Notes**

- The Flask app assumes that the model and the database are available and the model has already been trained using `train_model.py`.
- For future improvements, the model could be extended to include additional classifiers like Random Forest, SVM, or neural networks.
