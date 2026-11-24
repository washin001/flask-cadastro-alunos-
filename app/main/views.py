from datetime import datetime

from flask import flash, redirect, render_template, url_for

from . import main
from .forms import AlunoForm
from .. import db
from ..models import Aluno

ALUNO_NOME = 'Washington N Sousa'
ALUNO_PRONTUARIO = 'PT303755X'


@main.route('/')
def index():
    return render_template(
        'index.html',
        aluno=ALUNO_NOME,
        prontuario=ALUNO_PRONTUARIO,
        current_time=datetime.utcnow(),
    )


@main.route('/alunos', methods=['GET', 'POST'])
def alunos():
    form = AlunoForm()
    if form.validate_on_submit():
        prontuario = form.prontuario.data.strip().upper()
        if Aluno.query.filter_by(prontuario=prontuario).first():
            flash('Já existe um aluno com esse prontuário.', 'danger')
        else:
            db.session.add(Aluno(nome=form.nome.data.strip(), prontuario=prontuario))
            db.session.commit()
            flash('Aluno cadastrado com sucesso!', 'success')
            return redirect(url_for('main.alunos'))
    lista = Aluno.query.order_by(Aluno.id.desc()).all()
    return render_template('alunos.html', form=form, alunos=lista)
