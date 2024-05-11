import json

from entity_recognition_lib import EntityRecognizer

# Create an instance of the recognizer
recognizer = EntityRecognizer()

# Example texts with varied technological contexts
texts = [
    "Exploring data streaming with Apache Kafka and stream processing.",
    "Building web applications using Django and integrating with PostgreSQL.",
    "Advanced machine learning techniques with TensorFlow and PyTorch."
]

# Process texts and extract entities
results = recognizer.process_texts(texts)

# Deserialize the JSON string into a Python object
results = json.loads(results)

# Proceed with analyzing results
category_counts = {}
try:
    for result in results:
        for entity in result['extracted_entities']:
            if entity['category'] in category_counts:
                category_counts[entity['category']] += 1
            else:
                category_counts[entity['category']] = 1

    # Print the category counts
    print("Category Counts:")
    print(json.dumps(category_counts, indent=4))
except TypeError as e:
    print(f"Error processing results: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
