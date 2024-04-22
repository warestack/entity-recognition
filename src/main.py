import json
from nlp.entity_recognition import EntityRecognizer

# Create an instance of the recognizer
recognizer = EntityRecognizer()

# Texts you want to process
texts = [
    "I need an Express.js Mongo database backend",
    "and a React TypeScript frontend for my project"
]

# Get results as a JSON string
results_json = recognizer.process_texts(texts)

# Parse the JSON string back into a Python list of dictionaries
results = json.loads(results_json)

# Iterate over the results and print them in a readable format
for result in results:
    print("\n---\n")
    print("Input Text:", result["input_text"])
    print("Predicted Topic:", result["predicted_topic_name"])
    print("Extracted Entities:")
    for entity in result["extracted_entities"]:
        print(f"  - Entity: {entity['entity_name']} (Score: {entity['score']}, Category: {entity['category']})")
    print("Recommendations:")
    for recommendation in result["recommendations"]:
        print(f"  - {recommendation['category']}: {recommendation['recommendation']}")
    print("\n---\n")
