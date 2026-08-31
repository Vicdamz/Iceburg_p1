from fastapi import FastAPI

# Initialize the API application
app = FastAPI(title="My First API", version="1.0.0")

# 1. Root Endpoint (GET request)
@app.get("/")
def home():
    return {"message": "Welcome to my FastAPI server!", "status": "online"}

# 2. Path Parameter Endpoint
@app.get("/items/{item_id}")
def get_item(item_id: int):
    return {
        "item_id": item_id,
        "name": f"Product #{item_id}",
        "in_stock": True
    }

# 3. Query Parameter Endpoint
@app.get("/search")
def search_items(query: str, limit: int = 10):
    return {
        "search_query": query,
        "results_limit": limit,
        "results": [f"Result {i+1} for '{query}'" for i in range(limit)]
    }