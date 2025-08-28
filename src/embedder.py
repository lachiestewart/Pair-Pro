from typing import Any
import requests
import uuid

from models.embedded_point import EmbeddedPoint


class Embedder:

    def __init__(self, url: str, model: str):
        """
        Initialise the Embedder with the specified URL and model.
        """
        self.url = url
        self.model = model

    def embed_text(self, text: str) -> list[float]:
        """
        Get the embedding for the specified text.

        Args:
            text (str): The text to embed.

        Returns:
            list[float]: The embedding vector.
        """
        payload = {"model": self.model, "prompt": text}
        response = requests.post(self.url, json=payload)
        response.raise_for_status()
        return response.json().get("embedding")

    def embed_payload(self, payload: dict[str, str]) -> EmbeddedPoint:
        """
        Embed the specified payload.

        Args:
            payload (dict[str, str]): The payload to embed.

        Returns:
            EmbeddedPoint: The embedded point.
        """
        embeddings = {}
        for key, value in payload.items():
            embeddings[key] = self.embed_text(value)
        return EmbeddedPoint(
            id=str(uuid.uuid4()), payload=payload, embeddings=embeddings
        )
