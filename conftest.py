import pytest

from clients.httpbin_client import HttpBinClient



@pytest.fixture(scope="class")
def httpbin_client():

    return HttpBinClient()
