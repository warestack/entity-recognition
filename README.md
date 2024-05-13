# Entity Recognition Library

## Purpose

The Entity Recognition serves as a library for identifying technological entities within texts and suggesting relevant
 technologies using advanced NLP techniques.

## Installing the Library

Integrate our library into your project by installing it directly from [PyPI](https://pypi.org/project/entity-recognition-lib/#description):

```bash
pip install entity-recognition-lib
```

The required spaCy model (`en_core_web_sm`) will be automatically downloaded and installed if not already present on
 your system.

## Using the Library

Here's how to use the Entity Recognition library in your Python scripts:

```python
from entity_recognition_lib import EntityRecognizer

recognizer = EntityRecognizer()
texts = ["Your text here"]
results = recognizer.process_texts(texts)
print(results)
```

## Expected Output

The library processes text to identify and categorize technology entities, delivering structured output that includes
 identified entities and contextual recommendations.

Example output:

```json
[
  {
    "input_text": "Example text with technology entities",
    "predicted_topic_name": "topic_name",
    "extracted_entities": [
      {
        "entity_name": "entity_1",
        "score": 0.9,
        "category": "Category 1"
      },
      {
        "entity_name": "entity_2",
        "score": 0.8,
        "category": "Category 1"
      }
    ],
    "recommendations": [
      {
        "category": "Category 1",
        "recommendation": "entity_1"
      }
    ]
  }
]
```

For detailed usage examples and code snippets, please refer to the
 [examples directory](https://github.com/warestack/entity-recognition/blob/main/examples/EXAMPLES.md) in the repository.
The examples cover various scenarios, including:

- Basic usage of the library for entity recognition and recommendation generation
- Advanced features such as result analysis and visualization
- Integration samples with popular frameworks like Flask and Streamlit

We recommend exploring the examples to understand how to effectively utilize the Entity-Recognition library in your projects.

## Contributing

If you consider contributing to the Entity Recognition library, make sure to check out our
 [Contributing Guide](https://github.com/warestack/entity-recognition/blob/main/CONTRIBUTING.md) and our
  [Development Guide](https://github.com/warestack/entity-recognition/blob/main/DEVELOPMENT.md), for more information
   on how to run and test the project locally.
You are welcome to expand the technology entities corpus or add a new feature.

## License

This project is licensed under the MIT License - see the
 [LICENSE](https://github.com/warestack/entity-recognition/blob/main/LICENSE) file for details.
