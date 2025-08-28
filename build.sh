#!/bin/zsh
# Build script for Pair Pro

set -e

# Create Docker volumes if they don't exist
docker volume inspect ollama_data > /dev/null 2>&1 || docker volume create ollama_data
docker volume inspect qdrant_data > /dev/null 2>&1 || docker volume create qdrant_data

echo "Starting containers with docker compose..."
docker compose up -d

echo "Waiting for Ollama to be ready..."
# Wait for Ollama API to be available
until curl -s http://localhost:11434/api/tags > /dev/null; do
  sleep 2
done

echo "Checking if nomic-embed-text model is present in Ollama..."
if ! curl -s http://localhost:11434/api/tags | grep -q 'nomic-embed-text'; then
  echo "Pulling nomic-embed-text model into Ollama..."
  docker exec ollama ollama pull nomic-embed-text
else
  echo "nomic-embed-text model already present."
fi

echo "All done!"
