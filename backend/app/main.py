from fastapi import FastAPI

app = FastAPI(title="AI Chat Backend")


@app.get("/health")
async def health():
    return {"status": "ok"}