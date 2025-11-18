from langchain_community.vectorstores import Chroma
from config.config import Configuration
from utils.logger import get_logger
from utils.custom_exception import CustomException
from langchain_community.document_loaders import CSVLoader
from langchain_huggingface import HuggingFaceEmbeddings
from sentence_transformers import SentenceTransformer
from dotenv import load_dotenv
from langchain_text_splitters import CharacterTextSplitter

load_dotenv()


logger = get_logger(__name__)


class VectorStoreLoader:
    def __init__(self, processed_csv_path: str, persist_directory: str = "chroma_db"):
        self.processed_csv_path = processed_csv_path
        self.persist_directory = persist_directory
        self.embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
        self.vector_store = self.load_vector_store()

    def build_and_save_vector_store(self):
        try:
            logger.info(f"Loading vector store from {self.processed_csv_path}")
            loader = CSVLoader(file_path=self.processed_csv_path, encoding="utf-8")
            documents = loader.load()
            splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
            texts = splitter.split_documents(documents)
            logger.info(f"Documents loaded successfully from {self.processed_csv_path}")
            db = Chroma.from_documents(
                texts, self.embeddings, persist_directory=self.persist_directory
            )
            db.persist()
            logger.info(f"Vector store saved successfully to {self.persist_directory}")
            # return db
        except Exception as e:
            logger.error(
                f"Error loading vector store from {self.processed_csv_path}: {e}"
            )
            raise CustomException(e) from e

    def load_vector_store(self):
        try:
            logger.info(f"Loading vector store from {self.persist_directory}")
            db = Chroma(
                persist_directory=self.persist_directory,
                embedding_function=self.embeddings,
            )
            logger.info(
                f"Vector store loaded successfully from {self.persist_directory}"
            )
            return db
        except Exception as e:
            logger.error(
                f"Error loading vector store from {self.persist_directory}: {e}"
            )
            raise CustomException(e) from e
