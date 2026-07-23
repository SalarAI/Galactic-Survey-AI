from fastapi import FastAPI

app = FastAPI(
    title="Galactic Survey AI API",
    description="Backend API for Galactic Survey AI space exploration game",
    version="0.1.0"
)


@app.get("/")
def home():
    return {
        "message": "Welcome to Galactic Survey AI",
        "status": "online",
        "version": "0.1.0"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }
