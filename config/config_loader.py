import yaml
import os

class ConfigLoader:

    _config = None

    @classmethod
    def load_config(cls):

        if cls._config is None:

            env = os.getenv(
                "TEST_ENV",
                "qa"
            )

            config_path = os.path.join(
                os.path.dirname(__file__),
                f"{env}.yaml"
            )

            if not os.path.exists(config_path):
                raise FileNotFoundError(
                    f"Config file not found: {config_path}"
                )

            with open(config_path, "r") as file:
                cls._config = yaml.safe_load(file)

        return cls._config

