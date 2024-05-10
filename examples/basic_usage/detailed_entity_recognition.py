from entity_recognition_lib import EntityRecognizer

# Create an instance of the recognizer
recognizer = EntityRecognizer()

# Example text
text = "I need an Express.js Mongo database backend"

# Process text
results = recognizer.process_texts([text])

# Print the structured result
print(results)
