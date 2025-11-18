# Agentic AI Bootcamp

A comprehensive learning repository covering the fundamentals and advanced concepts of building agentic AI applications using LangChain, LangGraph, and related technologies.

## Overview

This repository contains hands-on tutorials, examples, and projects focused on building intelligent, autonomous AI agents. The materials cover everything from basic data ingestion to complex graph-based workflows and deployable AI applications.

## Table of Contents

- [Features](#features)
- [Repository Structure](#repository-structure)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Getting Started](#getting-started)
- [Modules](#modules)
- [Technologies Used](#technologies-used)
- [Contributing](#contributing)
- [License](#license)

## Features

- **Comprehensive Learning Path**: From basics to advanced agentic AI concepts
- **Hands-on Notebooks**: Interactive Jupyter notebooks with practical examples
- **Real-world Applications**: Build chatbots, document processing systems, and intelligent agents
- **Modern Tech Stack**: LangChain, LangGraph, OpenAI, Hugging Face, and more
- **Production-Ready**: Includes deployment examples with LangServe and FastAPI

## Repository Structure

```
Agentic-AI-BootCamp/
├── LangChain/
│   ├── DataIngestion/        # Loading data from various sources
│   ├── Splitting/             # Text splitting strategies
│   ├── VectorEmbeddings/      # OpenAI and Hugging Face embeddings
│   └── VectorDB/              # Vector database implementations (FAISS, ChromaDB)
├── LCEL/
│   └── simpleLcelApp.ipynb    # LangChain Expression Language basics
├── LangChainProjects/
│   ├── introduction.ipynb     # Project introduction and setup
│   └── simple_project.ipynb   # Basic LangChain project implementation
├── LangGraph/
│   ├── 1_basic_graph.ipynb    # Building simple workflows
│   ├── 2_chatbot.ipynb        # Conversational agents
│   ├── 3_state_schema.ipynb   # State management
│   ├── 4_chains.ipynb         # Sequential processing chains
│   └── 5_routers.ipynb        # Conditional routing logic
├── LangServe/
│   └── serve.py               # API deployment with LangServe
└── requirements.txt           # Python dependencies
```

## Prerequisites

- Python 3.10 or higher
- Basic understanding of Python programming
- Familiarity with machine learning concepts (recommended)
- API keys for:
  - OpenAI (for GPT models)
  - Hugging Face (for open-source models)
  - Groq (optional, for alternative LLM provider)

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/Agentic-AI-BootCamp.git
   cd Agentic-AI-BootCamp
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**

   Create a `.env` file in the root directory:
   ```env
   OPENAI_API_KEY=your_openai_api_key
   HUGGINGFACE_API_KEY=your_huggingface_api_key
   GROQ_API_KEY=your_groq_api_key  # Optional
   ```

## Getting Started

1. **Start with LangChain basics**

   Navigate to the `LangChain/DataIngestion/` directory and explore data loading techniques:
   ```bash
   jupyter notebook LangChain/DataIngestion/data_ingestion.ipynb
   ```

2. **Learn about text processing**

   Explore different text splitting strategies in `LangChain/Splitting/`

3. **Understand embeddings and vector databases**

   Work through the notebooks in `LangChain/VectorEmbeddings/` and `LangChain/VectorDB/`

4. **Build your first agent with LangGraph**

   Follow the progression in the `LangGraph/` directory from basic graphs to advanced routers

5. **Deploy your application**

   Learn to serve your LangChain applications using the examples in `LangServe/`

## Modules

### LangChain

**Data Ingestion**
- Text file loading
- PDF document processing (PyPDF, PyMuPDF)
- Web scraping with BeautifulSoup
- Academic paper loading (arXiv)
- Wikipedia article retrieval

**Text Splitting**
- Character-based text splitting
- Recursive character text splitting
- Web-based content splitting

**Vector Embeddings**
- OpenAI embeddings (text-embedding models)
- Hugging Face embeddings (open-source alternatives)

**Vector Databases**
- FAISS (Facebook AI Similarity Search)
- ChromaDB (persistent vector storage)

### LCEL (LangChain Expression Language)

- Simple LCEL application structure
- Chain composition
- Parallel and sequential execution

### LangGraph

1. **Basic Graphs**: Fundamental workflow construction
2. **Chatbots**: Building conversational agents with state
3. **State Schema**: Managing complex application state
4. **Chains**: Sequential processing pipelines
5. **Routers**: Conditional logic and dynamic workflows

### LangServe

- FastAPI integration
- RESTful API endpoints
- Server-sent events (SSE) for streaming
- Production deployment patterns

## Technologies Used

- **LangChain**: Framework for developing LLM-powered applications
- **LangGraph**: Library for building stateful, multi-actor applications
- **LangServe**: Tool for deploying LangChain applications as REST APIs
- **OpenAI**: GPT models and embeddings
- **Hugging Face**: Open-source models and embeddings
- **Groq**: Alternative LLM provider for high-performance inference
- **Vector Databases**: FAISS, ChromaDB
- **Web Frameworks**: FastAPI, Uvicorn
- **Data Processing**: BeautifulSoup, PyPDF, PyMuPDF, Wikipedia API

## Key Dependencies

```
langchain
langchain-community
langchain-openai
langchain-huggingface
langchain-groq
langgraph
langserve
faiss-cpu
chromadb
sentence-transformers
fastapi
uvicorn
```

See `requirements.txt` for the complete list.

## Learning Path

1. **Week 1-2**: LangChain fundamentals (data loading, splitting, embeddings)
2. **Week 3**: Vector databases and retrieval
3. **Week 4**: LCEL and chain composition
4. **Week 5-6**: LangGraph and agentic workflows
5. **Week 7**: Deployment with LangServe

## Best Practices

- Always use environment variables for API keys
- Start with simple examples before moving to complex workflows
- Experiment with different embedding models and vector databases
- Monitor token usage and costs when using paid APIs
- Test thoroughly before deploying to production

## Troubleshooting

**Common Issues:**

- **Import errors**: Ensure all dependencies are installed: `pip install -r requirements.txt`
- **API key errors**: Verify your `.env` file is properly configured
- **Memory issues**: Use batch processing for large documents
- **Rate limits**: Implement retry logic and respect API rate limits

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- LangChain team for the excellent framework and documentation
- OpenAI and Hugging Face for providing powerful AI models
- The open-source community for continuous support and contributions

## Contact

For questions or feedback, please open an issue in this repository.

---

**Happy Learning!** Build amazing agentic AI applications!
