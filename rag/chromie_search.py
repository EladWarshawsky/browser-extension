import chromadb
from chromadb.config import Settings

# Step 1: Initialize the PersistentClient to access the stored data
client = chromadb.PersistentClient(
    path="./chroma_db",  # Path to the persistent database directory
    settings=Settings()
)

# Step 2: Access the collection that was previously created
collection_name = "task_history_collection"
collection = client.get_collection(collection_name)

# Step 3: Query the collection for relevant documents
# You can modify this query text to fit what you're searching for
query_text = "the action in which the model is successful"
results = collection.query(query_texts=[query_text], n_results=1)  # Get top 5 relevant results

# Step 4: Print the query results
print("Relevant Documents:")
for doc in results['documents']:
    print(doc)