import pandas as pd
from utils.logger import get_logger
from utils.custom_exception import CustomException

logger = get_logger(__name__)


class AnimeDataLoader:
    def __init__(self, original_csv_path: str, processed_csv_path: str):
        self.original_csv_path = original_csv_path
        self.processed_csv_path = processed_csv_path

    def load_data_and_save_processed_csv(self):
        try:
            logger.info(f"Loading data from {self.original_csv_path}")
            df = pd.read_csv(
                self.original_csv_path, encoding="utf-8", on_bad_lines="skip"
            ).dropna()
            required_columns = {"Name", "Genres", "sypnopsis"}
            missing_columns = required_columns - set(df.columns)
            if missing_columns:
                raise CustomException(f"Missing columns: {missing_columns}")
            logger.info(f"Data loaded successfully from {self.original_csv_path}")

            df["combined_info"] = (
                "Title: "
                + df["Name"]
                + " Overview: "
                + df["sypnopsis"]
                + "Genres : "
                + df["Genres"]
            )
            df[["combined_info"]].to_csv(
                self.processed_csv_path, index=False, encoding="utf-8"
            )
            logger.info(f"Data saved successfully to {self.processed_csv_path}")
            logger.info(f"Data loaded successfully from {self.original_csv_path}")
            return self.processed_csv_path
        except Exception as e:
            logger.error(f"Error loading data from {self.original_csv_path}: {e}")
            raise CustomException(e) from e
