# import logging

# logging.basicConfig(
#     level=logging.DEBUG,
#     format="[%(asctime)s|%(levelname)s|%(name)s] %(message)s",
# )


# class APITestsLogger:
#     @staticmethod
#     def get_logger():
#         logger = logging.getLogger(name="API_LOGGER")
#         logger.setLevel(level=logging.DEBUG)
#         logger.propagate = False
#
#         APITestsLogger._add_file_handler(logger)
#         APITestsLogger._add_console_handler(logger)
#
#         return logger
#
#     @staticmethod
#     def _add_file_handler(logger):
#         if not any(isinstance(handler, logging.FileHandler) for handler in logger.handlers):
#             file_handler = logging.FileHandler(filename="api_tests.log", encoding="utf-8")
#             file_handler.setLevel(level=logging.DEBUG)
#             file_formatter = logging.Formatter(fmt="[%(asctime)s|%(levelname)s|%(name)s] %(message)s")
#             file_handler.setFormatter(file_formatter)
#             logger.addHandler(file_handler)
#
#     @staticmethod
#     def _add_console_handler(logger):
#         if not any(
#             isinstance(handler, logging.StreamHandler)
#             for handler in logger.handlers
#             if not isinstance(handler, logging.FileHandler)
#         ):
#             console_handler = logging.StreamHandler()
#             console_handler.setLevel(level=logging.INFO)
#             console_formatter = logging.Formatter(fmt="[%(asctime)s|%(levelname)s|%(name)s] %(message)s")
#             console_handler.setFormatter(console_formatter)
#             logger.addHandler(console_handler)
#
#
# logger = APITestsLogger.get_logger()


import logging.config
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent.parent

api_logger = {
    "version": 1,
    "formatters": {
        "standard": {
            "format": "[%(asctime)s|%(levelname)s|%(name)s] %(message)s",
        }
    },
    "handlers": {
        "file": {
            "class": "logging.handlers.RotatingFileHandler",
            "level": "DEBUG",
            "formatter": "standard",
            "filename": str(PROJECT_ROOT / "api_tests.log"),
            "maxBytes": 10_000_000,
            "backupCount": 5,
        },
        "console": {
            "class": "logging.StreamHandler",
            "level": "INFO",
            "formatter": "standard",
        },
    },
    "loggers": {
        "API_LOGGER": {
            "level": "DEBUG",
            "handlers": ["file", "console"],
            "propagate": False,
        }
    },
}


logging.config.dictConfig(api_logger)
logger = logging.getLogger(name="API_LOGGER")
