from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "postgresql://neondb_owner:npg_9BqYgSWUnaG7@ep-patient-rain-aqv1koks.c-8.us-east-1.aws.neon.tech/neondb?sslmode=require"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()