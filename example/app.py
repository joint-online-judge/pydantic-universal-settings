from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from example.config import AllSettings
from pydantic_universal_settings import init_settings

init_settings(AllSettings)
app = FastAPI()


@app.get("/")
async def redirect_to_docs() -> RedirectResponse:
    return RedirectResponse(url="/docs?docExpansion=none")
