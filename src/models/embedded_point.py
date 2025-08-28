from dataclasses import dataclass
from typing import Any


@dataclass
class EmbeddedPoint:
    id: str
    payload: dict[str, Any]
    embeddings: dict[str, list[float]]
