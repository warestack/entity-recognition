# Entity-Recognition

The Entity-Recognition library utilizes `spaCy`, `BERTopic`, and `Transformers` to provide a robust technology entity recognition system capable of identifying technological entities within texts and suggesting relevant technologies using advanced NLP techniques.

The library automatically downloads the required spaCy model if not installed, making it easy to get started.


## Features

- **Technology Entity Extraction**: Automatically extract technology-related terms and tools from texts.
- **Recommendation System**: Provides context-based technology recommendations.
- **BERTopic Integration**: Leverages topic modeling to enhance the relevance of recommendations.
- **spaCy Matchers**: Utilizes custom NLP patterns for precise entity recognition.

## Installation

### Prerequisites

- Python 3.6+
- pip

### Getting Started

Install the library directly from PyPI:

```bash
pip install entity-recognition-lib
```

The required spaCy model (`en_core_web_sm`) will be automatically downloaded and installed if not already present on your system.



Usage
-----

Here's how to use the Entity Recognition library in your Python scripts:

```python
from entity_recognition_lib import EntityRecognizer

# Create an instance of the recognizer
recognizer = EntityRecognizer()

# Example texts
texts = ["I need an Express.js Mongo database backend"]

# Process texts
results = recognizer.process_texts(texts)
print(results)
```
Expected output:

```json
[
    {
        "input_text": "I need an Express.js Mongo database backend",
        "predicted_topic_name": "575_databases_database_tables_schema",
        "extracted_entities": [
            {
                "entity_name": "Express.js",
                "score": 1.0,
                "category": "Backend Web Frameworks"
            },
            {
                "entity_name": "MongoDB",
                "score": 1.0,
                "category": "Databases"
            }
        ],
        "recommendations": [
            {
                "category": "Backend Web Frameworks",
                "recommendation": "Express.js"
            },
            {
                "category": "Databases",
                "recommendation": "MongoDB"
            }
        ]
    }
]
```

## Development

### Setting Up a Development Environment

1. **Clone the repository**:
   ```
   git clone https://github.com/cgoncalves94/entity-recognition.git
   cd entity-recognition
   ```
2. **Create and Activate a Virtual Environment**:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. **Install Dependencies**:
    ```
    pip install -r requirements.txt
    ```


## Testing

Run tests to ensure the setup is correct:

```
pytest
```

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository on GitHub.
2. Clone the forked repository to your machine.
3. Create a new branch for your changes.
4. Make changes and test.
5. Submit a pull request with a comprehensive description of changes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


