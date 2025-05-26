from pydantic import BaseModel, HttpUrl
from typing import Sequence


class ChatRouterRequest(BaseModel):
    user_id: str = None
    query :str