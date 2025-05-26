import json
import os
from app.logs.logger_config import logger
# read the json file
file_path = "credentials.json"
if os.path.exists(file_path):
    with open("credentials.json", "r") as f:
        data = json.load(f)
else:
    logger.error("credentials.json file not found.")
    raise FileNotFoundError("credentials.json file not found.")



GEMINI_API_KEY = data['GEMINI_API_KEY']
logger.info(f"GEMINI_API_KEY loaded successfully : {GEMINI_API_KEY}")
GEMINI_MODEL_NAME = data['GEMINI_MODEL_NAME']
logger.info(f"GEMINI_MODEL_NAME loaded successfully : {GEMINI_MODEL_NAME}")

