from typing import Union

from fastapi import FastAPI
from app.liveness import liveness_router
from app.readiness import readiness_router
from app.customers import customer_router
from app.version import version_router
from app.version import semver

tags_metdata = [
    {
        "name": "liveness",
        "description": "Check if service is up, i.e.: Can reach service."
    },
    {
        "name": "readiness",
        "description": "Check if service is ready, i.e.: Can connect/save to DB, can complete transaction, etc."
    },
    {
        "name": "version",
        "description": "Details about current version, i.e.: version, commit, branch"
    },
    {
        "name": "customers",
        "description": "Endpoint for for managing customer records."
    }
]

app = FastAPI(
    title="Customers API",
    description="API for managing customers",
    version=semver.current_version,
    openapi_tags=tags_metdata
)

app.include_router(liveness_router.router, prefix="/liveness")
app.include_router(readiness_router.router, prefix="/rediness")
app.include_router(version_router.router, prefix="/version")
app.include_router(customer_router.router, prefix="/customers")

# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}