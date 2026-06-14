from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Shared Expense App",
    description="Spreetail Assignment",
    version="1.0.0"
)

# CORS

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    return {
        "message": "Shared Expense App Running Successfully"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


# Routers will be added later

# auth router

# groups router

# expenses router

# importcsv router

# settlements router