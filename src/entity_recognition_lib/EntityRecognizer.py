import json
import asyncio
from entity_recognition_lib.functions.entity_extraction import extract_tech_entities, initialize_matcher_with_patterns
from entity_recognition_lib.functions.recommendation_generation import dynamic_score_entities, recommend_technologies
from entity_recognition_lib.functions.topic_classification import classify_text
from entity_recognition_lib.models import load_bertopic_model
from entity_recognition_lib.utils import load_json_file


class EntityRecognizer:
    def __init__(self):
        self.tech_entities = load_json_file("tech_entities.json")
        self.matcher = initialize_matcher_with_patterns(self.tech_entities)
        self.topic_model = asyncio.run(load_bertopic_model("MaartenGr/BERTopic_Wikipedia"))
        self.topic_info = self.topic_model.get_topic_info()
        self.topic_name_mapping = dict(zip(self.topic_info["Topic"], self.topic_info["Name"]))

    def process_text(self, text):
        extracted_entities = extract_tech_entities(text, self.tech_entities, self.matcher)
        topic_name, topic_keywords = classify_text(text, self.topic_model, self.topic_name_mapping)
        sorted_entities = dynamic_score_entities(extracted_entities, topic_keywords, text, self.tech_entities)
        recommendations = recommend_technologies(sorted_entities)

        return {
            "input_text": text,
            "predicted_topic_name": topic_name,
            "extracted_entities": sorted_entities,
            "recommendations": recommendations
        }

    def process_texts(self, texts):
        results = []
        for text in texts:
            result = self.process_text(text)
            results.append(result)
        return json.dumps(results, indent=4)  # Serialize the list of results to a JSON formatted string with indentation
