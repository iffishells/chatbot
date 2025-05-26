from importlib.resources import contents

from google import genai
from app.logs.logger_config import logger
from app.configs.const import GEMINI_API_KEY
class GEMINIModel:
    def __init__(self,
                 model_name: str,
                 max_tokens: int,
                 temperature: float,
                 api_key : str
                 ):
        self.model_name = model_name
        self.max_tokens = max_tokens
        self.temperature = temperature
        self.api_key =api_key
        logger.info(f"Gemini Model : {self.api_key }")
        self.client = genai.Client(api_key=self.api_key )

    def __repr__(self):
        return f"GeminiModel(model_name={self.model_name}, max_tokens={self.max_tokens}, temperature={self.temperature})"

    def get_response(self,query,history):

        logger.info(f"Query: {query}")
        logger.info(f"History: {history}")
        history_text = "\n".join([msg["role"] + ": " + msg["message"] for msg in history])
        concat_history_chat = history_text + "\nuser: " + query
        try:
            response = self.client.models.generate_content(
                model =self.model_name,
                contents = concat_history_chat)
            logger.info("Response from Gemini: %s", response.text)
            return response.text
        except Exception as e:
            logger.error("Error generating response: %s", str(e))
            return f"Sorry, an error occurred: {str(e)}"


    def __call__(self,query:str=None,
                 history:str=None):

        self.get_response(query=query,history=history)