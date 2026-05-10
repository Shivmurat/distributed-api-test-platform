from utils.polling_helper import PollingHelper


class TestPolling:

    counter = 0

    def async_operation(self):
        self.counter += 1

        print(f"Executoin count: {self.counter}")
        return self.counter == 3

    def test_polling(self):

        result = PollingHelper.poll(
            function=self.async_operation,
            timeout=10,
            interval=1,
            expected_value=True
        )

        assert result is True