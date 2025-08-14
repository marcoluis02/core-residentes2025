from fastapi import FastAPI
from app.core.db import Base, engine
from app.routes import usuarios_handler
from app.models.usuarios import Usuario
import uvicorn  


Base.metadata.create_all(bind=engine)

app = FastAPI(title="CRUD genérico implementado a Usuarios")

app.include_router(usuarios_handler.router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
