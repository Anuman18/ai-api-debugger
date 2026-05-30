from pydantic import BaseModel

class ErrorRequest(BaseModel):
    api_name: str
    error_message: str