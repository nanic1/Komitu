from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Conectar o codigo com o banco de dados
Base = declarative_base()
engine = create_engine('mysql+mysqlconnector://root:004517@localhost:3306/komitu', echo=True)
SessionLocal = sessionmaker(bind=engine)

def start_db():
    Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()