from app.models import Base
from app.database import engine

# Cria as tabelas
Base.metadata.create_all(engine)