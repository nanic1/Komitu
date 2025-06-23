from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import DATABASE_URL

# Conectar o codigo com o banco de dados
engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(bind=engine)