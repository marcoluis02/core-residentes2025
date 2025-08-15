from fastapi import FastAPI
from app.core.db import Base, engine
from app.routes import clientes_handler
from app.models.clientes import Cliente

# Crear todas las tablas (si no existen)
Base.metadata.create_all(bind=engine)

app = FastAPI(title="CRUD genérico implementado a Clientes")

# Incluir el router de clientes
app.include_router(clientes_handler.router)