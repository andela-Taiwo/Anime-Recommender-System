import sys
from pathlib import Path

# Add project root to Python path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from langchain_groq import ChatGroq
from langchain_classic.chains import RetrievalQA
from src.prompt_template import get_anime_prompt
from utils.logger import get_logger
from utils.custom_exception import CustomException
from langchain_community.vectorstores import Chroma

logger = get_logger(__name__)


class AnimeRecommender:
    def __init__(self, retriever: Chroma, api_key: str, model_name: str):
        self.llm = ChatGroq(api_key=api_key, model_name=model_name, temperature=0.0)
        self.retriever = retriever
        self.prompt = get_anime_prompt()
        self.qa_chain = RetrievalQA.from_chain_type(
            llm=self.llm,
            chain_type="stuff",
            retriever=self.retriever,
            return_source_documents=True,
            chain_type_kwargs={"prompt": self.prompt},
        )

    def get_recommendations(self, question: str) -> str:
        try:
            response = self.qa_chain.invoke({"query": question})
            return response["result"]
        except Exception as e:
            logger.error(f"Error getting recommendations: {e}")
            raise CustomException(e) from e
