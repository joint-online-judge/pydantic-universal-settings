import uvicorn

from example.config import AllSettings, settings
from pydantic_universal_settings import cli, init_settings


@cli.command()
def main() -> None:
    init_settings(AllSettings)
    uvicorn.run(
        "example.app:app",
        debug=settings.debug,
        reload=settings.debug,
        reload_dirs=["example", "pydantic_universal_settings"],
    )


if __name__ == "__main__":
    main()
