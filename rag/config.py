"""
config.py
---
Central configuration for the PersonalKB RAG pipeline.
Override any value here to tune the system.
"""

import os

# ChromaDB
CHROMA_DIR: str = os.environ.get("CHROMA_DIR", "./chroma_store")
COLLECTION_NAME: str = "personalkb"

# Chunking
CHUNK_SIZE: int = 500        # characters per chunk 
CHUNK_OVERLAP: int = 50      # overlap between consecutive chunks

# Retreival
TOP_K: int = 6               # number of chunks to retrieve per query

# LLM
CHAT_MODEL: str = "gpt-4o-mini"   

# Memory
MAX_HISTORY_TURNS: int = 10  # how many prior Q&A turns to include in context