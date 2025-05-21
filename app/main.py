from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi

from app.api.auth import router as auth_router
from app.api.corpus_api import router as corpus_router
from app.api.algorithm_api import router as algorithm_router

app = FastAPI(title="Fuzzy-Search API", version="0.1.0")

app.include_router(auth_router)
app.include_router(corpus_router)
app.include_router(algorithm_router)


def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema

    openapi_schema = get_openapi(
        title=app.title,
        version=app.version,
        description="FastAPI + SQLite + SQLAlchemy + JWT authentication",
        routes=app.routes,
    )

    openapi_schema.setdefault("components", {}).setdefault("securitySchemes", {})["BearerAuth"] = {
        "type": "http",
        "scheme": "bearer",
        "bearerFormat": "JWT",
    }

    for path, methods in openapi_schema["paths"].items():
        if path in ("/auth/signup", "/auth/token"):
            continue
        for operation in methods.values():
            operation["security"] = [{"BearerAuth": []}]

    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi