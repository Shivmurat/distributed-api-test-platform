from clients.httpbin_client import HttpBinClient

from utils.assertions import Assertions


class TestPostPayload:

    client = HttpBinClient()

    def test_post_payload(self):

        payload = {
            "name": "Shiv",
            "role": "SDET"
        }

        response = self.client.post_payload(payload)

        Assertions.assert_status_code(
            response.status_code,
            200
        )

        response_json = response.json()

        Assertions.assert_equals(
            response_json["json"]["name"],
            "Shiv"
        )