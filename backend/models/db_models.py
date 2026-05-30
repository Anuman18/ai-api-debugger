from sqlalchemy import Column, Integer, String, Text
from database import Base

class DebugSession(Base):

    __tablename__ = "debug_sessions"

    id = Column(Integer, primary_key=True, index=True)

    api_name = Column(String)

    error_message = Column(Text)

    category = Column(String)

    confidence_score = Column(String)

    ai_explanation = Column(Text)