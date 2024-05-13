import streamlit as st
from entity_recognition_lib import EntityRecognizer

recognizer = EntityRecognizer()

st.title("Technology Entity Recognition")

input_text = st.text_area(
    "Enter text",
    "I need a database system good for transactions for my project, was thinking between mysql or mongodb.",
)

if st.button("Recognize"):
    result = recognizer.process_text(input_text)
    st.write("Recognized Entities:")
    for entity in result["extracted_entities"]:
        st.write(f"- {entity['entity_name']} ({entity['category']})")
    st.write("Recommendations:")
    for recommendation in result["recommendations"]:
        st.write(f"- {recommendation['recommendation']} ({recommendation['category']})")
