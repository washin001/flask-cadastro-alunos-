from flask import render_template

from . import main


@main.app_errorhandler(404)
def pagina_nao_disponivel(e):
    return render_template('nao_disponivel.html'), 404


@main.app_errorhandler(500)
def erro_interno(e):
    return render_template('erro_500.html'), 500
