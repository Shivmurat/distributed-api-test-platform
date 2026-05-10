import time

from utils.logger import Logger

class PollingHelper:

    logger = Logger.get_logger()

    @staticmethod
    def poll(function, timeout=30, interval=2, expected_value=True):

        start_time = time.time()

        while time.time() - start_time < timeout:

            try:
                result = function()
                PollingHelper.logger.info(f"Polling result: {result}")

                if result == expected_value:
                    PollingHelper.logger.info("Expected polling result achieved")
                    return True

            except Exception as error:
                PollingHelper.logger.warning(f"Polling attempt failed: {error}")

            time.sleep(interval)

        raise TimeoutError(f"Polling timeout after {timeout} seconds")

