from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import auth, users
from starlette.middleware.sessions import SessionMiddleware
from core.config import settings

app = FastAPI(title="Mi API de Producción")

# Configuración de CORS
origins = [
    "http://localhost:3000",
    "http://localhost:8080",
    "http://localhost:5173",
    "http://localhost:5174",
    settings.FRONTEND_URL,
    # Añade aquí tu dominio de producción (ej: https://mi-app.com)
]

app.add_middleware(SessionMiddleware, secret_key=settings.SECRET_KEY)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_middleware(
    SessionMiddleware, 
    secret_key=settings.SECRET_KEY, 
    https_only=True,
    same_site="none"   
)

# Incluir Routers
app.include_router(auth.router, prefix="/auth") # Las rutas serán /auth/register y /auth/token
app.include_router(users.router)

@app.get("/")
async def root():
    return {"message": "API funcionando correctamente"}