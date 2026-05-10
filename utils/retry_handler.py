import time

from utils.logger import Logger


class RetryHandler:

    logger = Logger.get_logger()

    @staticmethod
    def retry(retries=3, delay=2, exceptions=(Exception, )):

        def decorator(func):

            def wrapper(*args, **kwargs):

                for attempt in range(1, retries + 1):

                    try:

                        RetryHandler.logger.info(
                            f"Attempt {attempt} for function: {func.__name__}"
                        )

                        return func(*args, **kwargs)

                    except exceptions as error:

                        RetryHandler.logger.warning(
                            f"Retry attempt {attempt} failed. Error: {error}"
                        )

                        if attempt == retries:

                            RetryHandler.logger.error(
                                f"All retry attempts failed for {func.__name__}"
                            )

                            raise

                        time.sleep(delay)

            return wrapper

        return decorator