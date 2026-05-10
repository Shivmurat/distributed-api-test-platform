import pytest

from clients.base_client import BaseClient

class TestBaseClient:

    client = BaseClient()

    def test_retry_for_failure(self):
        with pytest.raises(Exception):
            self.client.get("/invalid-endpoint")


  #  def test_connection_retry(self):
   #         self.client.get("/health")

