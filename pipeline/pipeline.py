import sys
from pathlib import Path

# Add project root to Python path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from src.vector_store_loader import VectorStoreLoader
from src.recommender import AnimeRecommender
from utils.logger import get_logger
from utils.custom_exception import CustomException
from config.config import GROQ_API_KEY, MODEL_NAME

logger = get_logger(__name__)


class AnimeRecommendationPipeline:
    def __init__(self, persist_directory: str = "chroma_db"):
        try:
            logger.info(
                f"Initializing AnimeRecommendationPipeline with persist_directory: {persist_directory}"
            )
            self.vector_store_loader = VectorStoreLoader(
                processed_csv_path="", persist_directory=persist_directory
            )
            retriever = self.vector_store_loader.load_vector_store().as_retriever()
            self.recommender = AnimeRecommender(
                retriever=retriever, api_key=GROQ_API_KEY, model_name=MODEL_NAME
            )
            logger.info(f"AnimeRecommendationPipeline initialized successfully")
        except Exception as e:
            logger.error(f"Error initializing AnimeRecommendationPipeline: {e}")
            raise CustomException(e) from e

    def recommend_anime(self, question: str) -> str:
        try:
            logger.info(f"Recommending anime for question: {question}")
            return self.recommender.get_recommendations(question)
        except Exception as e:
            logger.error(f"Error recommending anime: {e}")
            raise CustomException(e) from e
