from typing import Type, Union

from pydantic_universal_settings import (
    BaseSettings,
    CLIWatchMixin,
    EnvFileMixin,
    add_settings,
    generate_all_settings,
    get_settings_proxy,
)


@add_settings
class BaseConfig(BaseSettings):
    debug: bool = False
    host: str = "localhost"
    port: int


GeneratedSettings: Type[Union[BaseConfig]] = generate_all_settings(
    mixins=[EnvFileMixin, CLIWatchMixin]
)


class AllSettings(GeneratedSettings):  # type: ignore
    pass


settings: AllSettings = get_settings_proxy()  # type: ignore
