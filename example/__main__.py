from example.config import AllSettings, settings
from pydantic_universal_settings import cli, init_settings


@cli.command()
def main() -> None:
    init_settings(AllSettings)
    print(repr(settings))


if __name__ == "__main__":
    main()
