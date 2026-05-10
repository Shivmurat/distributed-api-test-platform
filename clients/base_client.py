import json
from asyncio import timeout
from http.client import responses

import requests

from config.config_loader import ConfigLoader
from utils.logger import Logger
from utils.retry_handler import RetryHandler
from requests.exceptions import (
    HTTPError,
    Timeout,
    ConnectionError
)


class BaseClient:

    def __init__(self):
        self.config = ConfigLoader.load_config()
        self.base_url = self.config.get("base_url")
        self.timeout = self.config.get("timeout", 30)
        self.headers = self.config.get("headers", {})
        self.logger = Logger.get_logger()

    @RetryHandler.retry(retries=3, delay=2, exceptions=(Timeout,ConnectionError,HTTPError))
    def get(self, endpoint, params=None):
        url = f"{self.base_url}{endpoint}"

        self.logger.info(f"GET Request started | URL {url}")

        response = requests.get(
            url=url,
            headers=self.headers,
            params=params,
            timeout=self.timeout
        )

        self.logger.info(
            f"GET response recieved |"
            f"Status code: {response.status_code}"
        )

        if response.status_code >= 500:
            self.logger.error(f"Server Error Response: {response.status_code}")
            response.raise_for_status()

        self.logger.debug(
            f"Respose Body: "
            f"{json.dumps(response.json(), indent=4)}"
        )

        return response

    def post(self, endpoint, payload=None):
        url = f"{self.base_url}{endpoint}"

        self.logger.info(
            f"POST Request Started | URL: {url}"
        )

        self.logger.debug(
            f"Request Payload: "
            f"{json.dumps(payload, indent=4)}"
        )

        response = requests.post(
            url=url,
            headers=self.headers,
            json=payload,
            timeout=self.timeout
        )

        self.logger.info(
            f"POST Response Received | "
            f"Status Code: {response.status_code}"
        )

        if response.status_code >= 500:
            self.logger.error(f"Server Error Response: {response.status_code}")
            response.raise_for_status()

        self.logger.debug(
            f"Response Body: "
            f"{json.dumps(response.json(), indent=4)}"
        )

        return response

