from typing import Type, Union

from pydantic_universal_settings import (
    add_settings,
    BaseSettings,
    generate_all_settings,
    EnvFileMixin,
    CLIMixin,
    get_settings_proxy,
)


@add_settings
class BaseConfig(BaseSettings):
    debug: bool = False
    host: str = "localhost"
    port: int = 9000


GeneratedSettings: Type[Union[BaseConfig]] = generate_all_settings(
    mixins=[EnvFileMixin, CLIMixin]
)


class AllSettings(GeneratedSettings):
    pass


settings: AllSettings = get_settings_proxy()




