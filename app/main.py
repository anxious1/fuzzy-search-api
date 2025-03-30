from fastapi import FastAPI, Depends
from fastapi.openapi.utils import get_openapi
from app.api import auth, search, ws_search, async_search, corpus_api, algorithm_api

app = FastAPI()


app.include_router(auth.router)
app.include_router(search.router)
app.include_router(ws_search.router)
app.include_router(async_search.router)
app.include_router(corpus_api.router)
app.include_router(algorithm_api.router)



# Правлю OpenAPI схему — подменяю Authorize на Bearer Token
def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="FastAPI",
        version="0.1.0",
        description="Auth with JWT",
        routes=app.routes,
    )
    openapi_schema["components"]["securitySchemes"] = {
        "BearerAuth": {
            "type": "http",
            "scheme": "bearer",
            "bearerFormat": "JWT",
        }
    }
    for path in openapi_schema["paths"]:
        for method in openapi_schema["paths"][path]:
            openapi_schema["paths"][path][method]["security"] = [{"BearerAuth": []}]
    app.openapi_schema = openapi_schema
    return app.openapi_schema

app.openapi = custom_openapi
