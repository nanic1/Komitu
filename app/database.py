from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Conectar o codigo com o banco de dados
engine = create_engine('mysql+mysqlconnector://root:004517@localhost:3306/komitu', echo=True)
SessionLocal = sessionmaker(bind=engine)