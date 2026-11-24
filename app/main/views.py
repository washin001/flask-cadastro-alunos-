from datetime import datetime

from flask import flash, redirect, render_template, url_for

from . import main
from .forms import AlunoForm
from .. import db
from ..models import Aluno, Disciplina

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
    form.disciplina.choices = [
        (d.id, d.nome) for d in Disciplina.query.order_by(Disciplina.nome).all()
    ]
    if form.validate_on_submit():
        db.session.add(Aluno(nome=form.nome.data.strip(), disciplina_id=form.disciplina.data))
        db.session.commit()
        flash('Aluno cadastrado com sucesso!', 'success')
        return redirect(url_for('main.alunos'))
    lista = Aluno.query.order_by(Aluno.id.desc()).all()
    return render_template('alunos.html', form=form, alunos=lista)
