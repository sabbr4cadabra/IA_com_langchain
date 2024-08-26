from codigo import chain
from fastapi import FastAPI
from langserve import add_routes

app = FastAPI(
  title="My first API IA with Langchain",
  version="1.0",
  description="A simple API server using LangChain's Runnable interfaces",
)

# 5. Adding chain route

add_routes(
    app,
    chain,
    path="/translate",
)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="localhost", port=8000)