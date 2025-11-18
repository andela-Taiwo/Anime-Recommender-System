import os
from dotenv import load_dotenv

load_dotenv()
MODEL_NAME = "llama-3.3-70b-versatile"
MODEL_URL = "https://api.groq.com/models/mistral-large-latest"
MODEL_API_KEY = os.getenv("GROQ_API_KEY")
MODEL_API_URL = "https://api.groq.com/models/mistral-large-latest"
GROQ_API_KEY = os.getenv("GROQ_API_KEY")


class Configuration:
    def __init__(self):
        self.groq_api_key = os.getenv("GROQ_API_KEY")
        self.chroma_api_key = os.getenv("CHROMA_API_KEY")
        self.chroma_url = os.getenv("CHROMA_URL")
        self.chroma_collection_name = os.getenv("CHROMA_COLLECTION_NAME")
        self.chroma_dimension = os.getenv("CHROMA_DIMENSION")
        self.chroma_distance_metric = os.getenv("CHROMA_DISTANCE_METRIC")
        self.chroma_metadata_fields = os.getenv("CHROMA_METADATA_FIELDS")
