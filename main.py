from fastapi import FastAPI
from app.core.db import Base, engine
from app.routes import carros_handler
from app.models.carros import Carro

Base.metadata.create_all(bind=engine)

app = FastAPI(title="CRUD genérico implementado a Carros")

app.include_router(carros_handler.router)