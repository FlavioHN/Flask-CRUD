from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from database import db
from flask_migrate import Migrate
from routes.usuario import bp_usuarios


app = Flask(__name__)

db = SQLAlchemy()
app.config["SECRET_KEY"] = "minha-chave"
conexao = 'sqlite:///meubanco.sqlite'
app.config["SQLALCHEMY_DATABASE_URI"] = conexao
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = "False"
db.init_app(app)

app.register_blueprint(bp_usuarios, url_prefix="/usuarios")

migrate = Migrate(app, db)

@app.route('/')
def index():
    return render_template("index.html")



if __name__ == "__main__":
    app.run(
        debug=True,
        port=3000
    )