from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship, declarative_base, sessionmaker
from database import Base
from datetime import datetime

# Models para os Usuarios
class Users(Base):
    __tablename__ = "users"

    id = Column("id", Integer, primary_key=True)
    nickname = Column("nick", String(25), unique=True)
    nome = Column("nome", String(70))
    email = Column("email", String(100))
    senha = Column("senha", String(100))
    bio = Column("bio", Text, nullable=True)
    foto_perfil = Column("foto_perfil", String(200), nullable=True) # planejo armazenar em URL
    data_criacao = Column(DateTime, default=datetime.utcnow)

# Models para os Posts
class Posts(Base):
    __tablename__ = "posts"

    id = Column("id", Integer, primary_key=True)
    user_id = Column("user_id", Integer, ForeignKey("users.id"), nullable=False)
    conteudo = Column("conteudo", Text)
    imagem = Column("imagem", String(200), nullable=True)
    data_criacao = Column(DateTime, default=datetime.utcnow)

# Models para os comentarios nos Posts
class Comments(Base):
    __tablename__ = "comments"

    id = Column("id", Integer, primary_key=True)
    user_id = Column("user_id", Integer, ForeignKey("users.id"), nullable=False)
    post_id = Column("post_id", Integer, ForeignKey("posts.id"), nullable=False)
    comentario = Column("comentario", Text, nullable=False)
    data_criacao = Column(DateTime, default=datetime.utcnow)

# Models para os Likes nos Posts
class Likes(Base):
    __tablename__ = "likes"

    id = Column("id", Integer, primary_key=True)
    user_id = Column("user_id", Integer, ForeignKey('users.id'), nullable=False)
    post_id = Column("post_id", Integer, ForeignKey('posts.id'), nullable=False)

    __table_args__ = (
        UniqueConstraint('user_id', 'post_id', name='uix_user_post'),
    )

# Models para os Follows no Perfil
class Follows(Base):
    __tablename__ = "follows"

    id = Column("id", Integer, primary_key=True)
    seguidor_id = Column("seguidor_id", Integer, ForeignKey("users.id"))
    seguindo_id = Column("seguindo_id", Integer, ForeignKey("users.id"))

    __table_args__ = (UniqueConstraint('seguidor_id', 'seguindo_id', name='uix_seguidor_seguindo'),)