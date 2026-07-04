from fastapi import FastAPI

app = FastAPI(
    title="API de Clientes",
    version="1.0.0"
)

@app.get("/")
def inicio():
    return {
        "mensaje": "Proyecto FastAPI iniciado correctamente"
    }