import json
import time

from entity_recognition_lib import EntityRecognizer


def process_text(text):
    start_time = time.time()
    # Create an instance of the recognizer
    recognizer = EntityRecognizer()

    # Process the text
    results_json = recognizer.process_texts([text])

    # Parse the JSON string back into a Python list of dictionaries
    results = json.loads(results_json)

    # Iterate over the results and print them in a readable format
    for result in results:
        print("Input Text:", result["input_text"])
        print("Predicted Topic:", result["predicted_topic_name"])
        print("Extracted Entities:")
        for entity in result["extracted_entities"]:
            print(f"  - Entity: {entity['entity_name']} (Score: {entity['score']}, Category: {entity['category']})")
        print("Recommendations:")
        for recommendation in result["recommendations"]:
            print(f"  - {recommendation['category']}: {recommendation['recommendation']}")
        print("\n---\n")

    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"\nExecution time: {elapsed_time} seconds")


if __name__ == "__main__":
    text = "I need an Express.js Mongo database backend"
    process_text(text)
