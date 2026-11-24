from datetime import datetime

from . import db


class Aluno(db.Model):
    __tablename__ = 'alunos'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    prontuario = db.Column(db.String(20), unique=True, index=True, nullable=False)
    data_cadastro = db.Column(db.DateTime, default=datetime.utcnow)
