import spacy
from bertopic import BERTopic
from transformers import AutoModel, AutoTokenizer
from spacy.util import is_package


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
    Checks if the model 'en_core_web_sm' is installed and prompts for download if not.

    Returns:
        nlp (spacy.Language): The loaded spaCy model, or None if not found.
    """
    model_name = "en_core_web_sm"
    if not is_package(model_name):  # Check if model is downloaded
        print(f"The spaCy model {model_name} is not installed.")
        print("Please run the following command to install it:")
        print(f"python -m spacy download {model_name}")
        return None
    else:
        nlp = spacy.load(model_name)
        return nlp