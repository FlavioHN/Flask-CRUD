from database import db

class Usuario(db.Model):
    __tablename__='usuario'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    sobrenome = db.Column(db.String(50))
    email = db.Column(db.String(10))
    senha = db.Column(db.String(20))


def __init__(self, nome, sobrenome, email, senha):
    self.nome = nome
    self.sobrenome = sobrenome
    self.email = email
    self.senha = senha


def __repr__(self):
    return f'Usuario: {self.nome, self.sobrenome}'