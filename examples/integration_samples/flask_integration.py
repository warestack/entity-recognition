import json

from entity_recognition_lib import EntityRecognizer
from flask import Flask, jsonify, request

app = Flask(__name__)
recognizer = EntityRecognizer()

@app.route('/recognize', methods=['POST'])
def recognize():
    data = request.get_json()
    text = data.get('text', '')

    if not text:
        return jsonify({"error": "No text provided"}), 400

    # Process the text using the EntityRecognizer
    results = recognizer.process_texts([text])

    # Check if results are already a JSON string and convert if necessary
    if isinstance(results, str):
        results = json.loads(results)  # Convert JSON string to Python object

    # Return the results
    return results

if __name__ == '__main__':
    app.run(debug=True)
