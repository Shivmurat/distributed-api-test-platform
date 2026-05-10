import pytest

from clients.httpbin_client import HttpBinClient

from utils.assertions import Assertions

@pytest.mark.smoke
class TestHeadersAPI:

    client = HttpBinClient()

    def test_headers(self, httpbin_client):

        response = httpbin_client.get_headers()

        Assertions.assert_status_code(
            response.status_code,
            200
        )

        response_json = response.json()

        Assertions.assert_key_exists(
            response_json,
            "headers"
        )