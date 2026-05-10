from utils.logger import Logger

class Assertions:

    logger = Logger.get_logger()

    @staticmethod
    def assert_status_code(actual, expected):

        Assertions.logger.info(
            f"Validateing status code | "
            f"Expected: {expected} | "
            f"Actual: {actual}"
        )

        assert actual == expected, (
            f"Equality validation failed. "
            f"Expected: {expected} "
            f"Actual: {actual}"
        )

    @staticmethod
    def assert_equals(actual, expected):
        Assertions.logger.info(
            f"Validating equality | "
            f"Expected: {expected} | "
            f"Actual: {actual}"
        )

        assert actual == expected, (
            f"Equality validation failed. "
            f"Expected: {expected}, "
            f"Actual: {actual}"
        )

    @staticmethod
    def assert_key_exists(data, key):
        Assertions.logger.info(
            f"Validating key existence | Key: {key}"
        )

        assert key in data, (
            f"Key validation failed. "
            f"Missing key: {key}"
        )