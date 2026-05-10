import pytest
import allure

from clients.httpbin_client import HttpBinClient

@allure.feature("Resiliency")
@allure.story("Retry Handling")
@pytest.mark.resiliency
class TestRetryBehavior:

  #  client = HttpBinClient()

    def test_retry_on_503(self, httpbin_client):

        with pytest.raises(Exception):

          #  self.client.get_status(503)
            httpbin_client.get_status(503)
