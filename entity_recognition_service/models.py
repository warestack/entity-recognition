import spacy

from bertopic import BERTopic
from transformers import AutoModel, AutoTokenizer
from spacy.util import is_package
from spacy.cli import download


async def load_embeddings_model():
    """
    Loads the embeddings model for sentence transformation.

    Returns:
      tokenizer (AutoTokenizer): The tokenizer for the embeddings model.
      model (AutoModel): The embeddings model.
    """
    tokenizer = AutoTokenizer.from_pretrained("sentence-transformers/all-MiniLM-L6-v2")
    model = AutoModel.from_pretrained("sentence-transformers/all-MiniLM-L6-v2")
    return tokenizer, model


async def load_bertopic_model(model_object_name):
    """
    Load a BERTopic model from a given object name.

    Parameters:
        model_object_name (str): The name of the model object to load.

    Returns:
        BERTopic: The loaded BERTopic model.
    """

    topic_model = BERTopic.load(model_object_name)

    return topic_model


def load_spacy_model():
    """
    Loads the spaCy model for the English language.
    Checks if the model 'en_core_web_sm' is installed and automatically downloads it if not.

    Returns:
        nlp (spacy.Language): The loaded spaCy model, or None if not found.
    """
    model_name = "en_core_web_sm"
    if not is_package(model_name):  # Check if model is downloaded
        print(f"The spaCy model {model_name} is not installed. Downloading now...")
        download(model_name)
        print(f"spaCy model {model_name} downloaded.")

    # After ensuring the model is downloaded, load it
    try:
        nlp = spacy.load(model_name)
        return nlp
    except Exception as e:
        print(f"Failed to load spaCy model {model_name}: {str(e)}")
        return None