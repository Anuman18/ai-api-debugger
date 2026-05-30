from utils.error_patterns import ERROR_PATTERNS
from services.ai_service import generate_ai_explanation
from database import SessionLocal
from models.db_models import DebugSession
from database import SessionLocal
from models.db_models import DebugSession

def analyze_error_logic(api_name: str, error_message: str):

    error_message = error_message.lower()

    best_match = None
    highest_score = 0

    for pattern in ERROR_PATTERNS:

        score = 0

        for keyword in pattern["keywords"]:

            if keyword in error_message:
                score += 1

        if score > highest_score:
            highest_score = score
            best_match = pattern

    if best_match:
        ai_response = generate_ai_explanation(
        error_message,
        best_match["category"]
        )
        confidence = round(
            (highest_score / len(best_match["keywords"])) * 100,
            2
        )
    
        db = SessionLocal()

        new_session = DebugSession(
            api_name="Unknown API",
            error_message=error_message,
            category=best_match["category"],
            confidence_score=f"{confidence}%",
            ai_explanation=ai_response
        )

        db.add(new_session)

        db.commit()

        db.close()


        return {
            "category": best_match["category"],
            "cause": best_match["cause"],
            "solutions": best_match["solutions"],
            "confidence_score": f"{confidence}%"
        }

    return {
    "category": best_match["category"],
    "cause": best_match["cause"],
    "solutions": best_match["solutions"],
    "confidence_score": f"{confidence}%",
    "ai_explanation": ai_response
}