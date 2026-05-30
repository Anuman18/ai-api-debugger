from fastapi import APIRouter

from models.request_models import ErrorRequest
from services.analyze_service import analyze_error_logic

router = APIRouter()

@router.post("/analyze")
def analyze_error(data: ErrorRequest):

    result = analyze_error_logic(
        data.api_name,
        data.error_message
    )

    return result