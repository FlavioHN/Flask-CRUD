from flask import Blueprint, render_template, request

bp_usuarios = Blueprint("usuario", __name__, template_folder="templates")

@bp_usuarios.route('/create', methods=["GET"])
def create():
    if request.method == "GET":
        return render_template("usuarios_create.html")

    if request.method == "POST":
        nome = request.form.get("nome")
        email = request.form.get("email")
        senha = request.form.get("senha")
        csenha = request.form.get("csenha")

        return "Dados cadastrados com sucesso!"