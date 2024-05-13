# Running the Entity Recognition Locally

## Setting Up the Project Locally

### Prerequisites

- Python 3.11 or newer
- pip and poetry

### Installation

1. **Clone the Project**

   First, clone the repository to your local machine:

   ```bash
   git clone https://github.com/warestack/entity-recognition.git
   cd entity-recognition
    ```

2. **Set Up Your Virtual Environment**

   Use pip to install a virtual environment and set up dependencies:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   pip install -r requirements.txt
   ```

   This command installs all necessary packages listed in the requirements.txt file within a virtual environment.

### Running Pre-commit Hooks Locally

To ensure code quality and consistency, it's recommended to set up and run pre-commit hooks locally before pushing your
changes:

- **Install Pre-commit**

   First, ensure that `pre-commit` is installed within your virtual environment:

   ```bash
   pip install pre-commit
   ```

- **Install Git Hooks**

   To set up the Git hooks in your local repository, run:

   ```bash
   pre-commit install
   ```

   This will ensure that the pre-commit hooks are run on every commit.

- **Manually Running Pre-commit Hooks**

   If you want to manually run the pre-commit hooks on all files (useful for initial setup or to check files without
   committing):

   ```bash
   pre-commit run --all-files
   ```

   This command will run all configured hooks against all files in the repository.

## Running the Project

### Using the Examples Directory

The examples directory contains sample scripts and applications that demonstrate how to use the library code
effectively. These examples are particularly useful for testing local changes to the library:

- Navigate to the `examples` directory.
- Run an example script to see how the library performs with your changes:

This approach helps ensure that any modifications you make to the library are reflected and can be tested immediately
through practical use cases.

## Unit Tests

Run the unit tests included in the `tests` directory with the following command:

```bash
pytest
```

Or, to run a specific unit test file:

```bash
pytest tests/test_specific_feature.py
```

## Bumping and Publishing Versions

This project utilizes GitHub Actions for automated version management and publishing. When a pull request is merged
into the `main` branch, the following happens automatically:

- **Version Bumping**: A new version number is generated based on the contents of the PR, adhering to semantic
   versioning.
- **Package Building**: The project is built using `poetry`, ensuring all package dependencies are properly
   encapsulated.
- **Publishing**: The newly built version is published to PyPI automatically, making it immediately available for use.
