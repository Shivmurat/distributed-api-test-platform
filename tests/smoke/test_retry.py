from utils.retry_handler import RetryHandler


class TestRetry:

    counter = 0

    @RetryHandler.retry(retries=3, delay=1)
    def flaky_function(self):

        self.counter += 1

        print(f"Execution count: {self.counter}")

        if self.counter < 3:
            raise Exception("Temporary failure")

        return "Success"

    def test_flaky_function(self):

        result = self.flaky_function()

        assert result == "Success"