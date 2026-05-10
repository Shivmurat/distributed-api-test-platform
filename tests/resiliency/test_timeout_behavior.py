import pytest

from clients.httpbin_client import HttpBinClient


class TestTimeoutBehavior:

 #   client = HttpBinClient()

    def test_timeout_retry(self, httpbin_client):

       # self.client.timeout = 2
        httpbin_client.timeout = 2

        with pytest.raises(Exception):

         #   self.client.get_delayed_response(10)
            httpbin_client.get_delayed_response(10)