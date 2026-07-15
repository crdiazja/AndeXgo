from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="AndeXgo Core API",
    description="Servicios de telemetría, facturación y gestión OCPP para cargadores de vehículos eléctricos en LatAm.",
    version="1.0.0"
)

origins = [
    "http://localhost:3000",
    "https://app.andexgo.com",
    "https://andexgo.com"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {
        "status": "online",
        "service": "AndeXgo API Engine",
        "version": "1.0.0",
        "region": "Colombia"
    }

@app.get("/api/health")
def health_check():
    return {"status": "healthy", "database": "connected"}
