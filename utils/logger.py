import logging
import os

from datetime import datetime
from config.config_loader import ConfigLoader


class Logger:

    _logger = None

    @classmethod
    def get_logger(cls):

        if cls._logger is None:

            config = ConfigLoader.load_config()

            log_level = config.get(
                "log_level",
                "INFO"
            ).upper()

            log_dir = "logs"

            if not os.path.exists(log_dir):
                os.makedirs(log_dir)

            cls._logger = logging.getLogger(
                "distributed-api-test-platform"
            )

            level_mapping = {
                "DEBUG": logging.DEBUG,
                "INFO": logging.INFO,
                "WARNING": logging.WARNING,
                "ERROR": logging.ERROR,
                "CRITICAL": logging.CRITICAL
            }

            cls._logger.setLevel(
                level_mapping.get(
                    log_level,
                    logging.INFO
                )
            )

            formatter = logging.Formatter(
                "%(asctime)s | "
                "%(levelname)s | "
                "%(message)s"
            )

            timestamp = datetime.now().strftime(
                "%Y%m%d_%H%M%S"
            )

            log_file = (
                f"logs/framework_{timestamp}.log"
            )

            file_handler = logging.FileHandler(log_file)

            file_handler.setFormatter(formatter)

            console_handler = logging.StreamHandler()

            console_handler.setFormatter(formatter)

            cls._logger.addHandler(file_handler)

            cls._logger.addHandler(console_handler)

        return cls._logger