from database import drop_db, start_db

if __name__ == "__main__":
    # deleta todos os dados do db
    drop_db()
    # inicia os dados dos models todos novamente
    start_db()
