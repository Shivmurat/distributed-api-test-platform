import time

import requests

from config.config_loader import ConfigLoader
from utils.logger import Logger


class AuthClient:

    logger = Logger.get_logger()

    _token = None

    _token_expiry = 0

    @classmethod
    def authenticate(cls):

        config = ConfigLoader.load_config()

        auth_url = config.get("auth_url")

        credentials = {
            "username": config.get("username"),
            "password": config.get("password")
        }

        cls.logger.info(
            "Generating new auth token"
        )

        response = requests.post(
            auth_url,
            json=credentials
        )

        response.raise_for_status()

        response_json = response.json()

        cls._token = response_json["token"]

        cls._token_expiry = (
            time.time() + response_json.get(
                "expires_in",
                3600
            )
        )

        return cls._token