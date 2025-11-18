import sys
from pathlib import Path

# Add project root to Python path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from src.vector_store_loader import VectorStoreLoader
from src.data_loader import AnimeDataLoader
from utils.logger import get_logger
from utils.custom_exception import CustomException

logger = get_logger(__name__)


def main():
    try:
        logger.info(f"Start Building pipeline")
        data_loader = AnimeDataLoader(
            original_csv_path="data/anime_with_synopsis.csv",
            processed_csv_path="data/anime_processed.csv",
        )
        processed_csv_path = data_loader.load_data_and_save_processed_csv()
        vector_store_loader = VectorStoreLoader(
            processed_csv_path=processed_csv_path, persist_directory="chroma_db"
        )
        vector_store_loader.build_and_save_vector_store()
        logger.info(f"Pipeline built successfully")
    except Exception as e:
        logger.error(f"Error building pipeline: {e}")
        raise CustomException(e) from e


if __name__ == "__main__":
    main()
