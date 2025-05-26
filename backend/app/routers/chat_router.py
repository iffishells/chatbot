from fastapi import APIRouter, HTTPException
from app.schemas.chat_router_schemas import ChatRouterRequest
from app.models.gemini_models import GEMINIModel
from app.configs.const import GEMINI_MODEL_NAME, GEMINI_API_KEY
from app.logs.logger_config import logger
from app.services.chat_history_services import add_message, get_user_history

chat_router = APIRouter()

# Instantiate once
GEMINIModel_OBJECT = GEMINIModel(
    model_name=GEMINI_MODEL_NAME,
    max_tokens=3000,
    temperature=0.5,
    api_key=GEMINI_API_KEY
)


@chat_router.post("/get_response/")
async def get_response(request: ChatRouterRequest):
    user_id = request.user_id
    query = request.query

    if not user_id or not query:
        raise HTTPException(status_code=400, detail="user_id and query are required")

    logger.info(f"Received query from user {user_id}: {query}")

    # Get previous chat history
    history = get_user_history(user_id)
    logger.info("History: %s", history)

    # Save user query to history
    add_message(user_id, "user", query)

    try:
        # Get Gemini response
        bot_response = GEMINIModel_OBJECT.get_response(query=query, history=history)  # Adjust if method differs
    except Exception as e:
        logger.error(f"Error from Gemini model: {str(e)}", exc_info=True)
        raise HTTPException(status_code=500, detail="Gemini model failed to respond")

    # Save Gemini reply
    add_message(user_id, "bot", bot_response)

    return {
        "user_id": user_id,
        "query": query,
        "response": bot_response,
        "history": get_user_history(user_id)
    }