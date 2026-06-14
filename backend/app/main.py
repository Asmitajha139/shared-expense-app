from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import groups
from app.routes import groups, expenses
from app.routes import groups, expenses, settlements
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

app.include_router(
    groups.router,
    prefix="/groups",
    tags=["Groups"]
)

# expenses router
app.include_router(
    groups.router,
    prefix="/groups",
    tags=["Groups"]
)

app.include_router(
    expenses.router,
    prefix="/expenses",
    tags=["Expenses"]
)

# importcsv router

# settlements router
app.include_router(
    settlements.router,
    prefix="/settlements",
    tags=["Settlements"]
)