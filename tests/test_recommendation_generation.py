import pytest
from unittest.mock import patch
from entity_recognition_lib.functions.recommendation_generation import dynamic_score_entities, recommend_technologies

@pytest.fixture
def tech_entities_fixture():
    return {
        "MySQL": {"category": "Database", "description": "SQL database management system", "score": 1},
        "MongoDB": {"category": "Database", "description": "NoSQL database management system", "score": 0.9},
        "React": {"category": "Frontend", "description": "A JavaScript library for building user interfaces", "score": 0.8},
        "NodeJS": {"category": "Backend", "description": "JavaScript runtime built on Chrome's V8 JavaScript engine", "score": 0.7}
    }

# Test to ensure outputs are consistent with the same inputs
@patch('entity_recognition_lib.functions.recommendation_generation.get_embedding')
@patch('entity_recognition_lib.functions.recommendation_generation.cosine_similarity')
def test_dynamic_score_entities_consistency(mock_cosine_similarity, mock_get_embedding, tech_entities_fixture):
    mock_get_embedding.return_value = [0.5] * 100  # Mocking embedding as a 100-dimensional vector
    mock_cosine_similarity.return_value = 0.8      # Mocking cosine similarity to always return 0.8

    entities = [{"entity": "MySQL", "category": "Database"}, {"entity": "MongoDB", "category": "Database"}]
    topic_keywords = ["databases", "schemas", "tables"]
    user_input = "We are comparing MySQL and MongoDB to find the best database system based on performance and features."

    results_first_run = dynamic_score_entities(entities, topic_keywords, user_input, tech_entities_fixture)
    results_second_run = dynamic_score_entities(entities, topic_keywords, user_input, tech_entities_fixture)

    assert results_first_run == results_second_run, "Results should be consistent between runs"

# Test for behavior when no entities match the input
def test_dynamic_score_entities_no_match(tech_entities_fixture):
    entities = [{"entity": "PostgreSQL", "category": "Database"}]
    topic_keywords = ["performance", "scalability"]
    user_input = "Looking for a scalable and high-performance database system."

    results = dynamic_score_entities(entities, topic_keywords, user_input, tech_entities_fixture)
    assert len(results) == 1 and results[0]["category"] == "Uncategorized", "Unknown entities should be categorized as 'Uncategorized'"


# Test handling edge cases such as empty inputs
def test_dynamic_score_entities_empty_input(tech_entities_fixture):
    entities = []
    topic_keywords = []
    user_input = ""

    results = dynamic_score_entities(entities, topic_keywords, user_input, tech_entities_fixture)
    assert results == [], "Should handle empty inputs gracefully"

# Using Behavioral Testing
def test_dynamic_score_entities_behavioral(tech_entities_fixture):
    entities = [{"entity": "MySQL", "category": "Database"}, {"entity": "MongoDB", "category": "Database"}]
    topic_keywords = ["SQL", "NoSQL", "transactions"]
    user_input = "We need a SQL database that can handle complex transactions."

    sorted_entities = dynamic_score_entities(entities, topic_keywords, user_input, tech_entities_fixture)
    assert sorted_entities[0]["entity_name"] == "MySQL", "MySQL should be ranked higher for SQL related queries"
    assert sorted_entities[1]["entity_name"] == "MongoDB", "MongoDB should be ranked lower for SQL related queries"
