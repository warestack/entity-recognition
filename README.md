# Entity-Recognition

The Entity-Recognition project leverages FastAPI, spaCy, BERTopic, and Transformers to provide a robust technology entity recognition system. This application identifies technology-related entities within texts and suggests relevant technologies using NLP techniques.

## Table of Contents
- [Entity-Recognition](#entity-recognition)
  - [Table of Contents](#table-of-contents)
  - [Features](#features)
  - [Quick Start](#quick-start)
    - [Prerequisites](#prerequisites)
    - [Getting Started](#getting-started)
  - [API Usage](#api-usage)
    - [Process Texts Endpoint](#process-texts-endpoint)
  - [Development](#development)
    - [Local Setup](#local-setup)
  - [Testing](#testing)
  - [Configuration](#configuration)
  - [Contributing](#contributing)
  - [License](#license)

## Features

- **Technology Entity Extraction**: Extract technology terms and tools from texts.
- **Recommendation System**: Offer recommendations based on the context and the entities identified.
- **BERTopic Integration**: Utilize topic modeling to improve the relevance of recommendations.
- **spaCy Matchers**: Employ custom NLP patterns for precise entity recognition.
- **Docker Compatibility**: Easy deployment with Docker and Docker Compose.

## Quick Start

### Prerequisites

- Docker

### Getting Started

Clone the repository and navigate to the directory:

```bash
git clone https://github.com/cgoncalves94/entity-recognition.git
cd entity-recognition
```
Build and run the application using Docker:

```
docker-compose up --build
```
This command builds the Docker image and starts the service. The API will be available at http://localhost:16000/ by default.


## API Usage

### Process Texts Endpoint

- **URL**: `/nlp/process/`
- **Method**: `POST`
- **Content-Type**: `application/json`
- **Body**:

```json
{
  "texts": ["Your sample text here", "Another sample text"]
}
```
- **Successful Response:**:
```json
[
  {
    "input_text": "Your sample text here",
    "predicted_topic_name": "Technology",
    "extracted_entities": [
      {
        "entity_name": "Python",
        "score": 0.9,
        "category": "Programming Language"
      }
    ],
    "recommendations": [
      {
        "category": "Programming Language",
        "recommendation": "Python"
      }
    ]
  }
]
```

## Development

### Local Setup

Set up the project locally (without Docker) by following these steps:

1. **Create and Activate a Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
2. **Install Dependencies**:
    ```
    pip install -r requirements/dev.txt
    ```
3. **Run the Application**:
   ```
   uvicorn src.main:app --reload
   ```

## Testing

Run tests using Docker:

```
docker-compose exec app pytest
```

## Configuration

Environmental variables are used for configuration which can be set in a .env file:

- `MODEL_NAME`: Path to the BERTopic model.
- `CORPUS_DIR`: Directory containing tech_entities.json.

Example `.env` file:


```
MODEL_NAME=model/bertopic_model
CORPUS_DIR=data/tech_entities.json
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


