import sys
from pathlib import Path

# Add project root to Python path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))
import streamlit as st
from pipeline.pipeline import AnimeRecommendationPipeline
from dotenv import load_dotenv

st.set_page_config(
    page_title="Anime Recommender", page_icon=":movie_camera:", layout="wide"
)

load_dotenv()


@st.cache_resource
def load_pipeline():
    return AnimeRecommendationPipeline()


pipeline = load_pipeline()

st.title("Anime Recommender System")

st.write(
    "This is a simple anime recommender that uses a pipeline to recommend anime based on the user's question."
)

query = st.text_input(
    "Enter your anime preferences eg. : Light Novel, Action, Adventure, etc."
)

if query:
    with st.spinner("Searching for anime..."):
        recommendation = pipeline.recommend_anime(query)
        st.markdown("### Recommendations")
        st.write(recommendation)
