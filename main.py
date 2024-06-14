
from fastapi import FastAPI

app = FastAPI()

# Import and use routers from the routers folder
from app.routers import items  # Example import

app.include_router(items.router)

# Additional routes and app configuration can be added here
