# Entity-Recognition

The Entity-Recognition library utilizes `spaCy`, `BERTopic`, and `Transformers` to provide a robust technology entity recognition system capable of identifying technological entities within texts and suggesting relevant technologies using advanced NLP techniques.

## Table of Contents
- [Entity-Recognition](#entity-recognition)
  - [Table of Contents](#table-of-contents)
  - [Features](#features)
  - [Installation](#installation)
    - [Prerequisites](#prerequisites)
    - [Getting Started](#getting-started)
  - [Usage](#usage)
  - [Development](#development)
    - [Setting Up a Development Environment](#setting-up-a-development-environment)
  - [Testing](#testing)
  - [Contributing](#contributing)
  - [License](#license)

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
pip install entity-recognition-library
```

## Usage

Here’s how to use the Entity Recognition library in your Python scripts:

```python
from entity_recognition import EntityRecognizer

# Create an instance of the recognizer
recognizer = EntityRecognizer()

# Example texts
texts = ["I need an Express.js Mongo database backend", "and a React TypeScript frontend for my project"]

# Process texts
results = recognizer.process_texts(texts)
print(results)
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
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. **Install Dependencies**:
    ```
    pip install -r requirements/dev.txt
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


