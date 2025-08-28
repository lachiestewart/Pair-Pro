from qdrant_client import QdrantClient
from qdrant_client.http.models import PointStruct, VectorParams

from models.embedded_point import EmbeddedPoint


class Qdrant:

    def __init__(self, url: str):
        self.client = QdrantClient(url=url)

    def create_collection(self, collection_name: str, config: dict[str, VectorParams]):
        """
        Create or recreate a Qdrant collection with the specified configuration.

        Args:
            collection_name (str): The name of the collection to create.
            config (dict[str, VectorParams]): The configuration for the collection.
        """
        self.client.recreate_collection(
            collection_name=collection_name,
            vectors_config=config,
        )

    def store_embedded_point(self, collection_name: str, embedded_point: EmbeddedPoint):
        """
        Store an embedded point in the specified Qdrant collection with named vectors.

        Args:
            collection_name (str): The name of the collection to store the embedded point in.
            embedded_point (EmbeddedPoint): The embedded point to store.
        """
        point = PointStruct(
            id=embedded_point.id,
            vector=embedded_point.embeddings,
            payload=embedded_point.payload,
        )

        self.client.upsert(
            collection_name=collection_name,
            points=[point],
        )

    def delete_collection(self, collection_name: str):
        """
        Delete a Qdrant collection.

        Args:
            collection_name (str): The name of the collection to delete.
        """
        self.client.delete_collection(collection_name=collection_name)

    def get_similar_points(
        self,
        collection_name: str,
        vector_name: str,
        embedding: list[float],
        top_k: int,
    ):
        """
        Retrieve similar points from a Qdrant collection based on the provided named vector.

        Args:
            collection_name (str): The name of the collection to search in.
            vector_name (str): The name of the vector to use for similarity search.
            embedding (list[float]): The embedding vector to use for similarity search.
            top_k (int): The number of similar points to retrieve.

        Returns:
            List[PointStruct]: A list of similar points.
        """
        search_result = self.client.query_points(
            collection_name=collection_name,
            query_vector={vector_name: embedding},
            limit=top_k,
        )
        return search_result
