import pytest

from entity_recognition_lib.functions.entity_extraction import (
    extract_tech_entities,
    initialize_matcher_with_patterns,
)
from entity_recognition_lib.utils import load_json_file

# Adjusting the load_tech_entities function if load_json_file is not an async function
def load_tech_entities():
    return load_json_file("tech_entities.json")

@pytest.fixture(scope="session")
def tech_entities():
    """Fixture to load the technology entities from the JSON file."""
    return load_tech_entities()

@pytest.fixture(scope="session")
def matcher(tech_entities):
    """Fixture to initialize the Matcher with the patterns."""
    return initialize_matcher_with_patterns(tech_entities)

@pytest.mark.asyncio
async def test_load_tech_entities(tech_entities):
    """Tests that the tech_entities fixture correctly loads the technology entities."""
    assert tech_entities is not None
    assert "MySQL" in tech_entities

def test_initialize_matcher_with_patterns(matcher):
    """Tests that the matcher fixture correctly initializes the Matcher."""
    assert matcher is not None

@pytest.mark.asyncio
async def test_extract_tech_entities_single_entity(matcher, tech_entities):
    """Tests that the extract_tech_entities() function correctly extracts a single entity."""
    text = "I want to use MySQL for my database."
    entities = extract_tech_entities(text, tech_entities, matcher)
    assert len(entities) == 1
    assert entities[0]["entity"] == "MySQL"

@pytest.mark.asyncio
async def test_extract_tech_entities_multiple_entities(matcher, tech_entities):
    """Tests that the extract_tech_entities() function correctly extracts multiple entities."""
    text = "In comparing database management systems, we're evaluating the performance and features of MySQL versus MongoDB to determine the best fit."
    entities = extract_tech_entities(text, tech_entities, matcher)
    assert len(entities) == 2
    assert entities[0]["entity"] == "MySQL"
    assert entities[1]["entity"] == "MongoDB"

@pytest.mark.asyncio
async def test_extract_tech_entities_different_types(matcher, tech_entities):
    """Tests extraction of entities with different types."""
    text = "I'm building a web app with React and NodeJS, using MongoDB for the database."
    entities = extract_tech_entities(text, tech_entities, matcher)
    assert len(entities) == 3
    assert entities[0]["type"] == "JavaScript Library"  # React
    assert entities[1]["type"] == "Runtime Environment"  # NodeJS
    assert entities[2]["type"] == "NoSQL"  # MongoDB

@pytest.mark.asyncio
async def test_extract_tech_entities_fuzzy_matching(matcher, tech_entities):
    """Tests fuzzy matching capabilities."""
    text = "I'm considering using Google Croud for my project."
    entities = extract_tech_entities(text, tech_entities, matcher)
    assert len(entities) == 1
    assert entities[0]["entity"] == "GoogleCloud"
