import asyncio
import json
from importlib import resources  

from requests import JSONDecodeError
import torch
import torch.nn.functional as F
from scipy.spatial.distance import cosine

from entity_recognition_lib.models import load_embeddings_model

tokenizer, model = asyncio.run(load_embeddings_model())

def load_json_file(file_name):
    """
    Load a JSON file from the installed package resources.

    Args:
        file_name (str): The filename of the JSON file to load from the 'data' directory within the package.

    Returns:
        dict: The contents of the JSON file as a dictionary.

    Raises:
        FileNotFoundError: If the file does not exist within the package resources.
    """
    package_path = 'entity_recognition_lib.data'  # Define the package path to the resources

    try:
      # Open the resource file within the context manager
      with resources.files(package_path).joinpath(file_name).open() as file:
        return json.load(file)
    except FileNotFoundError:
      raise FileNotFoundError(f"File not found: {file_name} in package resources.")
    except JSONDecodeError as e:
      raise JSONDecodeError(f"An error occurred while loading {file_name}: {str(e)}")


def mean_pooling(model_output, attention_mask):
    """
    Apply mean pooling to get the sentence embedding

    Parameters:
        model_output: The model's output.
        attention_mask: The attention mask to exclude padding tokens from the averaging process.

    Returns:
        torch.Tensor: The sentence embedding.
    """
    token_embeddings = model_output[0]  # First element of model_output contains all token embeddings
    input_mask_expanded = attention_mask.unsqueeze(-1).expand(token_embeddings.size()).float()
    sum_embeddings = torch.sum(token_embeddings * input_mask_expanded, 1)
    sum_mask = torch.clamp(input_mask_expanded.sum(1), min=1e-9)
    return sum_embeddings / sum_mask


def get_embedding(text):
    """
    Get the embedding representation of the given text.

    Parameters:
        text (str): The input text to be embedded.

    Returns:
        torch.Tensor: The embedding representation of the text.
    """


    # Tokenize the input text and prepare it for the model
    inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True, max_length=512)
    # Generate the embeddings by passing the inputs to the model
    with torch.no_grad():  # Disable gradient computation
        outputs = model(**inputs)
    # Extract the embeddings from the model's output, which is the mean of the last hidden state
    embeddings = mean_pooling(outputs, inputs["attention_mask"])

    # Normalize the embeddings
    normalized_embeddings = F.normalize(embeddings, p=2, dim=1)

    # Return the embeddings after removing the batch dimension
    return normalized_embeddings.squeeze()


def cosine_similarity(a, b):
    """
    Calculates the cosine similarity between two vectors.

    Parameters:
        a (numpy.ndarray): The first vector.
        b (numpy.ndarray): The second vector.

    Returns:
        float: The cosine similarity between the two vectors.
    """
    # Calculate the cosine similarity, which is 1 minus the cosine distance
    return 1 - cosine(a.detach().numpy(), b.detach().numpy())
