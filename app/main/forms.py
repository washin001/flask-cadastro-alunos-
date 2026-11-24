from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length


class AlunoForm(FlaskForm):
    nome = StringField('Nome do aluno', validators=[DataRequired(), Length(1, 100)])
    prontuario = StringField('Prontuário', validators=[DataRequired(), Length(1, 20)])
    submit = SubmitField('Cadastrar')
