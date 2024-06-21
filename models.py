from database import db

class Usuario(db.Model):
    __tablename__ = "usuario"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(length=20))
    sobrenome = db.Column(db.String(length=50))
    email = db.Column(db.String(length=100))
    senha = db.Column(db.String(length=20))

    def __init__(self, nome, sobrenome, email, senha):
        self.nome = nome
        self.sobrenome = sobrenome
        self.email = email
        self.senha = senha

    def __repr__(self):
        return "Usuario: {}".format(self.nome, self.sobrenome)