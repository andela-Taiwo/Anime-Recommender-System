# 🎬 Anime Recommender System

An intelligent anime recommendation system powered by Retrieval Augmented Generation (RAG) that helps users discover anime based on their preferences. The system uses vector embeddings, semantic search, and large language models to provide personalized anime recommendations.

## ✨ Features

- **Semantic Search**: Uses vector embeddings to find anime based on user preferences
- **RAG Architecture**: Combines retrieval and generation for accurate recommendations
- **Interactive Web Interface**: Beautiful Streamlit-based UI for easy interaction
- **Intelligent Recommendations**: Provides 3 detailed anime recommendations with explanations
- **Persistent Vector Store**: Uses ChromaDB for efficient vector storage and retrieval
- **Customizable**: Easy to configure models, embeddings, and data sources

## 🏗️ Architecture

The system follows a RAG (Retrieval Augmented Generation) architecture:

1. **Data Processing**: Loads and processes anime data from CSV files
2. **Vector Store**: Creates embeddings using HuggingFace models and stores them in ChromaDB
3. **Retrieval**: Uses semantic search to find relevant anime based on user queries
4. **Generation**: Uses Groq's LLM (Llama 3.3 70B) to generate personalized recommendations

## 🛠️ Technology Stack

- **LangChain**: Framework for building LLM applications
- **ChromaDB**: Vector database for storing embeddings
- **HuggingFace Embeddings**: `all-MiniLM-L6-v2` for text embeddings
- **Groq API**: Fast inference with Llama 3.3 70B model
- **Streamlit**: Web interface for user interaction
- **Pandas**: Data processing and manipulation

## 📋 Prerequisites

- Python >= 3.13
- Groq API key ([Get one here](https://console.groq.com/))
- Anime dataset in CSV format (included: `data/anime_with_synopsis.csv`)

## 🚀 Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd Anime-Recommender
   ```

2. **Install dependencies** (using uv):
   ```bash
   uv sync
   ```
   
   Or using pip:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**:
   Create a `.env` file in the project root:
   ```env
   GROQ_API_KEY=your_groq_api_key_here
   ```

## ⚙️ Configuration

The system can be configured through `config/config.py`. Key settings:

- **Model**: Default is `llama-3.3-70b-versatile`
- **Embeddings**: `all-MiniLM-L6-v2` from HuggingFace
- **Vector Store**: ChromaDB with persistent storage in `chroma_db/`
- **Data Paths**: Configured in `pipeline/build_pipeline.py`

## 📖 Usage

### 1. Build the Vector Store

First, you need to build the vector store from your anime data:

```bash
python pipeline/build_pipeline.py
```

This will:
- Load anime data from `data/anime_with_synopsis.csv`
- Process and combine anime information (Title, Synopsis, Genres)
- Create embeddings and build the vector store
- Save the vector store to `chroma_db/`

### 2. Run the Streamlit App

Launch the web interface:

```bash
streamlit run app/app.py
```

The app will open in your browser where you can:
- Enter your anime preferences (e.g., "Action, Adventure, Fantasy")
- Get personalized recommendations with detailed explanations

### 3. Use the Pipeline Programmatically

```python
from pipeline.pipeline import AnimeRecommendationPipeline

# Initialize the pipeline
pipeline = AnimeRecommendationPipeline(persist_directory="chroma_db")

# Get recommendations
question = "I want anime with action and adventure"
recommendations = pipeline.recommend_anime(question)
print(recommendations)
```

## 📁 Project Structure

```
Anime-Recommender/
├── app/
│   ├── __init__.py
│   └── app.py                 # Streamlit web application
├── config/
│   ├── __init__.py
│   └── config.py              # Configuration settings
├── data/
│   └── anime_with_synopsis.csv # Anime dataset
├── pipeline/
│   ├── __init__.py
│   ├── build_pipeline.py      # Script to build vector store
│   └── pipeline.py            # Main recommendation pipeline
├── src/
│   ├── __init__.py
│   ├── data_loader.py         # Data loading and processing
│   ├── vector_store_loader.py # Vector store management
│   ├── recommender.py         # Recommendation engine
│   └── prompt_template.py    # LLM prompt templates
├── utils/
│   ├── __init__.py
│   ├── logger.py              # Logging utilities
│   └── custom_exception.py    # Custom exception classes
├── chroma_db/                 # Vector store (created after build)
├── logs/                      # Application logs
├── .env                       # Environment variables (create this)
├── pyproject.toml             # Project dependencies
├── requirements.txt           # Python dependencies
└── README.md                  # This file
```

## 🔧 Components

### `AnimeDataLoader`
- Loads anime data from CSV files
- Validates required columns (Name, Genres, sypnopsis)
- Combines anime information into a single text field
- Saves processed data for vectorization

### `VectorStoreLoader`
- Creates embeddings using HuggingFace models
- Builds and persists vector store in ChromaDB
- Loads existing vector stores for retrieval

### `AnimeRecommender`
- Implements RetrievalQA chain using LangChain
- Uses Groq LLM for generating recommendations
- Retrieves relevant context from vector store
- Generates personalized anime recommendations

### `AnimeRecommendationPipeline`
- Main pipeline class that orchestrates the recommendation process
- Combines vector store loading and recommendation generation
- Provides a simple interface for getting recommendations

## 📝 Data Format

The CSV file should contain the following columns:
- `Name`: Anime title
- `Genres`: Comma-separated genres
- `sypnopsis`: Anime synopsis/description

## 🐛 Troubleshooting

### ModuleNotFoundError
If you encounter import errors, ensure you're running scripts from the project root directory.

### Vector Store Not Found
Run `python pipeline/build_pipeline.py` first to create the vector store.

### API Key Issues
Make sure your `.env` file contains a valid `GROQ_API_KEY`.

### Missing Dependencies
Install all dependencies using:
```bash
uv sync
# or
pip install -r requirements.txt
```

## 📄 License

MIT

## 👤 Author

Taiwo Sokunbi

## 🙏 Acknowledgments

- LangChain for the RAG framework
- Groq for fast LLM inference
- HuggingFace for embeddings
- ChromaDB for vector storage

