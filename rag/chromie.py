import json
import chromadb
from chromadb.config import Settings

# Initialize the PersistentClient to store data persistently
client = chromadb.PersistentClient(
    path="./chroma_db",  # Directory to store the persistent database
    settings=Settings()
)

# Load the JSON data from the file
file_path = 'taskHistory.json'  # Update this to your file path
with open(file_path, 'r', encoding='utf-8') as file:
    task_history = json.load(file)

# Create a collection or get the existing one
collection_name = "task_history_collection"
try:
    collection = client.create_collection(collection_name)
except chromadb.errors.UniqueConstraintError: 
    collection = client.get_collection(collection_name)

# Add documents to the collection
collection.add(
    documents=[json.dumps(task) for task in task_history],  # Convert tasks to JSON strings
    ids=[str(i) for i in range(len(task_history))]  # Generate unique IDs
)

print(f"Inserted {len(task_history)} tasks into the ChromaDB collection '{collection_name}'.")
