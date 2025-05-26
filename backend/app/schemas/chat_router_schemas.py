from pydantic import BaseModel, HttpUrl
from typing import Sequence


class ChatRouterRequest(BaseModel):
    history: str = None
    query :str