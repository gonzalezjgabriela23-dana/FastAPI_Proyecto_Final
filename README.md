# 📌 API de Gestión de Clientes, Facturas y Transacciones

Este proyecto es una API REST desarrollada con **FastAPI**, que permite gestionar clientes, facturas y transacciones con operaciones CRUD completas y validaciones entre entidades.

---

## 🚀 Funcionalidades

- Gestión completa de **Clientes**
- Gestión de **Facturas** asociadas a clientes
- Gestión de **Transacciones** asociadas a facturas
- Validación de relaciones entre entidades
- Manejo de errores con `HTTPException`
- Arquitectura modular con `APIRouter`
- Documentación automática con Swagger y ReDoc

---

## 🛠️ Tecnologías utilizadas

- Python 3.13
- FastAPI
- Uvicorn
- Pydantic

---

## 📁 Estructura del proyecto
├── main.py # Punto de entrada de la API
├── clientes.py # CRUD de clientes
├── facturas.py # CRUD de facturas
├── transacciones.py # CRUD de transacciones
├── requirements.txt # Dependencias del proyecto
├── .gitignore # Archivos ignorados por Git
└── README.md # Documentación del proyecto

---

## ⚙️ Instalación y ejecución

### 1. Clonar el repositorio

```bash
git clone https://github.com/tu-usuario/tu-repositorio.git
cd tu-repositorio
