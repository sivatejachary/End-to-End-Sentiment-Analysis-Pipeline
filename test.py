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
