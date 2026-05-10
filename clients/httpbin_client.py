from clients.base_client import BaseClient

class HttpBinClient(BaseClient):

    def get_status(self, status_code):
        return self.get(f"/status/{status_code}")

    def get_delayed_response(self, delay):
        return self.get(f"/delay/{delay}")

    def get_headers(self):
        return self.get("/headers")

    def post_payload(self, payload):
        return self.post("/post", payload)