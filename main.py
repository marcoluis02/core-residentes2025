from fastapi import FastAPI
from app.core.db import Base, engine
from app.routes import albums_handler
from app.models.albums import Album
import uvicorn

Base.metadata.create_all(bind=engine)

app = FastAPI(title="CRUD genérico implementado a Carros")

app.include_router(albums_handler.router)

if __name__ == "__main__":
    uvicorn.run(app,host="0.0.0.0", port=8000)