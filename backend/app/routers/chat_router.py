from fastapi import APIRouter
from app.schemas.chat_router_schemas import ChatRouterRequest
from app.models.gemini_models import GEMINIModel
from app.configs.const import GEMINI_MODEL_NAME, GEMINI_API_KEY
from app.logs.logger_config import logger


chat_router = APIRouter()
GEMINIModel_OBJECT = GEMINIModel(
    model_name=GEMINI_MODEL_NAME,
    max_tokens = 3000,
    temperature= 0.5,
    api_key=GEMINI_API_KEY
)


@chat_router.post("/get_response/")
async def get_response(request: ChatRouterRequest):

    # user_qeury = request.data.user_query
    history = request.history
    query = request.query
    logger.info(f"Received query : {query}")
    logger.info(f"Received history : {history}")

    if None in [query, history]:
        raise ValueError("Query and history cannot be None")

    GEMINIModel_OBJECT(query=query, history=history)
