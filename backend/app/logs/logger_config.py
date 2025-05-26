# logger_config/logger.py

import logging
from logging.handlers import RotatingFileHandler
import os

# Ensure log directory exists
LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

# Log file path
LOG_FILE_PATH = os.path.join(LOG_DIR, "application.log")

# Logger setup
logger = logging.getLogger("app_logger")
logger.setLevel(logging.INFO)

# Prevent multiple handlers in reload
if not logger.hasHandlers():
    formatter = logging.Formatter(
        "%(asctime)s — %(name)s — %(levelname)s — %(message)s"
    )

    file_handler = RotatingFileHandler(LOG_FILE_PATH, maxBytes=5_000_000, backupCount=3)
    file_handler.setFormatter(formatter)

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)