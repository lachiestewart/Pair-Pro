from qdrant_client.http.models import VectorParams, Distance


VECTOR_SIZE = 768

EMBEDDING_URL = "http://localhost:11434/api/embeddings"
EMBEDDING_MODEL = "nomic-embed-text"

QDRANT_URL = "http://localhost:6333"

MY_COLLECTION = {
    "NAME": "embeddings",
    "CONFIG": {
        "name": VectorParams(size=VECTOR_SIZE, distance=Distance.COSINE),
        "content": VectorParams(size=VECTOR_SIZE, distance=Distance.COSINE),
    },
}
